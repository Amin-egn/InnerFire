# pyqt
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon, QFont, QCursor


class BaseButton(QPushButton):
    """Basic Button"""
    SIZE = (84, 40)
    FONT = ''
    fontSize = 12
    ICON = ''
    iconSize = 24

    def __init__(self, *args, **kwargs):
        self.size = kwargs.pop('size', self.SIZE)
        self.icon = kwargs.pop('icon', self.ICON)
        self.font = kwargs.pop('font', self.FONT)
        super().__init__(*args, **kwargs)
        self._bootstrap()

    def _bootstrap(self):
        self.craftButton()
        self.craftStyle()

    def craftButton(self):
        self.setFixedSize(*self.size)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        if self.font:
            self.setFont(QFont(self.font, self.fontSize))
        if self.icon:
            self.setIcon(QIcon(self.icon))
            self.setIconSize(QSize(self.iconSize, self.iconSize))

    def craftStyle(self):
        pass


class FireButton(BaseButton):
    FONT = 'Lucida console'
    SIZE = (200, 40)

    def craftStyle(self):
        self.setStyleSheet("""
            FireButton {
                border: none;
                color: #777777;
            }
            FireButton:hover {
                border: 1px solid #66b071;
                border-radius: 20px;
                color: #111111;
            }
            FireButton:pressed {
                border-color: #3d9049;
            }
        """)
