# pyqt
from PyQt5.QtWidgets import QComboBox


# noinspection PyUnresolvedReferences
class ComboBox(QComboBox):
    """Combobox"""
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.ui = parent
        self.addItems(items)
        self.currentIndexChanged.connect(self.ui.changeIndex)

    # def changeIndex(self, func):
    #     self.currentIndexChanged.connect(func)
