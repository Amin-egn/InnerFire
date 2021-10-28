# pyqt
from PyQt5.QtCore import QAbstractTableModel, Qt, QPersistentModelIndex


class TableModel(QAbstractTableModel):
    """Table Model"""
    def __init__(self, header, data):
        super().__init__()
        self.header = header
        self._data = data
        self.check = dict()

    def checkState(self, index):
        if index in self.check.keys():
            return self.check[index]
        return Qt.Checked

    def data(self, index, role):
        row = self._data[index.row()]
        if role == Qt.DisplayRole:
            return row[index.column()]
        elif role == Qt.CheckStateRole and index.column() == 0:
            return self.checkState(QPersistentModelIndex(index))
        return None

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self.header)

    def headerData(self, section, orientation , role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]
            if orientation == Qt.Vertical:
                return str(section + 1)

    def setData(self, index, value, role):
        if not index.isValid():
            return False
        if role == Qt.CheckStateRole:
            self.check[QPersistentModelIndex(index)] = value
            return True
        return False

    def flags(self, index):
        flg = QAbstractTableModel.flags(self, index)
        if index.column() == 0:
            flg |= Qt.ItemIsUserCheckable
        return flg