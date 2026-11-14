from PyQt6.QtWidgets import QLineEdit, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QMessageBox

from newPthon.newone.widgetTwo import MyWindow,runSystem

class TodoList(MyWindow):
    def __init__(self):
        super().__init__( "ToDo Task",400,300)
        #widgets
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText("Enter a task....")

        self.addButton = QPushButton("Add",self)
        self.deleteButton = QPushButton("Delete",self)

        self.listWidget = QListWidget(self)

        # Layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.addButton)

        layout = QVBoxLayout()
        layout.addLayout(hbox)
        layout.addWidget(self.listWidget)
        layout.addWidget(self.deleteButton)
        self.setLayout(layout)

        #signals
        self.addButton.clicked.connect(self.add_task)
        self.lineEdit.returnPressed.connect(self.add_task)
        self.deleteButton.clicked.connect(self.delete_task)


    def add_task(self):
        text = self.lineEdit.text().strip()

        if text:
            self.listWidget.addItem(text)
            self.lineEdit.clear()
            self.lineEdit.setFocus()

    def delete_task(self):
        item = self.listWidget.currentRow()

        if item >= 0:
            self.listWidget.takeItem(item)
        else:
            QMessageBox.warning(self,"Error","Please select a task")



runSystem(TodoList)