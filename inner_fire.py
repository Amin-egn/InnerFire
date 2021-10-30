# internal
from src import Controller
from src.ui import MainWindow
# standard
import sys
# pyqt
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    controller = Controller(window)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
