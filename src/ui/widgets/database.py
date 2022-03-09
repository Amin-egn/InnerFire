# internal
from .base import BaseWidget
from .base_dialog import BaseDialog
from src.db import craftConnection
from src import sql_queries
from src.ui.component import (FireButton, ReceiveInput, TableView, ListView,
                              RemoveButton, SingleDimensionTableModel, AddButton,
                              WarningMessage, InfoMessage, SimpleButton, LockedTableView)
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
        self.setWindowUnits('Database', ':/icons/database')
        self.setFixedWidth(480)
        self.dataDict = self.ui.dbDataCollectorDict
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
        self.dbTitles.fillDataDict()
        self.ui.createDbTable(list(self.dataDict.keys()), list(self.dataDict.values()))

        self.ui.unlockNextStage()
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
            msg_params = WarningMessage('Enter all require parameters', self)
            msg_params.exec()

    def _makeConnection(self, params):
        error = None
        if craftConnection(params):
            modelTablesName = QSqlTableModel()
            self.ui.dbTables.proxyModel.setSourceModel(modelTablesName)
            queryTablesName = QSqlQuery()
            queryTablesName.prepare(sql_queries.TABLES_NAME)
            if queryTablesName.exec():
                modelTablesName.setQuery(queryTablesName)
                # ToDo -> check for conflict in settings.json
                settings.s('servername', self.serverInput.text().strip())
                settings.s('username', self.usernameInput.text().strip())
                settings.s('databasename', self.dbnameInput.text().strip())
                settings.save()
                self.ui.menuHandler(1)

            else:
                error = 'Cannot connect to database please check parameters correctness'
                print(queryTablesName.lastError())

        else:
            error = 'Cannot connect to database'

        if error:
            msg_err = WarningMessage(error, self)
            msg_err.exec()

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
        self._topLayout()
        # tables list
        # - proxy
        self.proxyModel = QSortFilterProxyModel(self)
        # - view
        self.listTablesName = TableView(self.proxyModel)
        # - sql model
        self.tableTitleSqlModel = QSqlTableModel()
        # table name
        self.table_name = ''
        # done button
        self.btnDoneLayout = QHBoxLayout()
        self.btnDoneLayout.setAlignment(Qt.AlignHCenter)
        self.btnSelect = FireButton('Select')
        # attach
        # - main
        self.btnDoneLayout.addWidget(self.btnSelect)
        # - general
        self.generalLayout.addWidget(self.listTablesName)
        self.generalLayout.addLayout(self.btnDoneLayout)

    def _topLayout(self):
        # layout
        self.topLayout = QHBoxLayout()
        # search bar
        self.searchInput = ReceiveInput(placeHolder='Search table\'s name')
        # back button
        # ToDo -> if user renewed connection, all selection would be clear
        self.btnBack = SimpleButton(icon=':/icons/back_arrow', size=(29, 29))
        self.btnBack.setToolTip('Connect to new Database')
        self.btnBack.setDisabled(True)
        # attach
        # - main
        self.topLayout.addWidget(self.searchInput)
        self.topLayout.addWidget(self.btnBack)
        # - general
        self.generalLayout.addLayout(self.topLayout)

    def _searchHandler(self, text):
        self.proxyModel.setFilterRegExp(str(text))

    def _fetchTitlesFromTable(self):
        self.selected_table = self.listTablesName.index(True)
        error, info = None, None
        if self.selected_table:
            self.tableTitleSqlModel.clear()
            queryTableTitles = QSqlQuery()
            queryTableTitles.prepare(sql_queries.COLUMNS_NAME)
            queryTableTitles.addBindValue(self.selected_table)

            if queryTableTitles.exec():
                self.tableTitleSqlModel.setQuery(queryTableTitles)
                self.table_name = self.selected_table
                self.ui.dbTitles.reset()
                self.ui.menuHandler(2)

            else:
                error = 'Something went wrong! Please check logs'
                print(queryTableTitles.lastError())

        else:
            info = 'Please choose a table'

        if error:
            msg_err = WarningMessage(error, self)
            msg_err.exec()

        if info:
            msg_info = InfoMessage(info, self)
            msg_info.exec()

    # noinspection PyUnresolvedReferences
    def _connectSignals(self):
        # search box
        self.searchInput.textChanged.connect(self._searchHandler)
        # done button
        self.btnSelect.clicked.connect(self._fetchTitlesFromTable)
        # back button
        self.btnBack.clicked.connect(lambda: self.ui.menuHandler(0))

    def _craftStyles(self):
        self.setStyleSheet("""
            DbTables {
                background: #fcfcfc;
            }
        """)


