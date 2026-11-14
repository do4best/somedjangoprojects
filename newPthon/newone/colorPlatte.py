import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout


class Color(QWidget):
    def __init__(self, color="red",parent=None):
        super(Color, self).__init__(parent)
        self.setAutoFillBackground(True)
        platte = QPalette()
        platte.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(platte)

class ColorWidget(QMainWindow):
    def __init__(self, color=None, parent=None):
        super(ColorWidget, self).__init__(parent)
        self.setWindowTitle("Color")
        widget1 = QWidget()

        layout = QVBoxLayout()
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("red"))
        layout.addWidget(Color("yellow"))
        widget1.setLayout(layout)
        widget = Color()
        self.setCentralWidget(widget1)

if __name__ == "__main__":
    main = QApplication([])
    widget = ColorWidget()
    widget.show()
    sys.exit(main.exec())
