from PyQt6.QtWidgets import QMainWindow, QApplication
import sys
from PyQt6.QtCore import QAbstractTableModel, Qt

class MyMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Main Window")



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



def mymainrun(dummy):
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    myMain = dummy()
    myMain.show()
    app.exec()