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
        self.mapDict = dict()
        # self.mapDict = {
        #     'Ashkhaslist':
        #         {'Name': [2, 3],
        #          'Fname': [2],
        #          'Lname': [3],
        #          'Address': ['_Null'],
        #          'Code': ['_AutoIncrement']
        #          }
        # }

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
        self.spnMinRow = ReceiveSpin(fixText='Minimum row in excel ', minVal=1)
        self.spnMinStartIncre = ReceiveSpin(fixText='Minimum Auto-Increment ')
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

        queries = self._createQuery(table_names[0], maps)
        self._importToDb(maps, queries)

    @staticmethod
    def _createQuery(table_name, maps):
        columns = maps.keys()
        query = sql_queries.INSERT_TO_TABLE.format(
            table_name,
            ', '.join(columns),
            ', '.join(['?' for _ in range(len(columns))])
        )
        return query

    def _importToDb(self, maps, query):
        # query
        queryToTable = QSqlQuery()
        queryToTable.prepare(query)
        val, auto_increment = None, self.spnMinStartIncre.value()

        # f_name = r'./mehrabi.xlsx'
        # book = load_workbook(filename=f_name)
        # sheet = book.active

        for row in self.ui.entrance.sheet.iter_rows(min_row=self.spnMinRow.value(),
                                                    values_only=self.chkValues.isChecked()):
            bind_list = list()
            for key, value in maps.items():
                if len(value) > 1:
                    val = ''
                    for i in value:
                        val = f'{val} {str(row[i])}'
                else:
                    if value[0] == '_AutoIncrement':
                        auto_increment += 1
                        val = auto_increment
                    elif value[0] == '_Null':
                        val = 'null'
                    else:
                        val = row[value[0]]
                bind_list.append(val)

            for bind in bind_list:
                queryToTable.addBindValue(bind)

            if queryToTable.exec():
                level = 1
            else:
                level = 0
            self._messageLabel(bind_list, level)

    def _connectSignals(self):
        self.btnCast.clicked.connect(self._analyzeAndVerify)

    def _craftStyle(self):
        self.setStyleSheet("""
            #Table {
                background: #fcfcfc;
                border: 2px dot-dash #33892a;
            }
        """)
