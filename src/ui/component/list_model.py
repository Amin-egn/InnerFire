# pyqt
from PyQt5.Qt import QAbstractListModel, Qt, QPersistentModelIndex


class ListModel(QAbstractListModel):
    """List Model"""
    def __init__(self, items=None):
        super().__init__()
        self.items = items or list()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.items[index.row()]
        if role == Qt.EditRole:
            return False

    def rowCount(self, index):
        return len(self.items)

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled


class CheckList(ListModel):
    """List with CheckBox"""
    def __init__(self, items=None):
        super().__init__(items)
        self.items = items
        self.checks = dict()

    def checkState(self, index):
        if index in self.checks.keys():
            return self.checks[index]
        else:
            return Qt.Unchecked

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.items[index.row()]

        if role == Qt.CheckStateRole:
            return self.checkState(QPersistentModelIndex(index))

        return None

    def setData(self, index, value, role):
        if not index.isValid():
            return False

        if role == Qt.CheckStateRole:
            self.checks[QPersistentModelIndex(index)] = value
            return True

        return False

    def flags(self, index):
        return Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
