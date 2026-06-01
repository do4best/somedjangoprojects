from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QVBoxLayout, QApplication, QWidget, QPushButton, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QEdit Example")
        self.setFixedSize(200, 100)
        window1 = QWidget()
        layout = QGridLayout()
        username = QLineEdit()
        username.setPlaceholderText("Enter your username")
        layout.addWidget(username, 0, 1,1,2)
        layout.addWidget(QLabel("Username:"), 0, 0,1,2)
        layout.addWidget(QLineEdit(), 1, 1,1,2)
        layout.addWidget(QLabel("Password:"), 1, 0,1,2)
        layout.addWidget(QPushButton("Push it"), 2, 1,1,2)
        window1.setLayout(layout)
        self.setCentralWidget(window1)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()