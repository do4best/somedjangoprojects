from PyQt6.QtWidgets import QPushButton, QFileDialog

from myMainQ import MyMain,myMainrun
class NewFile(MyMain):
    def __init__(self):
        MyMain.__init__(self)
        button =QPushButton("Click me")
        button.clicked.connect(self.get_an_value)
        self.setCentralWidget(button)

    def get_an_value(self):
        FILE_FILTERS = [
            "Portable Network Graphics files (*.png)",
            "Text files (*.txt)",
            "Comma Separated Values (*.csv)",
            "All files (*.*)",
        ]

        filter_string = ";;".join(FILE_FILTERS)
        filename,selected_filter = QFileDialog.getOpenFileName(self,"Open File","",filter_string)
        print(filename,selected_filter)

myMainrun(NewFile)