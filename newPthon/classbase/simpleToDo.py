from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QListWidget,
    QMessageBox
)

import sys


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Todo App")
        self.resize(400, 300)

        # Widgets
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Enter a task...")

        self.addBtn = QPushButton("Add")
        self.deleteBtn = QPushButton("Delete Selected")

        self.listWidget = QListWidget()

        # Layouts
        hbox = QHBoxLayout()
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.addBtn)

        layout = QVBoxLayout()
        layout.addLayout(hbox)
        layout.addWidget(self.listWidget)
        layout.addWidget(self.deleteBtn)

        self.setLayout(layout)

        # Signals
        self.addBtn.clicked.connect(self.add_task)
        self.lineEdit.returnPressed.connect(self.add_task)
        self.deleteBtn.clicked.connect(self.delete_task)

    def add_task(self):
        text = self.lineEdit.text().strip()

        if text:
            self.listWidget.addItem(text)
            self.lineEdit.clear()
            self.lineEdit.setFocus()

    def delete_task(self):
        item = self.listWidget.currentRow()

        if item >= 0:
            self.listWidget.takeItem(item)
        else:
            QMessageBox.warning(
                self,
                "Warning",
                "Please select a task first!"
            )


app = QApplication(sys.argv)

window = TodoApp()
window.show()

sys.exit(app.exec())