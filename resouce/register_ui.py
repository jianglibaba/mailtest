# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(419, 407)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 42, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 81, 31))
        self.label_3.setObjectName("label_3")
        self.account_le = QtWidgets.QLineEdit(Dialog)
        self.account_le.setGeometry(QtCore.QRect(160, 50, 171, 20))
        self.account_le.setObjectName("account_le")
        self.pwd_le = QtWidgets.QLineEdit(Dialog)
        self.pwd_le.setGeometry(QtCore.QRect(160, 110, 171, 20))
        self.pwd_le.setObjectName("pwd_le")
        self.comment_le = QtWidgets.QLineEdit(Dialog)
        self.comment_le.setGeometry(QtCore.QRect(160, 180, 171, 20))
        self.comment_le.setObjectName("comment_le")
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(60, 280, 75, 23))
        self.ok_btn.setObjectName("ok_btn")
        self.reset_btn = QtWidgets.QPushButton(Dialog)
        self.reset_btn.setGeometry(QtCore.QRect(240, 280, 75, 23))
        self.reset_btn.setObjectName("reset_btn")

        self.retranslateUi(Dialog)
        self.ok_btn.clicked.connect(Dialog.ok_slot)
        self.reset_btn.clicked.connect(Dialog.reset_slot)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "账号："))
        self.label_2.setText(_translate("Dialog", "密码："))
        self.label_3.setText(_translate("Dialog", "备注："))
        self.ok_btn.setText(_translate("Dialog", "确定"))
        self.reset_btn.setText(_translate("Dialog", "重置"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
