# internal
from src.ui.component import BaseDialog, FireButton
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.Qt import QListView, QAbstractItemView


class DbTablesName(BaseDialog):
    """Database Tables"""
    def craftDialog(self):
        # self modification
        self.setWindowTitle('Data-base Tables')
        # tables list
        self.listTables = QListView()
        self.listTables.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # done button
        self.btnDoneLayout = QHBoxLayout()
        self.btnDoneLayout.setAlignment(Qt.AlignHCenter)
        self.btnDone = FireButton('Done')
        # attach
        self.btnDoneLayout.addWidget(self.btnDone)
        self.generalLayout.addWidget(self.listTables)
        self.generalLayout.addLayout(self.btnDoneLayout)

    def craftStyles(self):
        self.setStyleSheet("""
            DbTables {
                background: #fcfcfc;
            }
        """)
