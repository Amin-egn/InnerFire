# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout


class BaseDialog(QDialog):
    """Base Dialog"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bootstrap()

    def _bootstrap(self):
        self.craftLayout()
        self.craftDialog()
        self.craftStyles()
        self.connectSignals()

    def craftLayout(self):
        # layout
        self.generalLayout = QVBoxLayout()
        self.setLayout(self.generalLayout)
        # window modality
        self.setWindowModality(Qt.ApplicationModal)

    def craftDialog(self):
        pass

    def craftStyles(self):
        pass

    def connectSignals(self):
        pass
