from PyQt6.QtGui import QFont, QColor

from TestMain import MainWindow
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt, QVariantAnimation
from TestMain import  MainWindow,runwindow
import random




class LabelOnly(MainWindow):
    def __init__(self):
        super().__init__()
        self.random_color()
        self.label = QLabel("Hello World")
        self.label.setFont(QFont("Times", 20))
        self.label.setStyleSheet(f"background-color: rgb({self.r}, {self.g}, {self.b}); color: rgb({self.br}, {self.bg}, {self.bb});")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        self.animation = QVariantAnimation()
        self.animation.setStartValue(QColor("red"))
        self.animation.setEndValue(QColor("blue"))
        self.animation.setDuration(2000)

        self.animation.valueChanged.connect(self.change_color)

        self.animation.setLoopCount(-1)  # infinite
        self.animation.start()

    def change_color(self, color):
        self.label.setStyleSheet(
            f"background-color: {color.name()}; color: white;"
        )

    def random_color(self):
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

        self.br = random.randint(0, 255)
        self.bg = random.randint(0, 255)
        self.bb = random.randint(0, 255)


runwindow(LabelOnly)

