import sys

from PyQt6.QtWidgets import QApplication, QWidget

class App(QWidget):
    def __init__(self,title="QWidget",width=500,height=500):
        super().__init__()

        self.setWindowTitle(title)
        self.setGeometry(width,height,width,height)

def runstart(run_it):
    app = QApplication([])
    window = run_it()
    window.show()
    sys.exit(app.exec())
