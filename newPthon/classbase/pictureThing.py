import os

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QComboBox, QVBoxLayout

from helloQMainWindow import MyWindow, run_app


class PictureThing(MyWindow):
    def __init__(self):
        super().__init__()

        # Current file directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pics_dir = os.path.join(base_dir, "pics")

        self.label = QLabel()
        self.label.setMinimumSize(400, 300)
        self.label.setScaledContents(True)

        self.comboBox = QComboBox()

        images = [
            ("One", "6.jpg"),
            ("Two", "7.jpg"),
            ("Three", "8.jpg"),
            ("Four", "9.jpg"),
            ("Five", "10.jpg"),

        ]

        for text, filename in images:
            full_path = os.path.join(pics_dir, filename)
            self.comboBox.addItem(text, full_path)

        self.comboBox.currentIndexChanged.connect(self.change_picture)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.comboBox)

        self.central.setLayout(layout)

        # Load first image immediately
        self.change_picture(0)

    def change_picture(self, index):
        path = self.comboBox.itemData(index)

        print("Loading:", path)
        print("Exists:", os.path.exists(path))

        pixmap = QPixmap(path)

        if pixmap.isNull():
            print("Image not found!")
            return

        self.label.setPixmap(pixmap)


if __name__ == "__main__":
    run_app(PictureThing)