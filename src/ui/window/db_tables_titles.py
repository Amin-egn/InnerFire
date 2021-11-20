# internal
from src.ui.component import BaseDialog, FireButton
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.Qt import QListView
from PyQt5.QtWidgets import QHBoxLayout


class DbTableTitles(BaseDialog):
    """Database Table Titles"""
    def craftDialog(self):
        # self modification
        self.setWindowTitle('Table Titles')
        # tables list
        self.listTitles = QListView()
        # done button
        self.btnDoneLayout = QHBoxLayout()
        self.btnDoneLayout.setAlignment(Qt.AlignHCenter)
        self.btnDone = FireButton('Done')
        # attach
        self.btnDoneLayout.addWidget(self.btnDone)
        self.generalLayout.addWidget(self.listTitles)
        self.generalLayout.addLayout(self.btnDoneLayout)

    def craftStyles(self):
        self.setStyleSheet("""
            DbTableTitles {
                background: #fcfcfc;
            }
        """)
