from PyQt6.QtWidgets import QWidget, QApplication
import sys

class myQWidget(QWidget):
    def __init__(self,parent=None,title="QWidget",width=300,height=300):
        QWidget.__init__(self,parent)
        self.setWindowTitle(title)
        self.setFixedSize(width,height)




def runQWidget(myWidget ):
    app = QApplication(sys.argv)
    window = myWidget()
    window.show()