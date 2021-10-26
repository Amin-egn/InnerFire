# internal
from src.ui.component import BaseWidget, BaseDialog, FButton
# external
from openpyxl import load_workbook
# pyqt
from PyQt5.QtGui import QLinearGradient
from PyQt5.QtCore import (QAbstractTableModel, Qt)
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QHBoxLayout, QFileDialog,
                             QTableWidget, QTableWidgetItem, QLabel)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # bootstrap
        self._bootstrap()
        # stylesheet
        self._styleSheet()

    def _bootstrap(self):
        self.setMinimumSize(640, 480)
        self._mainWidget = QWidget(self)
        self.setCentralWidget(self._mainWidget)
        self.generalLayout = QHBoxLayout()
        self._mainWidget.setLayout(self.generalLayout)
        self.excelHandler = ExcelResponse()
        self.generalLayout.addWidget(self.excelHandler)

    def _styleSheet(self):
        self.setStyleSheet("""
            background: #fcfcfc;
        """)

class ExcelResponse(BaseWidget):
    """Excel Handler"""
    def craftWidget(self):
        self.btnRead = FButton('Read Excel')
        self.btnRead.craftButton(120, 35)

        self.btnHeader = FButton('Show Headers')
        self.btnHeader.craftButton(120, 35)

        self.TblExcel = QTableWidget()
        self.TblExcel.setColumnCount(4)

        self.generalLayout.addWidget(self.TblExcel)
        self.generalLayout.addWidget(self.btnHeader)
        self.generalLayout.addWidget(self.btnRead)

    def openExcel(self):
        self.titleList = list()
        path = QFileDialog.getOpenFileName(
            self, 'Open file', '',
            'Excel files (*.xlsx)')[0]
        if path:
            wb = load_workbook(path)
            sheet = wb.active
            for cell in sheet.iter_cols(max_row=1, values_only=True):
                self.titleList.extend(list(cell))

        for r, i in enumerate(self.titleList):
            self.TblExcel.setItem(r, 1, QTableWidgetItem(i))


    def craftStyle(self):
        self.setStyleSheet("""
            QPushButton {
                background: QLinearGradient(
                x1: 1 y1: 1,
                x2: 0 y2: 0,
                stop: 1 #c2e59c,
                stop: 0 #64b3f4
                );
                border: 1px solid #ccc;
                color: #555;
            }
            QPushButton:hover {
                background: QLinearGradient(
                x1: 1 y1: 1,
                x2: 0 y2: 0,
                stop: 1 #64b3f4,
                stop: 0 #c2e59c
                );
                border-color: #888;
                color: #222;
            }
            QPushButton:pressed {
                border-style: double;
                color: #000
            }
        """)

    def connectSignals(self):
        self.btnRead.clicked.connect(self.openExcel)


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
