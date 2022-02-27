# pyqt
from PyQt5.QtWidgets import QListWidget


# noinspection PyUnresolvedReferences
class ListWidget(QListWidget):
    """List Widget"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self._bootstrap()

    def _bootstrap(self):
        self._craftList()
        self.setAlternatingRowColors(True)
        self.itemDoubleClicked.connect(self._doubleClicked)

    def _craftList(self):
        pass

    def _doubleClicked(self):
        self.takeItem(self.currentRow())

    def getMembers(self):
        memberList = list()
        for member in range(self.count()):
            memberList.append(self.item(member).text())

        return memberList


class DropList(ListWidget):
    """Drop List"""
    def _craftList(self):
        self.setAcceptDrops(True)
        self.setFlow(QListWidget.LeftToRight)

    def mimeTypes(self):
        mimetypes = super().mimeTypes()
        mimetypes.append('text/plain')
        return mimetypes

    def dropMimeData(self, index, data, action):
        if data.hasText():
            self.addItem(data.text())
            return True
        else:
            return super().dropMimeData(index, data, action)
