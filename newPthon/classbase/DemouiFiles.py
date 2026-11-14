import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from mytodolist import Ui_Form

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.add_task)
        self.ui.lineEdit.returnPressed.connect(self.add_task)
        self.ui.pushButton_2.clicked.connect(self.delete_task)

    def add_task(self):
        text = self.ui.lineEdit.text().strip()

        if text:
            number = self.ui.listWidget.count() + 1
            self.ui.listWidget.addItem(f"{number}.  {text}")
            self.ui.lineEdit.clear()

    def delete_task(self):
        row = self.ui.listWidget.currentRow()

        if row >= 0:
            self.ui.listWidget.takeItem(row)
        else:
            QMessageBox.warning(
                self,
                "Warning",
                "Please select a task first!"
            )

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())