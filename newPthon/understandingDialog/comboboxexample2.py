from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QInputDialog
from myMainQ import MyMain,myMainrun

class comboboxexample(MyMain):
    def __init__(self):
        super().__init__()

        self.widget = QWidget()
        self.vlayout = QVBoxLayout()

        for text in ["Integer", "Float", "Double", "String"]:
            self.createButtons(text)
        self.widget.setLayout(self.vlayout)

        self.setCentralWidget(self.widget)

    def createButtons(self,title):

        self.button1 = QPushButton(title)
        if title == "Integer":
            self.button1.setStyleSheet("background-color: red; color: white;")
        elif title == "Float":
            self.button1.setStyleSheet("background-color: blue; color: white;")
        elif title == "Double":
            self.button1.setStyleSheet("background-color: white; color: red;")
        elif title == "String":
            self.button1.setStyleSheet("background-color: black; color: blue;")
        self.button1.clicked.connect(self.get_an_value)
        self.vlayout.addWidget(self.button1)

    def get_an_value(self):

        my_int_value,ok = QInputDialog.getInt(self,"Get an Integer","Enter an integer")
        print("Result : ",ok,my_int_value)


myMainrun(comboboxexample)

