# pyqt
from PyQt5.Qt import QAbstractListModel, Qt


class ListModel(QAbstractListModel):
    """List Model"""
    def __init__(self, items=None):
        super().__init__()
        self.items = items or list()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.items[index.row()]

    def rowCount(self, index):
        return len(self.items)

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled


class CheckList(ListModel):
    """List with CheckBox"""
    def __init__(self, items=None):
        super().__init__(items)
        self.items = items
        self.checkList = list()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.items[index.row()]

        if role == Qt.CheckStateRole:
            if index.row() not in self.checkList:
                return Qt.Unchecked
            return Qt.Checked

    def setData(self, index, value, role):
        if not index.isValid() or role != Qt.CheckStateRole:
            return False

        if value == Qt.Checked:
            self.checkList.append(index.row())
        else:
            self.checkList.remove(index.row())

        self.dataChanged.emit(index, index)
        return True

    def flags(self, index):
        return Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
