# pyqt
from PyQt5.QtWidgets import QTableView, QAbstractItemView


class TableView(QTableView):
    """Table View"""
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.setModel(model)
        self._craftTable()
        self._craftDND()

    def _craftTable(self):
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.horizontalHeader().setStretchLastSection(True)

    def _craftDND(self):
        pass

    def index(self, val=False):
        indexes = self.selectedIndexes()
        if val:
            return indexes[0].data() if indexes else None

        return indexes[0].row() if indexes else None


class DragDropTableView(TableView):
    """Drag Table View"""
    def _craftDND(self):
        self.setDragEnabled(True)
        self.setDragDropOverwriteMode(True)

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        event.accept()
