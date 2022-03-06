# internal
from .base import BaseWidget
from src.ui.component import DragList, ListView, TableWidget, FireButton, ReceiveInput
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QFrame, QHBoxLayout, QVBoxLayout, QComboBox


# noinspection PyUnresolvedReferences
class WarpWoof(BaseWidget):
    """Warp And Woof"""
    def _craftWidget(self):
        self._guide()
        self._warpWoofer()
        self._wrapWoofFooter()

    def _guide(self):
        text = 'Attention ! \n' \
               'Before next stage, You must be sure. Please leave no rows empty'
        self.lblGuide = QLabel(text)
        self.generalLayout.addWidget(self.lblGuide)

    def _warpWoofer(self):
        # frame
        self.warpWooferFrame = QFrame(self)
        self.warpWooferFrame.setMinimumSize(580, 360)
        self.warpWooferFrame.setObjectName('Table')
        # layout
        self.warpWooferLayout = QHBoxLayout()
        self.warpWooferLayout.setContentsMargins(5, 5, 5, 5)
        self.warpWooferFrame.setLayout(self.warpWooferLayout)
        # Excel
        self._warpWoofExcel()
        # Database
        self._warpWoofDatabase()
        # attach
        self.generalLayout.addWidget(self.warpWooferFrame)

    def _warpWoofExcel(self):
        # excel layout
        self.innerExcelLayout = QVBoxLayout()
        self.innerExcelLayout.setAlignment(Qt.AlignHCenter)
        # label
        self.lblExcel = QLabel('Excel Titles')
        # model
        self.innerExcelTitleModel = DragList()
        self.innerExcelTitleModel.setItems(['foo', 'bar', 'baz', 'qux'])
        # view
        self.innerExcelTitleView = ListView(self.innerExcelTitleModel)
        self.innerExcelTitleView.setDragEnabled(True)
        self.innerExcelTitleView.setMinimumWidth(170)
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
        self.warpWooferLayout.addLayout(self.innerExcelLayout)

    def _warpWoofDatabase(self):
        # widget
        self.innerDbTitleWidget = TableWidget(['Title', 'Combobox', 'Droppables'])
        self.innerDbTitleWidget.setMinimumWidth(400)
        d = {'Amin': ['kala', 'mashin', 'laptop'], 'Samira': ['kolah'], 'Javad': ['bache', 'shekam']}
        self.innerDbTitleWidget.setRowRecords(d)
        # attach
        # - warpwoof
        self.warpWooferLayout.addWidget(self.innerDbTitleWidget)

    def _wrapWoofFooter(self):
        # layout
        self.footerLayout = QHBoxLayout()
        # button
        self.btnNextStage = FireButton('Next Stage!')
        # attach
        # - main
        self.footerLayout.addStretch()
        self.footerLayout.addWidget(self.btnNextStage)
        # - general
        self.generalLayout.addLayout(self.footerLayout)

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

    def _warpWoofHandler(self):
        # titleList = self.ui.entrance.titleList
        # record_holder = self.innerDbTitleWidget.getListRecords()
        # for value in record_holder.values():
        #     if value:
        #         for i in value:
        #             insert = 0
        #             if i in titleList:
        #                 rep = titleList.index(i)
        #                 value.remove(i)
        #                 value.insert(insert, rep)
        #                 insert += 1
        #
        # print(record_holder)
        # self.ui.innerImport.mapDict.update(record_holder)
        # print(self.innerDbTitleWidget.getListRecords())
        self.innerDbTitleWidget.getListRecords()

    def _connectSignals(self):
        # combobox
        self.comboBox.currentIndexChanged.connect(self._dragInputHandler)
        # cast button
        self.btnNextStage.clicked.connect(self._warpWoofHandler)

    def _craftStyle(self):
        self.setStyleSheet("""
            #Table {
                border: 2px dot-dash #33892a;
            }
        """)
