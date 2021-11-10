# pyqt
from PyQt5.QtWidgets import QTableView, QAbstractItemView


class TableView(QTableView):
    """Table View"""
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.setModel(model)
        self._craftTable()

    def _craftTable(self):
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.horizontalHeader().setStretchLastSection(True)
