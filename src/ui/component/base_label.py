# pyqt
from PyQt5.QtWidgets import QLabel


# class DragLabel(QLabel):
#     """Draggable Label"""
#     def __init__(self, text, parent):
#         super().__init__(text, parent)
#         self.setAutoFillBackground(True)
#         self.setFrameShape(QFrame.Panel)
#         self.setFrameShadow(QFrame.Raised)
#
#     def mousePressEvent(self, event):
#         hotSpot = event.pos()
#         mimeData = QMimeData()
#         mimeData.setText(self.text())
#         mimeData.setData('application/x-hotspot',
#                 '%d %d' % (hotSpot.x(), hotSpot.y()))
#
#         pixmap = QPixmap(self.size())
#         self.render(pixmap)
#
#         drag = QDrag(self)
#         drag.setMimeData(mimeData)
#         drag.setPixmap(pixmap)
#         drag.setHotSpot(hotSpot)
#
#         dropAction = drag.exec_(Qt.CopyAction | Qt.MoveAction, Qt.CopyAction)
#
#         if dropAction == Qt.MoveAction:
#             self.close()
#             self.update()


class MessageLabel(QLabel):
    """Message Label"""
    OPERATION = ['FAILED', 'SUCCEED']
    COLORS = [('#F8D7DA', '#842029'),
              ('#D1E7DD', '#0F5132')]

    def __init__(self, message, level, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message
        self.level = level
        self._bootstrap()

    def _bootstrap(self):
        self._craftMessage()
        self._craftStyle()

    def _craftMessage(self):
        self.setText(f'<h3>{self.OPERATION[self.level]}</h3><p>{self.message}</p>')

    def _craftStyle(self):
        bgColor, color = self.COLORS[self.level][0], self.COLORS[self.level][1]
        self.setStyleSheet(f"""
            padding: 5px;
            color: {color};
            border: 1px solid {color};
            background-color: {bgColor};
        """)
