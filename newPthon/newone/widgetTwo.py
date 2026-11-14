from PyQt6.QtWidgets import QApplication, QWidget

import sys


class MyWindow(QWidget):
    def __init__(self,title="New Title",width=200,height=200):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(width,height,width,height)

def runSystem(class_window):
    app = QApplication(sys.argv)
    window = class_window()
    window.show()
    sys.exit(app.exec())
