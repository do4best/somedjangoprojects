# base_window.py
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class BaseWindow(QMainWindow):
    def __init__(self, title="My App", width=600, height=400):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, width, height)

        # Central widget only — no layout here
        self.central = QWidget()
        self.setCentralWidget(self.central)

def run_app(window_class):
    app = QApplication(sys.argv)
    window = window_class()
    window.show()
    sys.exit(app.exec())
