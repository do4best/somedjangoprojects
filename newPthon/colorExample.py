from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout
import random


class Color(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(self.backgroundRole().Window,QColor(color))
        self.setPalette(palette)


class ColorExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Example")
        self.setGeometry(100,100,300,300)
        colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink"]
        widget = Color(random.choice(colors))
        mywidget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(Color(colors[0]))
        layout.addWidget(Color(colors[1]))
        layout.addWidget(Color(colors[2]))
        layout.addWidget(Color(colors[3]))
        layout.addWidget(Color(colors[4]))
        mywidget.setLayout(layout)
        self.setCentralWidget(mywidget)

if __name__ == "__main__":
    app = QApplication([])
    window = ColorExample()
    window.show()
    app.exec()