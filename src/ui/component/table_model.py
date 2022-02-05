# pyqt
from PyQt5.QtCore import QAbstractTableModel, Qt


# noinspection PyMethodOverriding
class TableModel(QAbstractTableModel):
    """Table Model"""
    def __init__(self, header, records=None, parent=None):
        super().__init__(parent)
        self.header = header
        self.records = records

    def data(self, index, role):
        row = self.records[index.row()]
        if role == Qt.DisplayRole:
            return row[index.column()]

        return None

    def rowCount(self, index):
        return len(self.records)

    def columnCount(self, index):
        return len(self.header)

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]

            if orientation == Qt.Vertical:
                return str(section + 1)


class DrgDrpTable(TableModel):
    """Drag and Drop Table"""
    def data(self, index, role):
        row = self.records[index.row()]
        if role == Qt.DisplayRole:
            return row
