# pyqt
from PyQt5.QtWidgets import QListView


class ListView(QListView):
    """List View"""
    def __init__(self,items, parent=None):
        super().__init__(parent)
        self.items = items or list()
