# internal
from .base_dialog import BaseDialog
from src.ui.component import FireButton, CheckList, ListView, SingleDimensionTableModel, TableView
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout


class ExcelResponse(BaseDialog):
    """Excel Responsible"""
    def _craftDialog(self):
        # self modification
        self.setWindowTitle('Excel Titles')
        self.setFixedWidth(320)
        # checklist model
        self.excelCheckListModel = CheckList()
        # list view
        self.excelListView = ListView(self.excelCheckListModel)
        # table model
        self.excelTableModel = SingleDimensionTableModel([])
        # table view
        self.excelTableView = TableView(self.excelTableModel)
        # done button
        self.btnDoneLayout = QHBoxLayout()
        self.btnDoneLayout.setAlignment(Qt.AlignHCenter)
        self.btnDone = FireButton('Done')
        # attach
        # - button layout
        self.btnDoneLayout.addWidget(self.btnDone)
        # - general
        self.generalLayout.addWidget(self.excelListView)
        self.generalLayout.addLayout(self.btnDoneLayout)
        # - entrance
        self.ui.modelsLayout.addWidget(self.excelTableView)

    def _innerToMainTable(self):
        checkedItems = list()
        try:
            for i in sorted(self.excelCheckListModel.checkList):
                checkedItems.append(self.excelCheckListModel.items[i])

            self.excelTableModel.header = ['Excel Headers']

        except Exception as e:
            print(str(e))
            self.excelTableModel.clearRecords()

        finally:
            self.excelTableModel.setRecords(checkedItems)

    # noinspection PyUnresolvedReferences
    def _connectSignals(self):
        self.btnDone.clicked.connect(self._innerToMainTable)

    def _craftStyles(self):
        self.setStyleSheet("""
            ExcelResponse {
                background: #fcfcfc;
            }
        """)
