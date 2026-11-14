from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout
import sys

def display(text):
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(200, 100)
    layout = QVBoxLayout()
    label = QLabel(text)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setFixedHeight(50)
    label.setFixedWidth(200)
    label.setStyleSheet("background-color: yellow; color: red;")

    layout.addWidget(label)
    window.setLayout(layout)
    window.setWindowTitle("Calculator")
    window.show()
    app.exec()


if __name__ == "__main__":

    display("Hello World")
