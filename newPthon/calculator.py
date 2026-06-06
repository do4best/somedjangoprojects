import sys
from PyQt6 import QtWidgets,QtCore,QtGui
from calk import Ui_Form
class MainWindow(QtWidgets.QWidget):
    ERROR_MESSAGE="Invalid input"
    MAX_FONT_SIZE=100
    MIN_FONT_SIZE=30
FONT_SIZE_THRESHOLD=[item for item in enumerate(range(90,30,-5),9)]
    def __init__(self):
        super().__init__()
        self._dragPos=None
        self.new_input_flag=False
        self.prev_text=""
        self.current_text=""
        self.show_text=""
        self.operator=""
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.output = self.ui.lineEdit
        self.close_btn=self.ui.close_button
        self.clear_btn=self.ui.pushButton_2
        self.plus_minus_btn=self.ui.pushButton_4
        self.percent_btn=self.ui.pushButton_4
        self.clear_btn.clicked.connect(self.clear_output)
        self.plus_minus_btn.clicked.connect(self.change_sign)
        self.percent_btn.clicked.connect(self.percent)
        self.ui.button_frame.setEnabled(False)
        self.ui.button_frame.setStyleSheet("")
        self.ui.button_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ui.button_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ui.button_frame.setObjectName("button_frame")
        self.ui.button_frame.setGeometry(QtCore.QRect(20, 20, 351, 351))

