# internal
from src.ui.component import BaseWidget, BaseDialog, FButton, TableModel
# external
from openpyxl import load_workbook
# pyqt
from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import QLinearGradient
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QHBoxLayout, QFileDialog,
                             QTableWidget, QTableWidgetItem, QLabel, QTableView, QDialog,
                             QVBoxLayout)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # bootstrap
        self._bootstrap()
        # stylesheet
        self._styleSheet()

    def _bootstrap(self):
        self.setWindowTitle('Inner Fire')
        self.setMinimumSize(640, 480)
        # central widget
        self._mainWidget = QWidget(self)
        self.setCentralWidget(self._mainWidget)
        # general layout
        self.generalLayout = QVBoxLayout()
        # set align top
        self.generalLayout.setAlignment(Qt.AlignTop)
        # excel response
        self.excelResponse = ExcelResponse()
        # attach
        self._mainWidget.setLayout(self.generalLayout)
        self.actionButtons()
        self.tableFrame()
        self.castButton()
        self.connectedSignals()

    def _styleSheet(self):
        self.setStyleSheet("""
            MainWindow {
                background: #fcfcfc;
            }
            #Buttons {
                border: none;
                color: #777777;
            }
            #Buttons:hover {
                border: 1px solid #66b071;
                border-radius: 20px;
                color: #111111;
            }
            #Buttons:pressed {
                border-color: #3d9049;
            }
            #Table {
                border: 2px dot-dash #3d9049;
            }
        """)

    def actionButtons(self):
        # button layout
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setContentsMargins(0, 10, 0, 0)
        self.buttonsLayout.setAlignment(Qt.AlignHCenter)
        # excel button
        self.btnExcel = FButton('Read Excel', icon='./src/ui/resources/spreadsheet.png')
        self.btnExcel.setObjectName('Buttons')
        self.btnExcel.iconSize = 24
        self.btnExcel.craftButton(200, 40)
        # data base button
        self.btnDb = FButton('Query Data-Base', icon='./src/ui/resources/database.png')
        self.btnDb.setObjectName('Buttons')
        self.btnDb.iconSize = 24
        self.btnDb.craftButton(200, 40)
        # attach
        self.buttonsLayout.addWidget(self.btnExcel)
        self.buttonsLayout.addWidget(self.btnDb)
        self.generalLayout.addLayout(self.buttonsLayout)

    def tableFrame(self):
        # frame widget
        self.tableWidget = QTableView()
        self.tableWidget.setObjectName('Table')
        # frame layout
        self.tableWidget.setMinimumSize(600, 360)
        self.tableLayout = QVBoxLayout()
        # attach
        self.tableWidget.setLayout(self.tableLayout)
        self.generalLayout.addWidget(self.tableWidget)

    def castButton(self):
        # cast layout
        self.castLayout = QHBoxLayout()
        self.castLayout.setContentsMargins(0, 10, 0, 0)
        # cast label
        self.lblCast = QLabel('You should select excel and sql table that you want to cast =)')
        # cast button
        self.btnCast = FButton('Cast!')
        self.btnCast.setObjectName('Buttons')
        self.btnCast.craftButton(200, 40)
        # attach
        self.castLayout.addWidget(self.lblCast)
        self.castLayout.addWidget(self.btnCast)
        self.generalLayout.addLayout(self.castLayout)

    def connectedSignals(self):
        self.btnExcel.clicked.connect(self.excelResponse.openExcel)


class ExcelResponse(BaseDialog):
    """Excel Handler"""
    def craftDialog(self):
        self.tblExcel = QTableView()
        # done button
        self.btnDone = FButton('Done')
        self.btnDone.craftButton(200, 40)
        # attach
        self.generalLayout.addWidget(self.tblExcel)
        self.generalLayout.addWidget(self.btnDone)

    def openExcel(self):
        self.titleList = list()

        path = QFileDialog.getOpenFileName(
            self, 'Open file', '',
            'Excel files (*.xlsx *.xlsm *.xltx *.xltm)')[0]
        if path:
            wb = load_workbook(path)
            sheet = wb.active
            for cell in sheet.iter_cols(max_row=1, values_only=True):
                self.titleList.append(list(cell))

        self.model = TableModel(['Excel Titles'], self.titleList)
        self.tblExcel.setModel(self.model)

        if self.titleList:
            self.show()



class RemoveSoon(BaseWidget):
    """Excel Handler"""
    def craftWidget(self):
        self.btnRead = FButton('Read Excel')
        self.btnRead.craftButton(120, 35)

        self.tblExcel = QTableView()

        self.generalLayout.addWidget(self.tblExcel)
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
                self.titleList.append(list(cell))

        self.model = TableModel(['Excel Titles'], self.titleList)
        self.tblExcel.setModel(self.model)

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
