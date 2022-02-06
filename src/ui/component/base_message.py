# internal
from .base_button import AddButton, RemoveButton
# pyqt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class BaseMessage(QMessageBox):
    """Base Message"""
    TITLE = 'Base Message'
    ICON = QMessageBox.NoIcon
    BUTTONS = QMessageBox.Ok
    FLAGICON = None

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
        self.setIcon(self.ICON)
        if self.FLAGICON:
            self.setWindowIcon(QIcon(self.FLAGICON))

        if self.BUTTONS & QMessageBox.Ok:
            self.addButton(AddButton('باشه'), QMessageBox.AcceptRole)

        if self.BUTTONS & QMessageBox.Yes:
            self.addButton(AddButton('بله'), QMessageBox.YesRole)

        if self.BUTTONS & QMessageBox.No:
            self.addButton(RemoveButton('خیر'), QMessageBox.RejectRole)

    def _craftStyle(self):
        self.setStyleSheet("""
            BaseMessage {
                background: #fcfcfc;
            }
        """)


class WarningMessage(BaseMessage):
    """Warning Message"""
    TITLE = 'InnerFire-Error!!!'
    ICON = QMessageBox.Warning
    BUTTONS = QMessageBox.Ok
    FLAGICON = './src/ui/resources/reaper.png'


class QuestionMessage(BaseMessage):
    """Question Message"""
    TITLE = 'InnerFire-Question?'
    ICON = QMessageBox.Question
    BUTTONS = QMessageBox.Yes | QMessageBox.No
    FLAGICON = './src/ui/resources/orc.png'


class InfoMessage(BaseMessage):
    """Information Message"""
    TITLE = 'InnerFire-Info!'
    ICON = QMessageBox.Information
    BUTTONS = QMessageBox.Ok
    FLAGICON = './src/ui/resources/people.png'
