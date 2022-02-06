# internal
from .base import BaseWidget
from .excel import ExcelResponse
from .database import DbResponse
from src.ui.component import FireButton, TableView, SingleDimensionTableModel
# external
from openpyxl import load_workbook
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QFileDialog, QFrame


class Entrance(BaseWidget):
    """Entrance"""
    def _craftWidget(self):
        self._actionButtons()
        # self._tableWidget()
        self._modelsFrame()
        self._castButton()
        self.excelResponse = ExcelResponse(self)

    def _actionButtons(self):
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
        # - general
        self.generalLayout.addLayout(self.buttonsLayout)

    def _tableWidget(self):
        # table model headers
        self.listTableModelHeaders = []
        # table model
        self.tableModel = SingleDimensionTableModel(self.listTableModelHeaders)
        # table view
        self.tableView = TableView(self.tableModel)
        self.tableView.setObjectName('Table')
        self.tableView.setMinimumSize(580, 360)
        # attach
        # - general
        self.generalLayout.addWidget(self.tableView)

    def _modelsFrame(self):
        # frame
        self.modelsFrame = QFrame(self)
        self.modelsFrame.setMinimumSize(580, 360)
        self.modelsFrame.setObjectName('Table')
        # layout
        self.modelsLayout = QHBoxLayout()
        self.modelsFrame.setLayout(self.modelsLayout)
        # attach
        self.generalLayout.addWidget(self.modelsFrame)

    def _castButton(self):
        # cast layout
        self.castLayout = QHBoxLayout()
        self.castLayout.setContentsMargins(0, 10, 0, 5)
        # cast label
        self.lblCast = QLabel('You should select excel and sql table that you want to cast =)')
        # cast button
        self.btnCast = FireButton('Next Stage!')
        self.btnCast.setDisabled(True)
        # attach
        self.castLayout.addWidget(self.lblCast)
        self.castLayout.addWidget(self.btnCast)
        # - general
        self.generalLayout.addLayout(self.castLayout)

    def _openExcel(self):
        # empty list
        titleList = list()
        try:
            path = QFileDialog.getOpenFileName(
                self, 'Open file', '',
                'Excel files (*.xlsx *.xlsm *.xltx *.xltm)')[0]
            if path:
                wb = load_workbook(path)
                sheet = wb.active
                for cell in sheet.iter_cols(max_row=1, values_only=True):
                    index = cell[0]
                    if index:
                        strip_index = str(index).strip()
                        titleList.append(strip_index)

        except Exception as e:
            print(str(e))

        else:
            if titleList:
                # excel
                self.excelResponse.show()
                self.excelResponse.excelCheckListModel.items = titleList
                self.excelResponse.excelCheckListModel.layoutChanged.emit()

            else:
                print('No Excel Selected !')

    def _database(self):
        # database
        self.dbResponse = DbResponse(self)
        self.dbResponse.show()

    def checkWidgetNumbers(self):
        if self.modelsLayout.count() > 1:
            self.btnCast.setEnabled(True)

    # noinspection PyUnresolvedReferences
    def _connectSignals(self):
        self.btnExcel.clicked.connect(self._openExcel)
        self.btnDb.clicked.connect(self._database)

    def _craftStyle(self):
        self.setStyleSheet("""
            MainWindow {
                background: #fcfcfc;
            }
            #Table {
                border: 2px dot-dash #3d9049;
            }
        """)
