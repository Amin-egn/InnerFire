# internal
from src.db import CreateConnection
from src.ui.component import TableModel
# pyqt
from PyQt5.Qt import QModelIndex
from PyQt5.QtSql import QSqlQuery, QSqlTableModel


class View(object):
    """View"""
    def __init__(self, ui):
        self.ui = ui
        self.exlRes = self.ui.excelResponse
        self.dbRes = self.ui.dbResponse
        self.dbTbl = self.ui.dbTable
        self.dbTtl = self.ui.dbTitles
        # connections
        # - button in exlRes
        self.btnExlDoneConnection = self.exlRes.btnDone
        # - button in dbRes
        self.btnDbConnection = self.dbRes.btnConnect
        # - button in dbTbl
        self.btnTblDoneConnection = self.dbTbl.btnDone
        # connect signals
        self.connectSignals()

    def dbRes_handler(self):
        conn_params = self.dbRes.inputList

        if all(conn_params):
            try:
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
            except Exception as e:
                print(str(e))

    def exlRes_emit_table(self):
        for k, v in self.exlRes.model.checks.items():
            print(f'{k} -> {v}')

    def table_titles_handler(self):
        indexes = self.listTables.selectedIndexes()
        index = indexes[0] if indexes else None
        if index is not None:
            pass

        self.dbTbl.close()
        self.dbTtl.show()

    def connectSignals(self):
        self.btnExlDoneConnection.clicked.connect(self.exlRes_emit_table)
        self.btnDbConnection.clicked.connect(self.dbRes_handler)
        self.btnTblDoneConnection.clicked.connect(self.table_titles_handler)
