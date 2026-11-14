import sys

from PyQt6.QtWidgets import QApplication,QPushButton,QMainWindow
class MainWindow(QMainWindow):
    def __init__(self,title="New Title",width=200,height=200):
        super().__init__()

        self.setWindowTitle(title)
        self.setGeometry(width,height,width,height)


def runwindow(run_it):
    app = QApplication(sys.argv)
    window = run_it()
    window.show()
    sys.exit(app.exec()
    )