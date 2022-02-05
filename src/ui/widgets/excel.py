# internal
from .base_dialog import BaseDialog
from src.ui.component import FireButton, DrgDrpTable
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.Qt import QListView, QAbstractItemView
from PyQt5.QtWidgets import QHBoxLayout


class ExcelResponse(BaseDialog):
    """Excel Responsible"""
    def _craftDialog(self):
        # self modification
        self.setWindowTitle('Excel Titles')
        self.setFixedWidth(320)
        # excel table
        self.listExcel = QListView()
        self.listExcel.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # done button
        self.btnDoneLayout = QHBoxLayout()
        self.btnDoneLayout.setAlignment(Qt.AlignHCenter)
        self.btnDone = FireButton('Done')
        # attach
        self.generalLayout.addWidget(self.listExcel)
        self.btnDoneLayout.addWidget(self.btnDone)
        self.generalLayout.addLayout(self.btnDoneLayout)

    def _innerToMainTable(self):
        checkedItems = list()
        excelHeaders = self.ui.modelExcel
        for i in sorted(excelHeaders.checkList):
            checkedItems.append(excelHeaders.items[i])

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

