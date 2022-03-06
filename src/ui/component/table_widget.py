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
        record_dict = dict()
        for i in range(self.recLen):
            record_dict[self.item(i, 0).text()] = self.cellWidget(i, col).getMembers()

        return record_dict

    def comboIndexChanged(self, index):
        selected_row_list = self.cellWidget(self.currentRow(), 2)
        selected_row_list.clear()
        if index == 0:
            trufal = False
        else:
            trufal = True
            if index == 1:
                item = '_Null'
            else:
                item = '_AutoIncrement'

            selected_row_list.addItem(item)

        selected_row_list.setDisabled(trufal)


class  PresentationTableWidget(QTableWidget):
    """Presentation Table Widget"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._craftTable()

    def _craftTable(self):
        self.setAlternatingRowColors(True)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setAutoScroll(True)
        self.horizontalHeader().setMinimumWidth(60)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setDefaultSectionSize(30)

    def setTitles(self, titles):
        self.setColumnCount(len(titles))
        self.setHorizontalHeaderLabels(titles)

    def setRowRecords(self, records):
        self._getRowCount(records)
        for index, elem in enumerate(records):
            for i, e in enumerate(elem):
                self.setItem(int(i), index, QTableWidgetItem(e))

    def _getRowCount(self, nestlist):
        holder = list()
        for i in nestlist:
            holder.append(len(i))
        self.setRowCount(max(holder))
