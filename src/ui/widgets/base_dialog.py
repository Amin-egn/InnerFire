# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout


class BaseDialog(QDialog):
    """Base Dialog"""
    def __init__(self, ui, *args, **kwargs):
        super().__init__(ui, *args, **kwargs)
        self.ui = ui
        self._bootstrap()

    def _bootstrap(self):
        self._craftLayout()
        self._craftDialog()
        self._craftStyles()
        self._connectSignals()

    def _craftLayout(self):
        # layout
        self.generalLayout = QVBoxLayout()
        self.setLayout(self.generalLayout)
        # widgets modality
        self.setWindowModality(Qt.ApplicationModal)

    def _craftDialog(self):
        pass

    def _craftStyles(self):
        pass

    def _connectSignals(self):
        pass
