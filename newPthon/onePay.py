# my_window.py
from base_window import BaseWindow, run_app
from PyQt6.QtWidgets import QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel
from PyQt6.QtCore import Qt

class MyWindow(BaseWindow):
    def __init__(self):
        super().__init__("Nice",200,100)

        # Attach layout once
        # self.layout = QHBoxLayout()
        # self.central.setLayout(self.layout)
        #
        # # Add widgets
        # self.line_edit = QLineEdit("Type here...")
        # self.button = QPushButton("Submit")
        #
        # self.layout.addWidget(self.line_edit)
        # self.layout.addWidget(self.button)
        self.layout = QGridLayout()
        self.central.setLayout(self.layout)
        self.setLayout(self.layout)
        self.label = QLabel("Enter Name")
        self.layout.addWidget(self.label,0,0)
        self.lineEdit = QLineEdit()

        self.button = QPushButton("Submit")
        self.button.clicked.connect(self.submit)
        self.layout.addWidget(self.button, 1, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignCenter)
        self.label1 = QLabel("?")
        self.layout.addWidget(self.label1,1,1,3,3,alignment=Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.textChanged.connect(self.label1.setText)
        self.layout.addWidget(self.lineEdit, 0, 1)





    def submit(self):
        self.button.setText("Submit")
        self.setWindowTitle("Submit")
        self.lineEdit.clear()
if __name__ == "__main__":
    run_app(MyWindow)
    run_app(MyWindow)
