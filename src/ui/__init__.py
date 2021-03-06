# internal
from src.ui import widgets
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QStackedLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # bootstrap
        self._bootstrap()
        # connect signal
        self._connectSignals()
        # stylesheet
        self._craftStyle()

    def _bootstrap(self):
        self.setWindowTitle('Inner Fire')
        self.setMinimumSize(600, 480)
        self.setWindowIcon(QIcon(':/icons/logo'))
        # central widget
        self._mainWidget = QWidget(self)
        self.setCentralWidget(self._mainWidget)
        # general layout
        self.generalLayout = QStackedLayout()
        self.generalLayout.setAlignment(Qt.AlignTop)
        self._mainWidget.setLayout(self.generalLayout)
        self._widgetsInstance()
        self.widgetsHandler()

    def _widgetsInstance(self):
        # Entrance
        self.entrance = widgets.Entrance(self)
        # WarpWoof
        self.warpWoof = widgets.WarpWoof(self)
        # InnerImport
        self.innerImport = widgets.InnerImport(self)
        # attach
        self.generalLayout.addWidget(self.entrance)
        self.generalLayout.addWidget(self.warpWoof)
        self.generalLayout.addWidget(self.innerImport)

    def widgetsHandler(self, index=0):
        self.generalLayout.setCurrentIndex(index)

    def _connectSignals(self):
        self.entrance.btnNextStage.clicked.connect(lambda: self.widgetsHandler(1))
        self.warpWoof.btnNextStage.clicked.connect(lambda: self.widgetsHandler(2))

    def _craftStyle(self):
        self.setStyleSheet("""
            MainWindow {
                background: #fcfcfc;
            }
        """)
