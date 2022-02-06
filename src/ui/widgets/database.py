# internal
from .base import BaseWidget
from .base_dialog import BaseDialog
from src.db import craftConnection
from src.ui.component import FireButton, ReceiveInput, TableView, ListView, RemoveButton, SingleDimensionTableModel
from src import settings
# pyqt
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.Qt import QSortFilterProxyModel
from PyQt5.QtSql import QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QFormLayout, QHBoxLayout, QStackedLayout


class DbResponse(BaseDialog):
    """Database Responsible"""
    def _craftLayout(self):
        self.generalLayout = QStackedLayout()
        self.generalLayout.setContentsMargins(5, 10, 5, 0)
        self.generalLayout.setAlignment(Qt.AlignVCenter)
        self.setLayout(self.generalLayout)

    def _craftDialog(self):
        self.setWindowTitle('Database')
        self.setFixedWidth(420)
        self._widgetInstances()
        self.menuHandler(0)

    def _widgetInstances(self):
        self.dbConn = DbConnection(self)
        self.dbTables = DbTablesName(self)
        self.dbTitles = DbTableTitles(self)
        self.widgetList = [self.dbConn, self.dbTables, self.dbTitles]

        for wid in self.widgetList:
            self.generalLayout.addWidget(wid)

    def menuHandler(self, index):
        self.generalLayout.setCurrentIndex(index)
        # animation
        self.animationOpacity = QPropertyAnimation(self, b'windowOpacity')
        self.animationOpacity.setStartValue(0.)
        self.animationOpacity.setEndValue(1.)
        self.animationOpacity.setDuration(600)
        self.animationOpacity.start()

    def closeEvent(self, event):
        if self.dbTitles.dbTitleTableModel.isEmpty():
            self.dbTitles.dbTitleTableView.deleteLater()

        self.close()


class DbConnection(BaseWidget):
    """Database Connection"""
    def _craftWidget(self):
        # form layout
        self.dataBaseLayout = QFormLayout()
        # inputs
        self.serverInput = ReceiveInput(text=settings.g('servername'))
        self.usernameInput = ReceiveInput(text=settings.g('username'))
        self.passwordInput = ReceiveInput(password=True)
        self.dbnameInput = ReceiveInput(text=settings.g('databasename'))
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
                modelTablesName = QSqlTableModel()
                self.ui.dbTables.proxyModel.setSourceModel(modelTablesName)
                queryTablesName = QSqlQuery()
                queryTablesName.prepare("""
                    SELECT TABLE_NAME
                    FROM INFORMATION_SCHEMA.TABLES
                    WHERE TABLE_TYPE='BASE TABLE'
                """)
                queryTablesName.exec_()
                modelTablesName.setQuery(queryTablesName)

        except Exception as e:
            print(str(e))

        else:
            settings.s('servername', self.serverInput.text().strip())
            settings.s('username', self.usernameInput.text().strip())
            settings.s('databasename', self.dbnameInput.text().strip())
            settings.save()
            self.ui.menuHandler(1)

    # noinspection PyUnresolvedReferences
    def _connectSignals(self):
        self.btnConnect.clicked.connect(self._connList)

    def _craftStyles(self):
        self.setStyleSheet("""
            DbConnection {
                background: #fcfcfc;
            }
        """)



class DbTablesName(BaseWidget):
    """Database Tables"""
    def _craftWidget(self):
        # search bar
        self.searchInput = ReceiveInput(placeHolder='Search table\'s name')
        # tables list
        self.proxyModel = QSortFilterProxyModel(self)
        self.listTablesName = TableView(self.proxyModel)
        # done button
        self.btnDoneLayout = QHBoxLayout()
        self.btnDoneLayout.setAlignment(Qt.AlignHCenter)
        self.btnDone = FireButton('Done')
        # attach
        self.btnDoneLayout.addWidget(self.btnDone)
        # - general
        self.generalLayout.addWidget(self.searchInput)
        self.generalLayout.addWidget(self.listTablesName)
        self.generalLayout.addLayout(self.btnDoneLayout)

    def _searchHandler(self, text):
        self.proxyModel.setFilterRegExp(str(text))

    def _fetchTitlesFromTable(self):
        selected_index = self.listTablesName.index(True)
        if selected_index is not None:
            try:
                modelTableTitles = QSqlTableModel()
                self.ui.dbTitles.proxyModel.setSourceModel(modelTableTitles)
                queryTableTitles = QSqlQuery()
                queryTableTitles.prepare("""
                    SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = ?
                """)
                queryTableTitles.addBindValue(selected_index)
                queryTableTitles.exec()
                modelTableTitles.setQuery(queryTableTitles)

            except Exception as e:
                print(str(e))

            else:
                self.ui.menuHandler(2)

    # noinspection PyUnresolvedReferences
    def _connectSignals(self):
        # search box
        self.searchInput.textChanged.connect(self._searchHandler)
        # done button
        self.btnDone.clicked.connect(self._fetchTitlesFromTable)

    def _craftStyles(self):
        self.setStyleSheet("""
            DbTables {
                background: #fcfcfc;
            }
        """)


class DbTableTitles(BaseWidget):
    """Database Table Titles"""
    def _craftWidget(self):
        # search bar
        self.searchInput = ReceiveInput(placeHolder='Search title\'s name')
        # proxy model
        self.proxyModel = QSortFilterProxyModel(self)
        # title
        self.listTablesTitles = ListView(self.proxyModel)
        # selected title list
        self.listTitleName = list()
        # table model
        self.dbTitleTableModel = SingleDimensionTableModel(['Table Titles'])
        # table view
        self.dbTitleTableView = TableView(self.dbTitleTableModel)
        # done button
        self.btnDoneLayout = QHBoxLayout()
        self.btnDoneLayout.setAlignment(Qt.AlignHCenter)
        self.btnDone = FireButton('Add')
        # remove butoon
        self.btnRemoveLayout = QHBoxLayout()
        self.btnRemoveLayout.setAlignment(Qt.AlignHCenter)
        self.btnRemove = RemoveButton('Remove')
        # attach
        # - button layout
        self.btnDoneLayout.addWidget(self.btnDone)
        # - remove layout
        self.btnRemoveLayout.addWidget(self.btnRemove)
        # - general
        self.generalLayout.addWidget(self.searchInput)
        self.generalLayout.addWidget(self.listTablesTitles)
        self.generalLayout.addLayout(self.btnDoneLayout)
        self.generalLayout.addLayout(self.btnRemoveLayout)
        # - entrance
        self.ui.ui.modelsLayout.addWidget(self.dbTitleTableView)

    def _searchHandler(self, text):
        self.proxyModel.setFilterRegExp(str(text))

    def _innerToMainTable(self, status):
        selected_row = self.listTablesTitles.index(True)
        if status == 'add':
            if selected_row not in self.listTitleName:
                self.listTitleName.append(selected_row)

        else:
            if selected_row in self.listTitleName:
                self.listTitleName.remove(selected_row)

        self.dbTitleTableModel.setRecords(self.listTitleName)
        self.dbTitleTableModel.layoutChanged.connect(self.ui.ui.checkWidgetNumbers)

    # noinspection PyUnresolvedReferences
    def _connectSignals(self):
        # search box
        self.searchInput.textChanged.connect(self._searchHandler)
        # button done
        self.btnDone.clicked.connect(lambda: self._innerToMainTable('add'))
        # button remove
        self.btnRemove.clicked.connect(lambda: self._innerToMainTable('remove'))

    def _craftStyles(self):
        self.setStyleSheet("""
            DbTableTitles {
                background: #fcfcfc;
            }
        """)
