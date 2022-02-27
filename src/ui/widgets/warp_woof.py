# internal
from .base import BaseWidget
from src.ui.component import DragList, ListView, TableWidget, FireButton, ReceiveInput
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QFrame, QHBoxLayout, QVBoxLayout, QComboBox


# noinspection PyUnresolvedReferences
class InnerImport(BaseWidget):
    """Inner Import"""
    def _craftWidget(self):
        self._guide()
        self._importer()

    def _guide(self):
        text = 'Attention ! \n' \
               'Before you cast, You must be sure. Please leave no rows empty'
        self.lblGuide = QLabel(text)
        self.generalLayout.addWidget(self.lblGuide)

    def _importer(self):
        # frame
        self.importerFrame = QFrame(self)
        # layout
        self.importerLayout = QHBoxLayout()
        self.importerFrame.setLayout(self.importerLayout)
        # Excel
        self._innerExcel()
        # Database
        self._innerDatabase()
        # attach
        self.generalLayout.addWidget(self.importerFrame)

    def _innerExcel(self):
        # excel layout
        self.innerExcelLayout = QVBoxLayout()
        self.innerExcelLayout.setAlignment(Qt.AlignHCenter)
        # label
        self.lblExcel = QLabel('Excel Titles')
        # model
        self.innerExcelTitleModel = DragList()
        self.innerExcelTitleModel.setItems(['Name', 'Lastname', 'Tell', 'Code'])
        # view
        self.innerExcelTitleView = ListView(self.innerExcelTitleModel)
        self.innerExcelTitleView.setAlternatingRowColors(True)
        self.innerExcelTitleView.setDragEnabled(True)
        self.innerExcelTitleView.setMinimumWidth(175)
        # input combobox
        self.comboBox = QComboBox()
        self.comboBox.addItem('String')
        self.comboBox.addItem('Integer')
        # drag input
        self.dragInput = ReceiveInput(placeHolder='Please insert strings', drag=True)
        # attach
        # - main
        self.innerExcelLayout.addWidget(self.lblExcel)
        self.innerExcelLayout.addWidget(self.innerExcelTitleView)
        self.innerExcelLayout.addWidget(self.comboBox)
        self.innerExcelLayout.addWidget(self.dragInput)
        # - importer
        self.importerLayout.addLayout(self.innerExcelLayout)

    def _innerDatabase(self):
        # database layout
        self.innerDbLayout = QVBoxLayout()
        self.innerDbLayout.setAlignment(Qt.AlignHCenter)
        # widget
        self.innerDbTitleWidget = TableWidget(['Title', 'Combobox', 'Droppables'])
        self.innerDbTitleWidget.setRowRecords(['Names', 'LastNames', 'Codes', 'Fullnames'])
        self.innerDbTitleWidget.setMinimumWidth(400)
        # button
        self.btnNextStage = FireButton('Cast')
        # attach
        # - main
        self.innerDbLayout.addWidget(self.innerDbTitleWidget)
        self.innerDbLayout.addWidget(self.btnNextStage)
        # - importer
        self.importerLayout.addLayout(self.innerDbLayout)

    def _dragInputHandler(self, index):
        self.dragInput.clear()
        if index == 0:
            text = 'Please insert strings'
            trufal = False
        else:
            text = 'Please insert integers'
            trufal = True

        self.dragInput.setPlaceholderText(text)
        self.dragInput.intValid(trufal)

    def _importHandler(self):
        self.innerDbTitleWidget.getListRecords()

    def _connectSignals(self):
        # combobox
        self.comboBox.currentIndexChanged.connect(self._dragInputHandler)
        # cast button
        self.btnNextStage.clicked.connect(self._importHandler)
