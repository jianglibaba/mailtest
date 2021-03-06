#导入pyqt模块
from PyQt5.Qt import *
#导入主窗口页面ui的py文件
from resouce.pane_ui import Ui_Form
#导入数据库处理文件
from mydata import *
#导入注册页面ui的py文件
from resouce.register_ui import Ui_Dialog




#注册页面
class RegisterPane(QDialog,Ui_Dialog):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def ok_slot(self):
        enable = self.enable_cb.currentText()
        if enable == "启用":
            enable_id = 1
        else:
            enable_id = 0
        # 如果每个输入项都不为空的表示输入正确
        if self.account_le.text() != '' and self.pwd_le.text() != '' and self.dep_le.text() != '' and self.who_le.text() != '':
            # 关闭窗口
            self.close()
            # 在数据库中新增字段
            Tools.addData(self.account_le.text(), self.pwd_le.text(), enable_id, self.dep_le.text(), self.who_le.text())

            # 提示新增成功
            self.showHint('新增成功')
        else:
            self.showHint('必填项不能为空')

    def reset_slot(self):
        self.account_le.clear()
        self.pwd_le.clear()
        self.comment_le.clear()

    def showHint(self, message):

        hint_msg = QMessageBox()
        hint_msg.setText(message)
        hint_msg.addButton(QMessageBox.Ok)
        hint_msg.setWindowTitle("提示")
        hint_msg.exec_()

