# pyqt
from PyQt5.Qt import QAbstractListModel, Qt


class ListModel(QAbstractListModel):
    """List Model"""
    def __init__(self, titles=None):
        super().__init__()
        self.titles = titles or list()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.titles[index.row()]

    def rowCount(self, index):
        return len(self.titles)


class CheckList(ListModel):
    """List with CheckBox"""
    def __init__(self, titles=None):
        super().__init__(titles)
        self.titles = titles

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.titles[index.row()]
        elif role == Qt.CheckStateRole:
            pass

    def setData(self, index, value, role):
        pass

    def flags(self, index):
        flg = QAbstractListModel.flags(self.index)
        if index.row():
            flg |= Qt.ItemIsUserCheckable
        return flg
