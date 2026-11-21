from pathlib import Path
from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PyQt6.QtGui import QImage

from MyMain import MyMain,mymainrun
from todo import Ui_MainWindow
import json


base_dir = Path(__file__).parent
tick = QImage(str(base_dir/'check.png'))
json_file = base_dir/'todos.json'


class TodoModel(QAbstractTableModel):
    def __init__(self,*args,todos=None,**kwargs):
        super().__init__(*args,**kwargs)
        self.todos = todos or []
        self.loadtodos()

    def savetodos(self):
        with open('todos.json','w') as f:
            json.dump(self.todos,f,indent=4)

    def loadtodos(self):
        try:
            with open('todos.json','r') as f:
                data = json.load(f)


            self.todos = [tuple(item) for item in data]

        except FileNotFoundError:
            self.todos = []


    def data(self,index, role=Qt.ItemDataRole.DisplayRole):



        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todos[index.row()]
            return text

        if role == Qt.ItemDataRole.DecorationRole:
            status, text = self.todos[index.row()]
            if status:
                return tick

        return  None

    def rowCount(self, parent=QModelIndex()):
        return len(self.todos)

    def columnCount(self, parent=QModelIndex()):
        return 1





class NewTodo(MyMain,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.todolistView.setModel(self.model)
        self.AddBtn.clicked.connect(self.addTodo)
        self.DeleteBtn.clicked.connect(self.delTodo)
        self.CompleteBtn.clicked.connect(self.complete)

    def addTodo(self):
        text = self.addtodoEdit.text().strip()
        if text:
            row = len(self.model.todos)
            self.model.beginInsertRows(QModelIndex(), row, row)
            self.model.todos.append((False,text))
            self.model.endInsertRows()
            self.model.savetodos()
            self.model.layoutChanged.emit()

            self.addtodoEdit.clear()

    def delTodo(self):
        indexes = self.todolistView.selectionModel().selectedIndexes()
        if indexes:
            row = indexes[0].row()

            self.model.beginRemoveRows(QModelIndex(), row,row)
            del self.model.todos[row]
            self.model.endRemoveRows()
            self.model.savetodos()
            self.model.layoutChanged.emit()

            self.todolistView.clearSelection()

    def complete(self):
        indexes = self.todolistView.selectionModel().selectedIndexes()
        if indexes:
            index = indexes[0]
            row  = index.row()
            status,text = self.model.todos[row]
            self.model.todos[row] = (True,text)
            self.model.savetodos()
            print(self.model.todos)
            self.model.dataChanged.emit(index,index)
            self.todolistView.clearSelection()





mymainrun(NewTodo)
