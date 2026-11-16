from PyQt6.QtWidgets import QMainWindow, QApplication
import sys

class MyMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Main Window")


def mymainrun(dummy):
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    myMain = dummy()
    myMain.show()
    app.exec()