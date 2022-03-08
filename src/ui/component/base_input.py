# pyqt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLineEdit, QSpinBox


# noinspection PyTypeChecker
class BaseInput(QLineEdit):
    """Base Input"""
    HEIGHT = 0

    def __init__(self, *args, **kwargs):
        self._pwd = kwargs.pop('password', False)
        self._placeHolder = kwargs.pop('placeHolder', '')
        self._textSelect = kwargs.pop('textSelect', False)
        self._intVal = kwargs.pop('intValidate', False)
        self._draggable = kwargs.pop('drag', False)
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

        if self._textSelect:
            self.mousePressEvent = lambda _: self.selectAll()

        if self._intVal:
            self.setValidator(QIntValidator())

        if self._draggable:
            self.setDragEnabled(True)

    def intValid(self, boolean):
        if boolean:
            self.setValidator(QIntValidator())
        else:
            self.setValidator(None)

    def _craftStyle(self):
        pass


class ReceiveInput(BaseInput):
    """Receive Input"""
    HEIGHT = 29


class BaseSpinbox(QSpinBox):
    """Base Spinbox"""
    SIZE = ()

    def __init__(self, *args, **kwargs):
        self._size = kwargs.pop('size', self.SIZE)
        self._fixText = kwargs.pop('fixText', None)
        self._suffText = kwargs.pop('suffText', None)
        self._minVal = kwargs.pop('minVal', None)
        self._maxVal = kwargs.pop('maxVal', None)
        super().__init__(*args, **kwargs)
        self._bootstrap()

    def _bootstrap(self):
        self._craftSpin()
        self._craftSpin()

    def _craftSpin(self):
        self.setFixedSize(*self._size)
        if self._fixText:
            self.setPrefix(self._fixText)

        if self._suffText:
            self.setSuffix(self._suffText)

        if self._minVal:
            self.setMinimum(self._minVal)

        if self._maxVal:
            self.setMaximum(self._maxVal)

    def _craftStyle(self):
        pass


class ReceiveSpin(BaseSpinbox):
    """Receive Spinbox"""
    SIZE = (200, 30)
