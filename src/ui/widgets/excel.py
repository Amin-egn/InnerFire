# internal
from .base_dialog import BaseDialog
from src.ui.component import FireButton, DrgDrpTable, CheckList, ListView
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout


class ExcelResponse(BaseDialog):
    """Excel Responsible"""
    def _craftDialog(self):
        # self modification
        self.setWindowTitle('Excel Titles')
        self.setFixedWidth(320)
        # excel model
        self.excelCheckListModel = CheckList()
        # excel headers
        self.listExcelHeaders = ListView(self.excelCheckListModel)
        # done button
        self.btnDoneLayout = QHBoxLayout()
        self.btnDoneLayout.setAlignment(Qt.AlignHCenter)
        self.btnDone = FireButton('Done')
        # attach
        self.generalLayout.addWidget(self.listExcelHeaders)
        self.btnDoneLayout.addWidget(self.btnDone)
        self.generalLayout.addLayout(self.btnDoneLayout)

    def _innerToMainTable(self):
        checkedItems = list()

        for i in sorted(self.excelCheckListModel.checkList):
            checkedItems.append(self.excelCheckListModel.items[i])

        modelDrgDrp = DrgDrpTable(['Excel Headers'], checkedItems)
        self.ui.tableWidget.setModel(modelDrgDrp)

    # noinspection PyUnresolvedReferences
    def _connectSignals(self):
        self.btnDone.clicked.connect(self._innerToMainTable)

    def _craftStyles(self):
        self.setStyleSheet("""
            ExcelResponse {
                background: #fcfcfc;
            }
        """)
