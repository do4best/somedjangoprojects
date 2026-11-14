from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from widgetTwo import MyWindow,runSystem


class Window_one(MyWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.label = QLabel("Hello World")
        self.button = QPushButton("Click me")
        self.button.clicked.connect(lambda :print("Click me"))
        self.layout.addWidget(self.button)

        self.layout.addWidget(self.label)


if __name__ == '__main__':
    runSystem(Window_one)