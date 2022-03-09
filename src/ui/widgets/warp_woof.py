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
        self.excelLayout = QVBoxLayout()
        self.excelLayout.setAlignment(Qt.AlignHCenter)
        # label
        self.lblExcel = QLabel('Excel Titles')
        # model
        self.excelTitleModel = DragList()
        # view
        self.excelTitleView = ListView(self.excelTitleModel)
        self.excelTitleView.setDragEnabled(True)
        self.excelTitleView.setMinimumWidth(170)
        # input combobox
        self.comboBox = QComboBox()
        self.comboBox.addItem('String')
        self.comboBox.addItem('Integer')
        # drag input
        self.dragInput = ReceiveInput(placeHolder='Please insert strings', drag=True)
        # attach
        # - main
        self.excelLayout.addWidget(self.lblExcel)
        self.excelLayout.addWidget(self.excelTitleView)
        self.excelLayout.addWidget(self.comboBox)
        self.excelLayout.addWidget(self.dragInput)
        # - importer
        self.warpWooferLayout.addLayout(self.excelLayout)

    def _warpWoofDatabase(self):
        # widget
        self.dbTitleWidget = TableWidget(['Title', 'Combobox', 'Droppables'])
        self.dbTitleWidget.setMinimumWidth(400)
        # attach
        # - warpwoof
        self.warpWooferLayout.addWidget(self.dbTitleWidget)

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

    def _nextStageHandler(self):
        titleList = self.ui.entrance.titleList
        record_holder = self.dbTitleWidget.getListRecords()
        for column in record_holder.values():
            for drop_title in column.values():
                if drop_title:
                    for title in drop_title:
                        insert = 0
                        if title in titleList:
                            rep = titleList.index(title)
                            drop_title.remove(title)
                            drop_title.insert(insert, rep)
                            insert += 1

        self.ui.innerImport.mapDict.update(record_holder)

    def _connectSignals(self):
        # combobox
        self.comboBox.currentIndexChanged.connect(self._dragInputHandler)
        # cast button
        self.btnNextStage.clicked.connect(self._nextStageHandler)

    def _craftStyle(self):
        self.setStyleSheet("""
            #Table {
                border: 2px dot-dash #33892a;
            }
        """)
