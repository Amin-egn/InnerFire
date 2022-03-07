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
        self.recordsDict = records
        self._getRowCount(list(self.recordsDict.values()))
        row = 0
        for key, val in self.recordsDict.items():
            for elem in val:
                self.setItem(row, 0, QTableWidgetItem(f'{key}-{elem}'))
                self.setCellWidget(row, 1, ComboBox(['Droppable', 'Null', 'Auto Increment'], self))
                self.setCellWidget(row, 2, DropList())
                row += 1

    def _getRowCount(self, nestlist):
        holder = list()
        for i in nestlist:
            holder.append(len(i))

        self.rowLen = sum(holder)
        self.setRowCount(self.rowLen)

    def getListRecords(self, col=2):
        record_dict = {}
        for i in range(self.rowLen):
            first_column = self.item(i, 0).text().split('-')
            dict_key = first_column[0]
            if dict_key not in record_dict.keys():
                record_dict[dict_key] = {}

            record_dict[dict_key][first_column[1]] = self.cellWidget(i, col).getMembers()

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


class PresentationTableWidget(QTableWidget):
    """Presentation Table Widget"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._craftTable()

    def _craftTable(self):
        self.setAlternatingRowColors(True)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.horizontalHeader().setMinimumWidth(60)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setDefaultSectionSize(30)

    def setTitles(self, titles):
        self.setColumnCount(len(titles))
        self.setHorizontalHeaderLabels(titles)

    def setRowRecords(self, records):
        self._getRowCount(records)
        self.clearContents()
        for index, elem in enumerate(records):
            for i, e in enumerate(elem):
                self.setItem(i, index, QTableWidgetItem(e))

    def _getRowCount(self, nestlist):
        holder = list()
        for i in nestlist:
            holder.append(len(i))
        self.setRowCount(max(holder))
