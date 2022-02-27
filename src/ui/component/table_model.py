# pyqt
from PyQt5.QtCore import QAbstractTableModel, Qt


# noinspection PyMethodOverriding,PyUnresolvedReferences
class TableModel(QAbstractTableModel):
    """Table Model"""
    def __init__(self, header, records=None, parent=None):
        super().__init__(parent)
        self.header = header
        self.records = records or list()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.records[index.row()][index.column()]

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

    def setRecords(self, records):
        self.beginResetModel()
        self.records = records
        self.endResetModel()
        self.layoutChanged.emit()

    def clearRecords(self):
        self.setRecords([])


class SingleDimensionTableModel(TableModel):
    """Drag and Drop Table"""
    def data(self, index, role):
        row = self.records[index.row()]
        if role == Qt.DisplayRole:
            return row

    def isEmpty(self, index=0):
        if self.rowCount(index) == 0:
            return True
        return False
