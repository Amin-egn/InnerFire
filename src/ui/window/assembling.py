# internal
from src.ui.component import BaseWidget, FireButton
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.Qt import QTableView
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel


class AssembleWidget(BaseWidget):
    """Front Widget"""
    def craftWidget(self):
        self.actionButtons()
        self.tableFrame()
        self.castButton()

    def actionButtons(self):
        # button layout
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setContentsMargins(0, 10, 0, 0)
        self.buttonsLayout.setAlignment(Qt.AlignHCenter)
        # excel button
        self.btnExcel = FireButton('Read Excel', icon='./src/ui/resources/spreadsheet.png')
        # data base button
        self.btnDb = FireButton('Query Data-Base', icon='./src/ui/resources/database.png')
        # attach
        self.buttonsLayout.addWidget(self.btnExcel)
        self.buttonsLayout.addWidget(self.btnDb)
        self.generalLayout.addLayout(self.buttonsLayout)

    def listFrame(self):
        pass

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
        self.castLayout.setContentsMargins(0, 10, 0, 5)
        # cast label
        self.lblCast = QLabel('You should select excel and sql table that you want to cast =)')
        # cast button
        self.btnCast = FireButton('Cast!')
        # attach
        self.castLayout.addWidget(self.lblCast)
        self.castLayout.addWidget(self.btnCast)
        self.generalLayout.addLayout(self.castLayout)

    def craftStyle(self):
        self.setStyleSheet("""
            #Table {
                border: 2px dot-dash #3d9049;
            }
        """)

