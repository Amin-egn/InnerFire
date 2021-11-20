# internal
from src.db import craftConnection
from src.ui.component import TableModel, DrgDrpTable
# pyqt
from PyQt5.QtCore import QItemSelectionModel
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtSql import QSqlQuery, QSqlTableModel


class View(object):
    """View"""
    def __init__(self, ui):
        self.ui = ui
        self.assemble = self.ui.assembleWidget
        self.exlRes = self.ui.excelResponse
        self.dbRes = self.ui.dbResponse
        self.dbTbl = self.ui.dbTable
        self.dbTtl = self.ui.dbTableTitles
        # connections
        # - button in front
        # -- excel
        self.btnExcelShow = self.assemble.btnExcel
        # -- database
        self.btnDbShow = self.assemble.btnDb
        # - button in exlRes
        self.btnExlDoneConnection = self.exlRes.btnDone
        # - button in dbRes
        self.btnDbConnection = self.dbRes.btnConnect
        # - button in dbTbl
        self.btnTblDoneConnection = self.dbTbl.btnDone
        # connect signals
        self.connectSignals()

    def openExcel_handler(self):
        """choose excel file """
        try:
            if self.exlRes.openExcel():
                self.exlRes.show()

        except Exception as e:
            print(str(e))

    def exlRes_to_table_handler(self):
        """load excel titles and insert to table"""
        self.checkedItems = list()
        for i in sorted(self.exlRes.modelExcel.checkList):
            self.checkedItems.append(self.exlRes.modelExcel.items[i])

        self.modelDrgDrp = DrgDrpTable(['Excel Titles'], self.checkedItems)
        self.assemble.tableWidget.setModel(self.modelDrgDrp)

    def dbRes_handler(self):
        """connect to database"""
        conn_params = self.dbRes.inputList

        if all(conn_params):
            try:
                self.createConn = craftConnection(conn_params)
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


    def table_titles_handler(self):
        """get all columns of chosen table"""
        indexes = self.dbTbl.listTables.selectedIndexes()
        index = indexes[0].data() if indexes else None
        print(index)
        if index is not None:
            try:
                self.dbTbl.close()
                self.dbTtl.show()
                modelTitle = QSqlTableModel()
                queryTableTitles = QSqlQuery()
                self.dbTtl.listTitles.setModel(modelTitle)
                queryTableTitles.prepare("""
                    SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = ?
                """)
                queryTableTitles.addBindValue(index)
                queryTableTitles.exec()
                modelTitle.setQuery(queryTableTitles)

            except Exception as e:
                print(str(e))

    def connectSignals(self):
        # open excel
        self.btnExcelShow.clicked.connect(self.openExcel_handler)
        # open database
        self.btnDbShow.clicked.connect(self.dbRes.show)
        # connect to sql server
        self.btnExlDoneConnection.clicked.connect(self.exlRes_to_table_handler)
        # get all tables
        self.btnDbConnection.clicked.connect(self.dbRes_handler)
        # get all table columns
        self.btnTblDoneConnection.clicked.connect(self.table_titles_handler)
