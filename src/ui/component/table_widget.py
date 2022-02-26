# standard
from functools import partial
# internal
from .list_widget import DropList
from .combobox import ComboBox
# pyqt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView


class TableWidget(QTableWidget):
    """Table Widget"""
    def __init__(self, headers, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers = headers
        self._craftTable()

    def _craftTable(self):
        self.setColumnCount(len(self.headers))
        self.setHorizontalHeaderLabels(self.headers)
        self.setAlternatingRowColors(True)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setDefaultSectionSize(30)

    def setRowRecords(self, records):
        self.recLen = len(records)
        self.setRowCount(self.recLen)
        for i, rec in enumerate(records):
            self.setItem(int(i), 0, QTableWidgetItem(rec))
            self.setCellWidget(i, 1, ComboBox(['Droppable', 'Null', 'Auto Increment'], self))
            self.setCellWidget(i, 2, DropList())

    def getListRecords(self, col=2):
        for i in range(self.recLen):
            self.cellWidget(i, col).getMembers()

    def changeIndex(self, index):
        if index == 1 or index == 2:
            pass
