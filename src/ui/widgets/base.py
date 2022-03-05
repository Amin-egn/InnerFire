# pyqt
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class BaseWidget(QWidget):
    """Base Widget"""
    def __init__(self, parent=None):
        self.ui = parent
        super().__init__(parent)
        self._bootstrap()

    def _bootstrap(self):
        self._initialize()
        self._craftLayout()
        self._craftWidget()
        self._craftStyle()
        self._connectSignals()

    def _craftLayout(self):
        self.generalLayout = QVBoxLayout()
        self.generalLayout.setContentsMargins(5, 7, 5, 5)
        self.setLayout(self.generalLayout)

    def _initialize(self):
        pass

    def _craftWidget(self):
        pass

    def _craftStyle(self):
        pass

    def _connectSignals(self):
        pass

    def reset(self):
        self._initialize()
