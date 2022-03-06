# pyqt
from PyQt5.QtWidgets import QListView, QAbstractItemView


class ListView(QListView):
    """List View"""
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.setModel(model)
        self._craftList()

    def _craftList(self):
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setAlternatingRowColors(True)

    def index(self, val=False):
        indexes = self.selectedIndexes()
        if val:
            return indexes[0].data() if indexes else None

        return indexes[0].row() if indexes else None
