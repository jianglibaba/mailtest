import sys
from PyQt5.Qt import *
from resouce.pane_ui import Ui_Form
from mydata import *


#主窗口页面
class MailPane(QWidget,Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

        # 初始化表格
        self.initTable()


    def initTable(self):
        # 设置表格的列数为4
        self.sql_tw.setColumnCount(4)

        # 水平和垂直方向设置为正好填满表格
        self.sql_tw.horizontalHeader().setStretchLastSection(True)
        self.sql_tw.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置表格的表头，并设置为不可编辑
        headerlabels = ['序号', '账号', '密码', '备注']
        self.sql_tw.setHorizontalHeaderLabels(headerlabels)
        self.sql_tw.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 隐藏id列，不显示数据的id也就是主键，这里的主键只用来删除和修改数据时使用
        self.sql_tw.setColumnHidden(0, True);

        # 不显示单元格
        self.sql_tw.setShowGrid(False)

        # 设置表格选择行为为 只能一行一行选择
        self.sql_tw.setSelectionBehavior(QAbstractItemView.SelectRows)

         #初始化表格数据
        self.flushTable()


    def flushTable(self):
        # 从数据表中获取数据
        data_list = Tools.getData()

        # 设置表格的行数，和数据的数量相关
        self.sql_tw.setRowCount(len(data_list))

        # 设置表格的数据
        for index in range(len(data_list)):
            self.sql_tw.setItem(index, 0, QTableWidgetItem(str(data_list[index][0])))
            self.sql_tw.setItem(index, 1, QTableWidgetItem(data_list[index][1]))
            self.sql_tw.setItem(index, 2, QTableWidgetItem(data_list[index][2]))
            self.sql_tw.setItem(index, 3, QTableWidgetItem(data_list[index][3]))




if __name__ == "__main__":

    app = QApplication(sys.argv)

    myui = MailPane()
    myui.show()
    sys.exit(app.exec_())