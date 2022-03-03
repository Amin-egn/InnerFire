# internal
from .base_dialog import BaseDialog
from src.ui.component import (ListView, SingleDimensionTableModel, ListModel,
                              AddButton, RemoveButton, LockedTableView, ReceiveInput)
# pyqt
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import QHBoxLayout


class ExcelResponse(BaseDialog):
    """Excel Responsible"""
    def _craftDialog(self):
        self.setWindowUnits('Excel Titles', ':/icons/excel')
        # self modification
        self.setFixedWidth(480)
        self._searchBar()
        self._excelModelView()
        self._buttons()

    def _searchBar(self):
        self.searchInput = ReceiveInput(placeHolder='Search titles\'s name')
        # attach
        # - general
        self.generalLayout.addWidget(self.searchInput)

    def _excelModelView(self):
        # layout
        self.modelViewLayout = QHBoxLayout()
        # list
        # - list
        self.excelTitleList = list()
        # - model
        self.excelListModel = ListModel()
        # - proxy
        self.proxyModel = QSortFilterProxyModel(self)
        self.proxyModel.setSourceModel(self.excelListModel)
        # - view
        self.excelListView = ListView(self.proxyModel)
        # table
        # - model
        self.selectedTitleTableModel = SingleDimensionTableModel(['Selected Titles'])
        # - view
        self.selectedTitleTableView = LockedTableView(self.selectedTitleTableModel)
        # attach
        # - main
        self.modelViewLayout.addWidget(self.selectedTitleTableView)
        self.modelViewLayout.addWidget(self.excelListView)
        # - general
        self.generalLayout.addLayout(self.modelViewLayout)

    def _buttons(self):
        # layout
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setAlignment(Qt.AlignRight)
        # add button
        self.btnAdd = AddButton('Add')
        # remove button
        self.btnRemove = RemoveButton('Remove')
        # attach
        # - main
        self.buttonsLayout.addWidget(self.btnAdd)
        self.buttonsLayout.addWidget(self.btnRemove)
        # - general
        self.generalLayout.addLayout(self.buttonsLayout)

    def _searchHandler(self, text):
        self.proxyModel.setFilterRegExp(str(text))

    def _innerToMainTable(self, status):
        selected_row = self.excelListView.index(True)
        if status == 'add':
            if selected_row not in self.excelTitleList:
                self.excelTitleList.append(selected_row)
        else:
            if selected_row in self.excelTitleList:
                self.excelTitleList.remove(selected_row)

        self.selectedTitleTableModel.setRecords(self.excelTitleList)

    def closeEvent(self, event):
        if self.excelTitleList:
            self.ui.excelDataCollectorList.extend(self.excelTitleList)
            self.ui.createExcelView(self.selectedTitleTableModel)

        self.close()

    # noinspection PyUnresolvedReferences
    def _connectSignals(self):
        # search
        self.searchInput.textChanged.connect(self._searchHandler)
        # buttons
        # - add
        self.btnAdd.clicked.connect(lambda: self._innerToMainTable('add'))
        # - remove
        self.btnRemove.clicked.connect(lambda: self._innerToMainTable('remove'))

    def _craftStyles(self):
        self.setStyleSheet("""
            ExcelResponse {
                background: #fcfcfc;
            }
        """)
