import sys
from PyQt5.Qt import *
from resouce.pane_ui import Ui_Form


#主窗口页面
class MailPane(QWidget,Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)



if __name__ == "__main__":

    app = QApplication(sys.argv)

    myui = MailPane()
    myui.show()
    sys.exit(app.exec_())