#主窗口页面
class MailPane(QWidget,Ui_Form):

    newpwd_signal = pyqtSignal(str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

        # 初始化表格
        self.initTable()

        #实例化注册页面类
        self.my_dialog = RegisterPane()

    def initTable(self):
        # 设置表格的列数为5
        self.sql_tw.setColumnCount(5)

        # 水平和垂直方向设置为正好填满表格
        self.sql_tw.horizontalHeader().setStretchLastSection(True)
        self.sql_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置表格的表头，并设置为不可编辑
        headerlabels = [ '账号', '密码', '启用', '部门', '备注']
        self.sql_tw.setHorizontalHeaderLabels(headerlabels)
        self.sql_tw.setEditTriggers(QAbstractItemView.NoEditTriggers)

#        隐藏id列，不显示数据的id也就是主键，这里的主键只用来删除和修改数据时使用
#        self.sql_tw.setColumnHidden(0, True);

        # 不显示单元格
        self.sql_tw.setShowGrid(True)

        # 设置表格选择行为为 只能一行一行选择
        self.sql_tw.setSelectionBehavior(QAbstractItemView.SelectRows)

        #初始化表格数据
        self.flushTable()

        #显示暂停账号为红色
        self.red()

    #刷新数据函数
    def flushTable(self):
        # 从数据表中获取数据
        data_list = Tools.getData()

        # 设置表格的行数，和数据的数量相关
        self.sql_tw.setRowCount(len(data_list))

        # 设置表格的数据
        for index in range(len(data_list)):
       #     self.sql_tw.setItem(index, 0, QTableWidgetItem(str(data_list[index][0])))
            self.sql_tw.setItem(index, 0, QTableWidgetItem(data_list[index][0]))
            self.sql_tw.setItem(index, 1, QTableWidgetItem(data_list[index][1]))
            self.sql_tw.setItem(index, 2, QTableWidgetItem(str(data_list[index][2])))
            self.sql_tw.setItem(index, 3, QTableWidgetItem(data_list[index][3]))
            self.sql_tw.setItem(index, 4, QTableWidgetItem(data_list[index][4]))

    #暂停账号的字体显示红色
    def red(self):
        new_row = Tools.redData()
        column = [0,1,2,3,4]
        for i in column:
            for y in new_row:
                self.sql_tw.item(y, i).setForeground(QBrush(QColor(255, 0, 0)))

    #弹出注册窗口注册槽函数
    def register_slot(self):
        self.my_dialog.exec_()
        # 添加数据后，刷新主窗口页面
        self.flushTable()

    #编辑时弹出的提示窗口
    def editDialog(self,a,b):
        delDialog = QDialog(self)
        delDialog.setWindowTitle(a)
        group = QGroupBox('', delDialog)
        lb1 = QLabel(b)

        ok_button = QPushButton(u'确定', delDialog)
        cancel_button = QPushButton(u'取消', delDialog)

        ok_button.clicked.connect(delDialog.accept)
        ok_button.setDefault(True)
        cancel_button.clicked.connect(delDialog.reject)
        group_layout = QVBoxLayout()
        group_item = [lb1]
        for item in group_item:
            group_layout.addWidget(item)
        group.setLayout(group_layout)
        group.setFixedSize(group.sizeHint())

        button_layout = QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(group)
        dialog_layout.addLayout(button_layout)
        delDialog.setLayout(dialog_layout)
        delDialog.setFixedSize(delDialog.sizeHint())

        # 当点击是(ok)，表示确定返回True
        if delDialog.exec_():
            return True
        # 否则返回False
        return False

    #删除数据槽函数
    def del_slot(self):
        # 选中某行
        selected_row = self.sql_tw.selectedItems()
        if len(selected_row) == 5:

            del_row = self.sql_tw.row(selected_row[0])
            id = self.sql_tw.item(del_row, 0).text()
            a="删除账号"
            b="确定要删除"+id+"吗？？？"

            # 如果返回值为True，表示点击了确定删除
            if self.editDialog(a,b) == True:
                Tools.delData(id)
                self.my_dialog.showHint("删除成功！")
                self.flushTable()

        else:
            # 如果没有选中改行时，点击编辑，弹出提示框
            self.my_dialog.showHint("请选中一行进行删除")

    # 暂停账号的槽函数
    def pause_slot(self):
        # 选中某行
        selected_row = self.sql_tw.selectedItems()
        if len(selected_row) == 5:
            #获取行号（edit_row为行号）
            edit_row = self.sql_tw.row(selected_row[0])
            id = self.sql_tw.item(edit_row, 0).text()

            a = "暂停账号"
            b = "确定要暂停"+id+"吗?"

            # 如果返回值为True，表示点击了确定编辑
            if self.editDialog(a,b) == True:
                Tools.pauseData(id)
                self.my_dialog.showHint("账号已暂停！")
                self.initTable()

        else:
            # 如果没有选中改行时，点击编辑，弹出提示框
            self.my_dialog.showHint("请选中你要暂停的账号!")

    # 暂停账号的槽函数
    def enable_slot(self):
        # 选中某行
        selected_row = self.sql_tw.selectedItems()
        if len(selected_row) == 5:
            # 获取行号（edit_row为行号）
            edit_row = self.sql_tw.row(selected_row[0])
            id = self.sql_tw.item(edit_row, 0).text()

            a = "启用账号"
            b = "确定要启用"+id+"吗?"

            # 如果返回值为True，表示点击了确定编辑
            if self.editDialog(a, b) == True:
                Tools.enableData(id)
                self.my_dialog.showHint("账号已启用！")
                self.initTable()

        else:
            # 如果没有选中改行时，点击编辑，弹出提示框
            self.my_dialog.showHint("请选中你要启用的账号!")

    # 保存为csv文件的槽函数
    def save_slot(self):
        Tools.saveData()
        self.my_dialog.showHint("已保存！")


    #修改密码的槽函数
    def changepwd_slot(self):
        # 选中某行
        selected_row = self.sql_tw.selectedItems()
        if len(selected_row) == 5:

            del_row = self.sql_tw.row(selected_row[0])
            id = self.sql_tw.item(del_row, 0).text()
            a = "修改密码"
            b = "确定修改吗?"

            # 如果返回值为True，表示点击了确定编辑
            if self.editDialog(a,b) == True:
                self.newpwd_signal.emit(id)
                self.my_dialog.showHint("密码已修改！")


        else:
            # 如果没有选中改行时，点击编辑，弹出提示框
            self.my_dialog.showHint("请选中你要修改密码的账号!")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myui = MailPane()
    myui.show()
    sys.exit(app.exec_())