# pyqt
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon, QFont, QCursor


class FireButton(QPushButton):
    """Basic Button"""
    width = 75
    height = 23
    alt = ''
    font = 'Lucida console'
    fontSize = 12
    ICON = ''
    iconSize = 16

    def __init__(self, *args, **kwargs):
        self.size = kwargs.pop('size', None)
        self.icon = kwargs.pop('icon', self.ICON)
        super().__init__(*args, **kwargs)
        self.craftButton(self.width, self.height)

    def craftButton(self, width, height):
        self.setFixedSize(width, height)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        if self.alt:
            self.setToolTip(self.alt)
        if self.font:
            self.setFont(QFont(self.font, self.fontSize))
        if self.icon:
            self.setIcon(QIcon(self.icon))
            self.setIconSize(QSize(self.iconSize, self.iconSize))


class FlameButton(FireButton):
    pass