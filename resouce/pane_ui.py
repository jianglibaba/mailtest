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
        Form.resize(631, 636)
        self.sql_tw = QtWidgets.QTableWidget(Form)
        self.sql_tw.setGeometry(QtCore.QRect(10, 10, 471, 611))
        self.sql_tw.setObjectName("sql_tw")
        self.sql_tw.setColumnCount(0)
        self.sql_tw.setRowCount(0)
        self.register_btn = QtWidgets.QPushButton(Form)
        self.register_btn.setGeometry(QtCore.QRect(510, 40, 91, 31))
        self.register_btn.setObjectName("register_btn")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 100, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 160, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 220, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 280, 91, 31))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        self.register_btn.clicked.connect(Form.register_slot)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "邮件管理系统测试版"))
        self.register_btn.setText(_translate("Form", "注册账号"))
        self.pushButton_2.setText(_translate("Form", "删除账号"))
        self.pushButton_3.setText(_translate("Form", "暂停账号"))
        self.pushButton_4.setText(_translate("Form", "修改密码"))
        self.pushButton_5.setText(_translate("Form", "保存通讯录"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
