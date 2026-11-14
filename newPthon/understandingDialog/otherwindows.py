from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QAction
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QMainWindow, QLineEdit, QWidget, QHBoxLayout, QMenu

from myQWidget import myQWidget,runQWidget
from myMainQ import MyMain,myMainrun
class myWidget(myQWidget):
    def __init__(self):
        super(myWidget,self).__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Hello")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class myMainWindow(MyMain):
    def __init__(self):
        super(myMainWindow,self).__init__()
        self.w = myWidget()
        self.quitButton = QPushButton("Quit")
        self.quitButton.clicked.connect(self.showWidget)


        self.lineEdit = QLineEdit()
        self.lineEdit.textChanged.connect(self.w.label.setText)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.quitButton)
        self.layout.addWidget(self.lineEdit)
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

    def showWidget(self,checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()



class MyMouse(MyMain):
    def __init__(self):
        super(MyMouse,self).__init__()
        # self.label = QLabel("Hello")
        # self.label.setFont(QFont("Times",20))
        # self.colors = ["red", "green", "blue", "yellow", "purple"]
        # self.index = 0
        #
        # self.label.setStyleSheet(f"background-color: {self.colors[self.index]}")
        # self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.setCentralWidget(self.label)

    # def mouseMoveEvent(self,event):
    #     self.index = (self.index + 1) % len(self.colors)
    #
    #     self.label.setStyleSheet(
    #         f"background-color: {self.colors[self.index]};"
    #     )
    #     self.label.setText("Mouse moved")
    #
    # def mouseReleaseEvent(self,event):
    #     self.index = (self.index + 1) % len(self.colors)
    #
    #     self.label.setStyleSheet(
    #         f"background-color: {self.colors[self.index]};"
    #     )
    #     self.label.setText("Mouse released")
    #
    # def mousePressEvent(self,event):
    #     self.index = (self.index + 1) % len(self.colors)
    #
    #     self.label.setStyleSheet(
    #         f"background-color: {self.colors[self.index]};"
    #     )
    #     self.label.setText("Mouse pressed")
    #
    # def mouseDoubleClickEvent(self,event):
    #     self.index = (self.index + 1) % len(self.colors)
    #
    #     self.label.setStyleSheet(
    #         f"background-color: {self.colors[self.index]};"
    #     )
    #     self.label.setText("Mouse double clicked")

    def contextMenuEvent(self,event):
        contextMenu = QMenu(self)
        contextMenu.addAction(QAction("Click me",self))
        contextMenu.addAction(QAction("Click me", self))
        contextMenu.addAction(QAction("Click me", self))
        contextMenu.exec(event.globalPos())




myMainrun(MyMouse)
