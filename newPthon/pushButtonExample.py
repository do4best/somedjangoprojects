from PyQt6.QtWidgets import QPushButton, QDialog,QApplication,QDialogButtonBox,QLabel,QVBoxLayout


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HELLO!")
        buttons = (
                QDialogButtonBox.StandardButton.Ok
              | QDialogButtonBox.StandardButton.Cancel
                    )
        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.show()

if __name__ == "__main__":
    app = QApplication([])
    dialog = CustomDialog()
    app.exec()
