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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "邮件管理系统测试版"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
