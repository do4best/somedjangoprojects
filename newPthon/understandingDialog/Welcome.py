from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPalette,QColor
from PyQt6.QtCore import Qt
import sys
import MyUI
from MyUI import Ui_Form

class Welcome(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        f = self.label.font()
        f.setPointSize(12)
        self.label.setFont(f)

        self.pushButton.clicked.connect(self.buttonClicked)
        self.show()
        print("MyUI being loaded from:", MyUI.__file__)


    def buttonClicked(self):
        self.label.setText("Welcome")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window,QColor(0,128,255))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    app.setPalette(palette)
    form = Welcome()
    sys.exit(app.exec())
