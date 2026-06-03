from PyQt6.QtWidgets import QMainWindow, QGridLayout, QApplication, QWidget, QStackedLayout, QVBoxLayout, QHBoxLayout, \
    QPushButton
import random
from colorExample import Color
class ColorExample1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello PyQt6")
        # layout = QStackedLayout()
        # layout.addWidget(Color("red"))
        # layout.addWidget(Color("green"))
        # layout.addWidget(Color("blue"))
        # layout.addWidget(Color("yellow"))
        # layout.setCurrentIndex(3)
        # widget =QWidget()
        # widget.setLayout(layout)
        # widget.setFixedSize(300,300)
        # self.setCentralWidget(widget)
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.stack = QStackedLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(self.stack)

        btn1 = QPushButton("red")
        btn1.pressed.connect(lambda: self.stack.setCurrentIndex(0))
        hbox.addWidget(btn1)
        self.stack.addWidget(Color("red"))
        btn1 = QPushButton("blue")
        btn1.pressed.connect(lambda: self.stack.setCurrentIndex(1))
        hbox.addWidget(btn1)
        self.stack.addWidget(Color("blue"))
        btn1 = QPushButton("orange")
        btn1.pressed.connect(lambda: self.stack.setCurrentIndex(2))
        hbox.addWidget(btn1)
        self.stack.addWidget(Color("orange"))
        colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink"]
        widget1 = Color(random.choice(colors))
        btn1 = QPushButton("Random")
        btn1.pressed.connect(lambda: self.stack.setCurrentIndex(3))
        hbox.addWidget(btn1)
        self.stack.addWidget(widget1)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication([])
    window = ColorExample1()
    window.show()
    app.exec()
