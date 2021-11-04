# internal
from src.db import CreateConnection
from src.ui.component import TableModel
# pyqt
from PyQt5.QtSql import QSqlQuery, QSqlTableModel


class View(object):
    """View"""
    def __init__(self, ui):
        self.ui = ui
        self.dbRes = self.ui.dbResponse
        self.dbTbl = self.ui.dbTable
        self.btnDbConnection = self.dbRes.btnConnect
        self.connectSignals()

    def dbRes_handler(self):
        conn_params = self.dbRes.inputList

        if all(conn_params):
            self.createConn = CreateConnection(conn_params)
            self.dbRes.close()
            self.dbTbl.show()
            self.model = QSqlTableModel()
            self.dbTbl.listTables.setModel(self.model)
            self.query = QSqlQuery("""
                SELECT TABLE_NAME
                FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_TYPE='BASE TABLE'
            """)
            self.model.setQuery(self.query)

    def connectSignals(self):
        self.btnDbConnection.clicked.connect(self.dbRes_handler)
