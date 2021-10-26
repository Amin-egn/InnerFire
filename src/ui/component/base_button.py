# pyqt
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon, QFont, QCursor


class FButton(QPushButton):
    """Basic Button"""
    width = 75
    height = 23
    alt = ''
    font = ''
    fontSize = 12
    icon = ''
    iconSize = 16

    def __init__(self, *args, **kwargs):
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
