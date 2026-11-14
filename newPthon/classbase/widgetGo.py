from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QLineEdit, QGridLayout, QApplication, QPushButton

from gowithWiget import App,runstart

class WindowApp(App):
    def __init__(self):
        super().__init__(width=200,height=300)
        self.label1 = QLabel()
        self.label1.setText("Enter Your Name")
        self.lineEdit = QLineEdit()
        self.lineEdit.setText("Enter Your Name")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label1,0,0)
        self.layout.addWidget(self.lineEdit,0,1,0,2)
        self.btn = QPushButton("Enter")
        self.btn.clicked.connect(self.run)
        self.lineEdit.returnPressed.connect(self.run)
        self.layout.addWidget(self.btn,1,0)

        self.setLayout(self.layout)

    def run(self):
        text = self.lineEdit.text().strip()

        if text:
            print(f"• {text}")
            self.lineEdit.clear()

if __name__ == "__main__":
    runstart(WindowApp)
