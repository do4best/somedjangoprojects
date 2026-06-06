from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QToolBar


class ToolbarAndMenues(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toolbar and Menues")
        label = QLabel("Hello PyQt6")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
        toolbar = QToolBar("Main Toolbar")

        self.addToolBar(toolbar)

        button_action = QAction("My Button", self)
        button_action.triggered.connect(self.onMyButtonClicked)
        toolbar.addAction(button_action)


        self.show()

    def onMyButtonClicked(self,s):
        print("My Button Clicked",s)



if __name__ == "__main__":
    app = QApplication([])
    window = ToolbarAndMenues()
    app.exec()