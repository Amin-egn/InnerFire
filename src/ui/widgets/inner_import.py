# internal
from .base import BaseWidget
from src.ui.component import SingleDimensionTableModel, DragDropTableView
# pyqt
from PyQt5.QtWidgets import QLabel, QFrame, QHBoxLayout


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
        # - model
        self.innerExcelTitleModel = SingleDimensionTableModel(['Excel\'s titels'])
        self.innerExcelTitleModel.setRecords(['Firstname', 'Lastname', 'Tell'])
        # - view
        self.innerExcelTitleView = DragDropTableView(self.innerExcelTitleModel)
        self.innerExcelTitleView.setFixedWidth(170)
        # Database
        # - model
        self.innerDbTitleModel = SingleDimensionTableModel(['Table\'s titles'])
        self.innerDbTitleModel.setRecords(['Code', 'Address', 'Name', 'Fname', 'Lname', 'Balance', 'Tell'])
        # - view
        self.innerDbTitleView = DragDropTableView(self.innerDbTitleModel)
        self.innerDbTitleView.setMinimumWidth(400)
        # attach
        # - importer
        self.importerLayout.addWidget(self.innerExcelTitleView)
        self.importerLayout.addWidget(self.innerDbTitleView)
        # - general
        self.generalLayout.addWidget(self.importerFrame)
