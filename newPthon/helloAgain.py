import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QPushButton
from PyQt6.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.the_button_toggle1 = True
        self.setWindowTitle("Hello Again")
        button = QPushButton("Click me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button)
        # button.clicked.connect(self.the_button_toggle)
        button.setChecked(self.the_button_toggle1)
        self.setFixedSize(400, 300)
        self.setCentralWidget(button)

    def the_button(self):
        print("Hello Again")

    def the_button_toggle(self,checked):
        self.the_button_toggle1 = checked
        print("Hello PyQt6")


app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()
