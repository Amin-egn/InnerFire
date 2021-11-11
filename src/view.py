# internal
from src.db import craftConnection
from src.ui.component import TableModel, DrgDrpTable
# pyqt
from PyQt5.QtSql import QSqlQuery, QSqlTableModel


class View(object):
    """View"""
    def __init__(self, ui):
        self.ui = ui
        self.front = self.ui.frontWidget
        self.exlRes = self.ui.excelResponse
        self.dbRes = self.ui.dbResponse
        self.dbTbl = self.ui.dbTable
        self.dbTtl = self.ui.dbTableTitles
        # connections
        # - button in front
        # -- excel
        self.btnExcelShow = self.front.btnExcel
        # -- database
        self.btnDbShow = self.front.btnDb
        # - button in exlRes
        self.btnExlDoneConnection = self.exlRes.btnDone
        # - button in dbRes
        self.btnDbConnection = self.dbRes.btnConnect
        # - button in dbTbl
        self.btnTblDoneConnection = self.dbTbl.btnDone
        # connect signals
        self.connectSignals()

    def openExcel_handler(self):
        try:
            if self.exlRes.openExcel():
                self.exlRes.show()

        except Exception as e:
            print(str(e))

    def exlRes_to_table_handler(self):
        self.checkedItems = list()
        for i in sorted(self.exlRes.modelExcel.checkList):
            self.checkedItems.append(self.exlRes.modelExcel.items[i])

        self.modelDrgDrp = DrgDrpTable(['Excel Titles'], self.checkedItems)
        self.front.tableWidget.setModel(self.modelDrgDrp)

    def dbRes_handler(self):
        conn_params = self.dbRes.inputList

        if all(conn_params):
            try:
                self.createConn = craftConnection(conn_params)
                if self.createConn:
                    self.dbRes.close()
                    self.dbTbl.show()
                    self.modelConn = QSqlTableModel()
                    self.dbTbl.listTables.setModel(self.modelConn)
                    self.queryConn = QSqlQuery("""
                        SELECT TABLE_NAME
                        FROM INFORMATION_SCHEMA.TABLES
                        WHERE TABLE_TYPE='BASE TABLE'
                    """)
                    self.modelConn.setQuery(self.queryConn)
            except Exception as e:
                print(str(e))


    def table_titles_handler(self):
        indexes = self.dbTbl.listTables.selectedIndexes()
        index = indexes[0].row() if indexes else None
        if index is not None:
            try:
                self.dbTbl.close()
                self.dbTtl.show()
                self.modelTitle = QSqlTableModel()
                self.dbTtl.listTitles.setModel(self.modelTitle)
                self.queryTable = QSqlQuery(f"""
                    SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = '{index}'
                """)
                self.modelTitle.setQuery(self.queryTable)
            except Exception as e:
                print(str(e))

    def connectSignals(self):
        self.btnExcelShow.clicked.connect(self.openExcel_handler)
        self.btnExlDoneConnection.clicked.connect(self.exlRes_to_table_handler)
        self.btnDbConnection.clicked.connect(self.dbRes_handler)
        self.btnTblDoneConnection.clicked.connect(self.table_titles_handler)
