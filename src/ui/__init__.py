# internal
from src.ui.window import (DbResponse, ExcelResponse, AssembleWidget,
                           DbTablesName, DbTableTitles)
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget


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
        # front widget
        self.assembleWidget = AssembleWidget()
        # excel response
        self.excelResponse = ExcelResponse()
        # database response
        self.dbResponse = DbResponse()
        # database table
        self.dbTable = DbTablesName()
        # database titles
        self.dbTableTitles = DbTableTitles()
        # attach
        self._mainWidget.setLayout(self.generalLayout)
        self.generalLayout.addWidget(self.assembleWidget)

    def _styleSheet(self):
        self.setStyleSheet("""
            MainWindow {
                background: #fcfcfc;
            }
        """)
