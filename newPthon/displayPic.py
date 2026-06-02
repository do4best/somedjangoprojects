import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QGridLayout, QCheckBox, QComboBox, QListWidget, \
    QLineEdit, QSpinBox, QSlider, QDial


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Display Picture")

        central_widget = QWidget(self)
        check = QCheckBox("Check me")
        check.setChecked(True)
        check.stateChanged.connect(lambda state: print("Check state:", state))
        ## Combo Box
        comboBox = QComboBox(self)
        comboBox.addItems(["Item 1", "Item 2", "Item 3"])
        comboBox.currentIndexChanged.connect(lambda index: print("Selected index:", index))
        ## QList Widget
        listWidget = QListWidget(self)
        listWidget.addItems(["Item 1", "Item 2", "Item 3"])
        listWidget.currentRowChanged.connect(lambda currentRow: print("Current row:", currentRow))
        ## QLineEdit Example
        lineEdit = QLineEdit(self)
        lineEdit.setMaxLength(20)
        lineEdit.setPlaceholderText("Enter your name")
        lineEdit.textChanged.connect(lambda text: print("Text changed:", text))
        lineEdit.returnPressed.connect(lambda: print("Enter key pressed"))
        lineEdit.textEdited.connect(lambda text: print("Text edited:", text))

        ## QSpin Box Example
        spinBox = QSpinBox(self)
        spinBox.setRange(1, 100)
        spinBox.setMinimum(-10)
        spinBox.setMinimum(3)
        spinBox.setPrefix("$")
        spinBox.setSuffix("c")
        spinBox.valueChanged.connect(lambda value: print("Value changed:", value))
        spinBox.textChanged.connect(lambda text: print("Text changed:", text))
        ## QSlider Example
        slider = QSlider()
        slider.setMinimum(-10)
        slider.setMaximum(3)
        slider.setSingleStep(3)
        slider.setOrientation(Qt.Orientation.Horizontal)
        slider.valueChanged.connect(lambda value: print("Slider value:", value))
        slider.sliderMoved.connect(lambda value: print("Slider moved:", value))
        slider.sliderReleased.connect(lambda: print("Slider released"))
        slider.sliderPressed.connect(lambda: print("Slider pressed"))
        ## QDial
        dial = QDial()
        dial.setRange(0, 360)
        dial.setNotchesVisible(True)
        dial.setSingleStep(10)
        dial.valueChanged.connect(lambda value: print("Dial value:", value))


        layout = QGridLayout()
        image_files=[
            "mylady.jpg",
            "1.jpg",
            "2.png",
        ]
        for index, image_file in enumerate(image_files):
            label = QLabel(self)
            pixmap = QPixmap(image_file)
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            label.setFixedSize(300, 400)
            layout.addWidget(label, index // 3, index % 3)

        layout.addWidget(check, 3, 0, 1, 3)
        layout.addWidget(comboBox, 4, 0, 1, 3)
        layout.addWidget(listWidget, 5, 0, 1, 3)
        layout.addWidget(lineEdit, 6, 0, 1, 2)
        layout.setSpacing(10)
        layout.addWidget(QLabel("Hello"), 6, 2, 1, 3)
        layout.addWidget(spinBox, 7, 0, 1, 3)
        layout.addWidget(slider, 8, 0, 1, 3)
        layout.addWidget(dial, 9, 0, 1, 3)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())