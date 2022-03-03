# internal
from .base_button import AddButton, RemoveButton
# pyqt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox


class BaseMessage(QMessageBox):
    """Base Message"""
    TITLE = 'Base Message'
    ICON = QMessageBox.NoIcon
    BUTTONS = QMessageBox.Ok
    FLAGICON = ':/icons/book'

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.text = text
        self._bootstrap()

    def _bootstrap(self):
        self._craftMessage()
        self._craftStyle()

    def _craftMessage(self):
        self.setWindowTitle(self.TITLE)
        self.setText(self.text)
        pix = QPixmap(self.ICON)
        pix.scaledToWidth(64)
        pix.scaledToHeight(64)
        self.setIconPixmap(pix)
        self.setWindowIcon(QIcon(self.FLAGICON))

        if self.BUTTONS & QMessageBox.Ok:
            self.addButton(AddButton('Okayyy'), QMessageBox.AcceptRole)

        if self.BUTTONS & QMessageBox.Yes:
            self.addButton(AddButton('Yesss'), QMessageBox.YesRole)

        if self.BUTTONS & QMessageBox.No:
            self.addButton(RemoveButton('Nooo'), QMessageBox.RejectRole)

    def _craftStyle(self):
        self.setStyleSheet("""
            BaseMessage {
                background: #fcfcfc;
            }
        """)


class WarningMessage(BaseMessage):
    """Warning Message"""
    TITLE = 'InnerFire-Error!!!'
    ICON = ':/icons/warning'
    BUTTONS = QMessageBox.Ok


class QuestionMessage(BaseMessage):
    """Question Message"""
    TITLE = 'InnerFire-Question?'
    ICON = ':/icons/question'
    BUTTONS = QMessageBox.Yes | QMessageBox.No


class InfoMessage(BaseMessage):
    """Information Message"""
    TITLE = 'InnerFire-Info!'
    ICON = ':/icons/information'
    BUTTONS = QMessageBox.Ok
