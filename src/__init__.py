# internal
from src.view import View


class Controller(object):
    """Controller"""
    def __init__(self, ui):
        self.ui = ui
        self.view = View(self.ui)
