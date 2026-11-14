from PyQt6.QtWidgets import QDialog, QLabel, QComboBox, QMessageBox, QApplication, QWidget
import sys

def show_message(s):
    dlg = QDialog(s)
    dlg.setWindowTitle("?")
    dlg.show()
    sys.exit(dlg.exec())


# app = QApplication(sys.argv)
# window = show_message()
# window.show()
# sys.exit(app.exec())

from PyQt6.QtWidgets import QMessageBox

def show_message1(self):
    QMessageBox.information(
        self, "?",
        "Message",
    )


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()

    def show_message1(self, s):
        QMessageBox.information(
            self,
            "?",
            s
        )


def thismessage(s):
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show_message1(s)


