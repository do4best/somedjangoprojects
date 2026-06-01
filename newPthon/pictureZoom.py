import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QSlider, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zoom Picture")

        self.pixmap = QPixmap("mylady.jpg")
        self.pixmap = self.pixmap.scaled(800,800)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(10)
        self.slider.setMaximum(300)
        self.slider.setValue(100)
        self.slider.valueChanged.connect(self.zoom_picture)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)

        central_widget = QWidget()
        central_widget.setFixedSize(300, 300)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.zoom_picture(100)

        self.show()

    def zoom_picture(self, value):
        width = int(self.pixmap.width() * value / 100)
        height = int(self.pixmap.height() * value / 100)

        scaled_pixmap = self.pixmap.scaled(
            width,
            height,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.label.setPixmap(scaled_pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())