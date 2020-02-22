# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changepwd_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class New_Pwd(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 81, 31))
        self.label_2.setObjectName("label_2")
        self.newpwd_btn = QtWidgets.QLineEdit(Dialog)
        self.newpwd_btn.setGeometry(QtCore.QRect(150, 50, 151, 20))
        self.newpwd_btn.setObjectName("newpwd_btn")
        self.repeat_btn = QtWidgets.QLineEdit(Dialog)
        self.repeat_btn.setGeometry(QtCore.QRect(150, 110, 151, 20))
        self.repeat_btn.setObjectName("repeat_btn")
        self.newpwd_le = QtWidgets.QPushButton(Dialog)
        self.newpwd_le.setGeometry(QtCore.QRect(50, 190, 75, 23))
        self.newpwd_le.setObjectName("newpwd_le")
        self.resetpwd_le = QtWidgets.QPushButton(Dialog)
        self.resetpwd_le.setGeometry(QtCore.QRect(210, 190, 75, 23))
        self.resetpwd_le.setObjectName("resetpwd_le")

        self.retranslateUi(Dialog)
        self.newpwd_le.clicked.connect(Dialog.newpwd_slot)
        self.resetpwd_le.clicked.connect(Dialog.resetpwd_slot)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "输入新密码："))
        self.label_2.setText(_translate("Dialog", "重复新密码："))
        self.newpwd_le.setText(_translate("Dialog", "确认"))
        self.resetpwd_le.setText(_translate("Dialog", "重置"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
