# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pane_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(727, 710)
        self.sql_tw = QtWidgets.QTableWidget(Form)
        self.sql_tw.setGeometry(QtCore.QRect(10, 10, 571, 691))
        self.sql_tw.setObjectName("sql_tw")
        self.sql_tw.setColumnCount(0)
        self.sql_tw.setRowCount(0)
        self.register_btn = QtWidgets.QPushButton(Form)
        self.register_btn.setGeometry(QtCore.QRect(610, 20, 91, 31))
        self.register_btn.setObjectName("register_btn")
        self.del_btn = QtWidgets.QPushButton(Form)
        self.del_btn.setGeometry(QtCore.QRect(610, 80, 91, 31))
        self.del_btn.setObjectName("del_btn")
        self.pause_btn = QtWidgets.QPushButton(Form)
        self.pause_btn.setGeometry(QtCore.QRect(610, 140, 91, 31))
        self.pause_btn.setObjectName("pause_btn")
        self.changepwd_btn = QtWidgets.QPushButton(Form)
        self.changepwd_btn.setGeometry(QtCore.QRect(610, 320, 91, 31))
        self.changepwd_btn.setObjectName("changepwd_btn")
        self.save_btn = QtWidgets.QPushButton(Form)
        self.save_btn.setGeometry(QtCore.QRect(610, 260, 91, 31))
        self.save_btn.setObjectName("save_btn")
        self.enable_btn = QtWidgets.QPushButton(Form)
        self.enable_btn.setGeometry(QtCore.QRect(610, 200, 91, 31))
        self.enable_btn.setObjectName("enable_btn")

        self.retranslateUi(Form)
        self.register_btn.clicked.connect(Form.register_slot)
        self.del_btn.clicked.connect(Form.del_slot)
        self.pause_btn.clicked.connect(Form.pause_slot)
        self.save_btn.clicked.connect(Form.save_slot)
        self.changepwd_btn.clicked.connect(Form.changepwd_slot)
        self.enable_btn.clicked.connect(Form.enable_slot)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "邮件管理系统测试版"))
        self.register_btn.setText(_translate("Form", "注册账号"))
        self.del_btn.setText(_translate("Form", "删除账号"))
        self.pause_btn.setText(_translate("Form", "暂停账号"))
        self.changepwd_btn.setText(_translate("Form", "修改密码"))
        self.save_btn.setText(_translate("Form", "保存通讯录"))
        self.enable_btn.setText(_translate("Form", "启用账号"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
