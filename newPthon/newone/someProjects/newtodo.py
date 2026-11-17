from PyQt6.QtCore import QAbstractTableModel, Qt
from MyMain import MyMain,mymainrun
from todo2 import Ui_MainWindow


class TodoModel(QAbstractTableModel):
    def __init__(self,todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

    def rowCount(self, index):
        return len(self.todos)





class NewTodo(MyMain,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel(todos=[(False,"Python with QT")])
        self.dispList.setModel(self.model)



mymainrun(NewTodo)
