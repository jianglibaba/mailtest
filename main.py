import sys
from PyQt5.Qt import *
from pane import *
from newpwd import *
from mydata import *


if __name__ == "__main__":

    app = QApplication(sys.argv)

    mail = MailPane()
    my_newpwd =Ui_Dialog()

    def show_newpwd(id):
        global newid
        newid = id
        my_newpwd.exec_()

    def change_pwd(text):
        a =text
        b = newid
        print(a)
        print(b)
        Tools.changepwd(b,a)
        mail.flushTable()







    mail.newpwd_signal.connect(show_newpwd)

    my_newpwd.newpwd_signal.connect(change_pwd)


    mail.show()
    sys.exit(app.exec_())

