# pyqt
from PyQt5.QtWidgets import QLineEdit


class BaseInput(QLineEdit):
    """Base Input"""
    HEIGHT = 0

    def __init__(self, *args, **kwargs):
        self._pwd = kwargs.pop('password', False)
        self._placeHolder = kwargs.pop('placeHolder', '')
        super().__init__(*args, **kwargs)
        self._bootstrap()

    def _bootstrap(self):
        self._craftInput()
        self._craftStyle()

    def _craftInput(self):
        self.setFixedHeight(self.HEIGHT)
        if self._pwd:
            self.setEchoMode(QLineEdit.Password)

        if self._placeHolder:
            self.setPlaceholderText(self._placeHolder)

    def _craftStyle(self):
        pass


class ReceiveInput(BaseInput):
    """Receive Input"""
    HEIGHT = 29
