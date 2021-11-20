# internal
from src.ui.component import BaseDialog, FireButton
# pyqt
from PyQt5.QtWidgets import QLineEdit, QFormLayout, QHBoxLayout


class DbResponse(BaseDialog):
    """Database Responsible"""
    def craftDialog(self):
        # self modification
        self.setFixedWidth(380)
        self.setWindowTitle('Data-base Information')
        # form layout
        self.dataBaseLayout = QFormLayout()
        # inputs
        self.serverInput = QLineEdit(text='.\\')
        self.usernameInput = QLineEdit(text='sa')
        self.passwordInput = QLineEdit(echoMode=QLineEdit.EchoMode.Password)
        self.dbnameInput = QLineEdit()
        # add widgets
        self.dataBaseLayout.addRow('Server:', self.serverInput)
        self.dataBaseLayout.addRow('Username:', self.usernameInput)
        self.dataBaseLayout.addRow('Password:', self.passwordInput)
        self.dataBaseLayout.addRow('Database name:', self.dbnameInput)
        # button layout
        self.btnLayout = QHBoxLayout()
        self.btnLayout.setContentsMargins(0, 10, 0, 0)
        self.btnConnect = FireButton('Connect')
        # attach
        self.btnLayout.addWidget(self.btnConnect)
        self.generalLayout.addLayout(self.dataBaseLayout)
        self.generalLayout.addLayout(self.btnLayout)

    def connList(self):
        self.inputList = [
            self.serverInput.text().strip(),
            self.usernameInput.text().strip(),
            self.passwordInput.text().strip(),
            self.dbnameInput.text().strip()
        ]
        return self.inputList

    def connectSignals(self):
        self.btnConnect.clicked.connect(self.connList)

    def craftStyles(self):
        self.setStyleSheet("""
            DbResponse {
                background: #fcfcfc;
            }
        """)
