import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class ColorWidget(QWidget):
    def __init__(self, color: str, width: int, height: int, mode: str = "resize",label="Great"):
        super().__init__()

        # Give it a background color
        self.setStyleSheet(f"background-color: {color};")

        # Add a label so you can see which mode is applied
        # layout = QVBoxLayout()
        # layout.addWidget(QLabel(f"{color} ({mode})"))
        # self.setLayout(layout)
        label = QLabel(label, self)
        label.move(10, 10)

        # Apply sizing directly in constructor
        if mode == "resize":
            self.resize(width, height)          # sets current size
        elif mode == "fixed":
            self.setFixedSize(width, height)    # enforces exact size
        elif mode == "minimum":
            self.setMinimumSize(width, height)  # allows bigger but not smaller

app = QApplication(sys.argv)

# Three widgets with different sizing modes
red = ColorWidget("red", 200, 100, "resize")
green = ColorWidget("green", 300, 200, "fixed")
blue = ColorWidget("blue", 400, 300, "minimum")

blue.show()
green.show()
red.show()


sys.exit(app.exec())
