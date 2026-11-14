import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton


class WindowWidget(QWidget):
    def __init__(self,title="QWidget",width=500,height=500):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(width,height,width,height)


def widget_class(widget_window):
    app = QApplication(sys.argv)
    window = widget_window()
    window.show()
    sys.exit(app.exec())


class CreateWindow(WindowWidget):
    def __init__(self):
        super().__init__("CreateWindow")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.label = QLabel("Hello World")
        self.layout.addWidget(self.label)
        self.button = QPushButton("Click Me")
        self.layout.addWidget(self.button)



if __name__ == "__main__":
    widget_class(CreateWindow)
    widget_class(CreateWindow)