class DbTableTitles(BaseWidget):
    """Database Table Titles"""
    def _initialize(self):
        # table name
        self.selectedTableName = self.ui.dbTables.table_name
        # selected title list
        self.selectedTitleList = list()
        if self.selectedTableName:
            self.selectedTitleTableModel.header = [self.selectedTableName]
            self.selectedTitleTableModel.clearRecords()

        if self.selectedTableName in self.ui.dataDict.keys():
            self.selectedTitleList = self.ui.dataDict[self.selectedTableName]
            self.selectedTitleTableModel.setRecords(self.selectedTitleList)

    def _craftWidget(self):
        self._topLayout()
        self._dbModelView()
        self._buttons()

    def _topLayout(self):
        # layout
        self.topLayout = QHBoxLayout()
        # search bar
        self.searchInput = ReceiveInput(placeHolder='Search title\'s name')
        # back button
        self.btnBack = SimpleButton(icon=':/icons/back_arrow', size=(29, 29))
        self.btnBack.setToolTip('Back to select Table')
        # attach
        # - main
        self.topLayout.addWidget(self.searchInput)
        self.topLayout.addWidget(self.btnBack)
        # - general
        self.generalLayout.addLayout(self.topLayout)

    def _searchHandler(self, text):
        self.proxyModel.setFilterRegExp(str(text))

    def _dbModelView(self):
        # layout
        self.modelViewLayout = QHBoxLayout()
        # list
        # - proxy
        self.proxyModel = QSortFilterProxyModel(self)
        self.proxyModel.setSourceModel(self.ui.dbTables.tableTitleSqlModel)
        # - view
        self.titlesListView = ListView(self.proxyModel)
        # table
        # - model
        self.selectedTitleTableModel = SingleDimensionTableModel([self.selectedTableName])
        # - view
        self.selectedTitleTableView = LockedTableView(self.selectedTitleTableModel)
        # attach
        # - main
        self.modelViewLayout.addWidget(self.selectedTitleTableView)
        self.modelViewLayout.addWidget(self.titlesListView)
        # - general
        self.generalLayout.addLayout(self.modelViewLayout)

    def _buttons(self):
        # layout
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setAlignment(Qt.AlignRight)
        # add button
        self.btnAdd = AddButton('Add')
        # remove button
        self.btnRemove = RemoveButton('Remove')
        # attach
        # - main
        self.buttonLayout.addWidget(self.btnAdd)
        self.buttonLayout.addWidget(self.btnRemove)
        # - general
        self.generalLayout.addLayout(self.buttonLayout)

    def _innerToMainTable(self, status):
        # ToDo -> redo here and user must can remove from table model
        selected_row = self.titlesListView.index(True)
        if status == 'add':
            if selected_row not in self.selectedTitleList:
                self.selectedTitleList.append(selected_row)

        else:
            if selected_row in self.selectedTitleList:
                self.selectedTitleList.remove(selected_row)

        self.selectedTitleTableModel.setRecords(self.selectedTitleList)

    def fillDataDict(self):
        if self.selectedTitleList:
            self.ui.dataDict[self.selectedTableName] = self.selectedTitleList
        else:
            if self.selectedTableName in self.ui.dataDict.keys():
                del self.ui.dataDict[self.selectedTableName]

    def _backToTablesName(self):
        self.fillDataDict()
        self.ui.menuHandler(1)

    # noinspection PyUnresolvedReferences
    def _connectSignals(self):
        # search box
        self.searchInput.textChanged.connect(self._searchHandler)
        # button done
        self.btnAdd.clicked.connect(lambda: self._innerToMainTable('add'))
        # button remove
        self.btnRemove.clicked.connect(lambda: self._innerToMainTable('remove'))
        # button back
        self.btnBack.clicked.connect(self._backToTablesName)

    def _craftStyles(self):
        self.setStyleSheet("""
            DbTableTitles {
                background: #fcfcfc;
            }
        """)
