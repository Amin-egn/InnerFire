# standard
import sys
# internal
# noinspection PyUnresolvedReferences
from src.ui import resources
from src.ui import MainWindow
# pyqt
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
