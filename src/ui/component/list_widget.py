# pyqt
from PyQt5.QtWidgets import QListWidget


# noinspection PyUnresolvedReferences
class DropList(QListWidget):
    """Drop List"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self._bootstrap()

    def _bootstrap(self):
        self.setAcceptDrops(True)
        self.setFlow(QListWidget.LeftToRight)
        self.setAlternatingRowColors(True)
        self.itemDoubleClicked.connect(self._doubleClicked)

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

    def _doubleClicked(self):
        selected = self.currentRow()
        self.takeItem(selected)

    def getMembers(self):
        memberList = list()
        for member in range(self.count()):
            memberList.append(self.item(member).text())

        print(memberList)
        # return memberList
