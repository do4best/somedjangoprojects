from random import choice

from PyQt6.QtWidgets import QMainWindow, QApplication,QPushButton

window_titles = [
"My App",
"My App",
"Still My App",
"Still My App",
"What on earth",
"What on earth",
"This is surprising",
"This is surprising",
"Something went wrong",
]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("Hello World")
        self.button = QPushButton("Click me", self)
        self.setCentralWidget(self.button)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.resize(400, 300)
        self.show()

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        new_window_title = choice(window_titles)
        self.setWindowTitle(new_window_title)
        print(self.button_is_checked)

    def the_window_title_changed(self,window_title):
        if window_title == "Something went wrong":
            self.button.setDisabled(True)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()

