# standard
from .base import BaseWidget
from src.ui.component import FireButton
# pyqt
from PyQt5.QtWidgets import QLabel, QFrame, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout


class InnerImport(BaseWidget):
    """Inner Import"""
    def _craftWidget(self):
        self._guide()
        self._checkOptions()
        self._monitoring()

    def _guide(self):
        text = 'NOTE! \n' \
               'This might not be rollback \n' \
               'Please check everything before cast'
        self.lblGuide = QLabel(text)
        # attach
        self.generalLayout.addWidget(self.lblGuide)

    def _checkOptions(self):
        # widget
        self.checkOptionsWidget = QWidget(self)
        # layout
        self.checkOptionLayout = QHBoxLayout()
        self.checkOptionsWidget.setLayout(self.checkOptionLayout)
        # check options
        # - layout
        self.checksGridLayout = QGridLayout()
        # button
        self.btnCast = FireButton('Cast !')
        # attach
        # - main
        self.checkOptionLayout.addLayout(self.checksGridLayout)
        self.checkOptionLayout.addWidget(self.btnCast)
        # - general
        self.generalLayout.addWidget(self.checkOptionsWidget)

    def _monitoring(self):
        # frame
        self.monitorFrame = QFrame(self)
        self.monitorFrame.setMinimumSize(560, 300)
        self.monitorFrame.setObjectName('Table')
        # layout
        self.monitorLayout = QVBoxLayout()
        self.monitorFrame.setLayout(self.monitorLayout)
        # attach
        # - general
        self.generalLayout.addWidget(self.monitorFrame)

    def _progressBar(self):
        pass

    def _craftStyle(self):
        self.setStyleSheet("""
            #Table {
                border: 2px dot-dash #33892a;
            }
        """)
