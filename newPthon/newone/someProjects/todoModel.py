from PyQt6.QtCore import QAbstractTableModel, Qt


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