from PyQt6.QtCore import QAbstractTableModel, Qt
from MyMain import MyMain,mymainrun
from todo1 import Ui_Form


class TodoModel(QAbstractTableModel):
    def __init__(self,todo=None):
        super().__init__()
        self.todos = todo or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

    def rowCount(self, index):
        return len(self.todos)





class NewTodo(MyMain,Ui_Form):
    def __init__(self):
        MyMain.__init__(self)
        self.setupUi(self)
        self.model = TodoModel()
        self.todoView.setModel(self.model)



mymainrun(NewTodo)
