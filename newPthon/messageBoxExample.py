from PyQt6.QtWidgets import QPushButton, QDialog, QApplication, QDialogButtonBox, QLabel, QVBoxLayout, QMessageBox


class CustomDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HELLO!")

        self.show()

if __name__ == "__main__":
    app = QApplication([])
    dialog = CustomDialog()
    app.exec()