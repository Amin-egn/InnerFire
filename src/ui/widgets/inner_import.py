# internal
from .base import BaseWidget
from src.ui.component import FireButton, ReceiveSpin, MessageLabel
from src import sql_queries
# pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QFrame, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout, QCheckBox,
                             QScrollArea, QProgressBar)
from PyQt5.QtSql import QSqlQuery


class InnerImport(BaseWidget):
    """Inner Import"""
    def _initialize(self):
        # self.mapDict = dict()
        self.mapDict = {
            'Ashkhaslist':
                {'Name': [1, 2],
                 'Fname': [2],
                 'Lname': [1],
                 'Address': ['_Null'],
                 'Code': ['_AutoIncrement']
                 }
        }

    def _craftWidget(self):
        self._guide()
        self._checkOptions()
        self._monitoring()
        self._progressBar()

    def _guide(self):
        text = 'NOTE! \n' \
               'This might not be rollback \n' \
               'Please check everything before cast'
        self.lblGuide = QLabel(text)
        # attach
        self.generalLayout.addWidget(self.lblGuide)

    def _checkOptions(self):
        # widget
        self.checkOptionsWidget = QWidget(self)
        # layout
        self.checkOptionsLayout = QHBoxLayout()
        self.checkOptionsWidget.setLayout(self.checkOptionsLayout)
        # check options
        # - layout
        self.checksGridLayout = QGridLayout()
        # - checkboxes
        # -- spinboxes
        self.spnMinRow = ReceiveSpin()
        self.spnMinStartIncre = ReceiveSpin()
        # -- checkboxes
        self.chkValues = QCheckBox('Values', self)
        self.chkValues.setChecked(True)
        # button
        self.btnCast = FireButton('Cast !')
        # attach
        # - grid
        self.checksGridLayout.addWidget(self.chkValues, 0, 0)
        self.checksGridLayout.addWidget(self.spnMinRow, 1, 0)
        self.checksGridLayout.addWidget(self.spnMinStartIncre, 1, 1)
        # - main
        self.checkOptionsLayout.addLayout(self.checksGridLayout)
        self.checkOptionsLayout.addWidget(self.btnCast)
        # - general
        self.generalLayout.addWidget(self.checkOptionsWidget)

    def _monitoring(self):
        # scroll
        self.scroll = QScrollArea(self)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setObjectName('Table')
        self.scroll.setMinimumSize(560, 300)
        # frame
        self.monitorFrame = QFrame(self)
        self.scroll.setWidget(self.monitorFrame)
        # layout
        self.monitorLayout = QVBoxLayout()
        self.monitorFrame.setLayout(self.monitorLayout)
        # attach
        # - general
        self.generalLayout.addWidget(self.scroll)

    def _messageLabel(self, message, level):
        self.monitorLayout.insertWidget(0, MessageLabel(message, level))

    def _progressBar(self):
        self.progressBar = QProgressBar()
        # self.generalLayout.addWidget(self.progressBar)

    def _analyzeAndVerify(self):
        table_names, maps = [], {}
        for key, value in self.mapDict.items():
            table_names.append(key)
            maps.update(value)

        # self._importToDb()
        self._createQuery(table_names[0], maps)

    def _createQuery(self, table_name, map):
        columns = map.keys()
        query = sql_queries.INSERT_TO_TABLE.format(
            table_name,
            ', '.join(columns),
            ', '.join(['?' for _ in range(len(columns))])
        )

        print(query)

    def _importToDb(self, table_name, map):
        # query
        queryToTable = QSqlQuery()


            # query_insert = sql_queries.INSERT_TO_TABLE.format(
            #     table,
            #     ', '.join(columns),
            #     ', '.join(['?' for _ in range(len(columns))])
            # )
            # queryToTable.prepare(query_insert)
            #
            # for row in self.ui.entrance.sheet.iter_rows(min_row=self.spnMinRow.value(),
            #                                             values_only=self.chkValues.isChecked()):




        # table_cols = self.mapDict.keys()
        # cols_range = len(table_cols)
        # cols_name = ', '.join(table_cols)
        #
        # query_insert = sql_queries.INSERT_TO_TABLE.format(
        #     self.ui.entrance.dbName,
        #     cols_name,
        #     ', '.join(['?' for _ in range(cols_range)])
        # )
        # queryToTable.prepare(query_insert)
        #
        # for row in self.ui.entrance.sheet.iter_rows(min_row=self.spnMinRow.value(),
        #                                             values_only=self.chkValues.isChecked()):
        #     for col in table_cols:
        #         queryToTable.addBindValue(row[self.mapDict[col][0]])
        #
        #     queryToTable.exec()

    def _connectSignals(self):
        self.btnCast.clicked.connect(self._analyzeAndVerify)

    def _craftStyle(self):
        self.setStyleSheet("""
            #Table {
                background: #fcfcfc;
                border: 2px dot-dash #33892a;
            }
        """)
