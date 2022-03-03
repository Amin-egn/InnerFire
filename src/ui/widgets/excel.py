# internal
from .base_dialog import BaseDialog
from src.ui.component import FireButton, CheckList, ListView, SingleDimensionTableModel, TableView
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout


class ExcelResponse(BaseDialog):
    """Excel Responsible"""
    def _craftDialog(self):
        self.setWindowUnits('Excel Titles', ':/icons/excel')
        # self modification
        self.setFixedWidth(380)
        # checklist model
        self.excelCheckListModel = CheckList()
        # list view
        self.excelListView = ListView(self.excelCheckListModel)
        # table model
        self.excelTableModel = SingleDimensionTableModel([])
        # table view
        self.excelTableView = TableView(self.excelTableModel)
        # buttons
        # - layout
        self.btnDoneLayout = QHBoxLayout()
        self.btnDoneLayout.setAlignment(Qt.AlignHCenter)
        # - doen
        self.btnDone = FireButton('Done')
        # - exit
        self.btnExit = FireButton('Exit')
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
                # todo: duplicate Excel titles
                checkedItems.append(self.excelCheckListModel.items[i])

            self.excelTableModel.header = ['Excel Titles']
            self.ui.excelWidgetSignal = 1

        except Exception as e:
            print(str(e))
            self.excelTableModel.clearRecords()
            self.ui.excelWidgetSignal = 0
            self.ui.listExcelDataCollector.clear()

        finally:
            self.excelTableModel.setRecords(checkedItems)
            self.ui.listExcelDataCollector.extend(self.excelTableModel.records)

    def closeEvent(self, event):
        if not self.excelTableModel.isEmpty():
            self.ui.checkWidgetNumbers()

        self.close()

    # noinspection PyUnresolvedReferences
    def _connectSignals(self):
        self.btnDone.clicked.connect(self._innerToMainTable)

    def _craftStyles(self):
        self.setStyleSheet("""
            ExcelResponse {
                background: #fcfcfc;
            }
        """)
