import sys

from PyQt6.QtWidgets import QMainWindow, QApplication


class MyMain(QMainWindow):
    def __init__(self,title="Qmain",width=500,height=500):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(width,height)


def myMainrun(rat):
    app = QApplication(sys.argv)
    myMain = rat()
    myMain.show()
    sys.exit(app.exec())