import sys
from PyQt5.Qt import *

from resouce.changepwd_ui import *


#注册页面
class Ui_Dialog(QDialog,Ui_Dialog):
    newpwd_signal = pyqtSignal(str)

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)



    def newpwd_slot(self):
        newpwd_text = self.newpwd_btn.text()
        self.newpwd_signal.emit(newpwd_text)
        self.close()


    def resetpwd_slot(self):
        self.newpwd_btn.clear()
        self.repeat_btn.clear()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())