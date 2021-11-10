# pyqt
from PyQt5.QtCore import QAbstractTableModel, Qt, QPersistentModelIndex


class TableModel(QAbstractTableModel):
    """Table Model"""
    def __init__(self, header, data):
        super().__init__()
        self.header = header
        self._data = data

    def data(self, index, role):
        row = self._data[index.row()]
        if role == Qt.DisplayRole:
            return row[index.column()]

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

class DrgDrpTable(TableModel):
    """Drag and Drop Table"""
    def data(self, index, role):
        row = self._data[index.row()]
        if role == Qt.DisplayRole:
            return row