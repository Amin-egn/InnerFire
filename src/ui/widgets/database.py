# internal
from .base_dialog import BaseDialog
from src.db import craftConnection
from src.ui.component import FireButton
# pyqt
from PyQt5.QtSql import QSqlQuery, QSqlTableModel
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

    def _connList(self):
        dataBaseInputList = [
            self.serverInput.text().strip(),
            self.usernameInput.text().strip(),
            self.passwordInput.text().strip(),
            self.dbnameInput.text().strip()
        ]
        if all(dataBaseInputList):
            self._makeConnection(dataBaseInputList)
        else:
            print('Enter all params')

    def _makeConnection(self, params):
        try:
            self.createConn = craftConnection(params)
            if self.createConn:
                self.dbRes.close()
                self.dbTbl.show()
                modelTablesName = QSqlTableModel()
                self.dbTbl.listTables.setModel(modelTablesName)
                queryTablesName = QSqlQuery("""
                    SELECT TABLE_NAME
                    FROM INFORMATION_SCHEMA.TABLES
                    WHERE TABLE_TYPE='BASE TABLE'
                """)
                modelTablesName.setQuery(queryTablesName)

        except Exception as e:
            print(str(e))

    # noinspection PyUnresolvedReferences
    def connectSignals(self):
        self.btnConnect.clicked.connect(self.connList)

    def craftStyles(self):
        self.setStyleSheet("""
            DbResponse {
                background: #fcfcfc;
            }
        """)
