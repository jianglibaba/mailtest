from PyQt5.Qt import *
#导入主窗口文件
from pane import *
#导入修改密码窗口文件
from newpwd import *
#导入数据库处理文件
from mydata import *


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    mail = MailPane()
    my_newpwd =Ui_Dialog()

    def show_newpwd(id):
        global newid
        newid = id
        my_newpwd.exec_()

    def change_pwd(text):
        a = newid
        b = text
        Tools.changepwd(a,b)
        mail.flushTable()

    mail.newpwd_signal.connect(show_newpwd)

    my_newpwd.newpwd_signal.connect(change_pwd)

    mail.show()

    sys.exit(app.exec_())

