# pyqt
from PyQt5.QtSql import QSqlDatabase


class CreateConnection(object):
    def __init__(self, l):
        self.l = l
        self.conn = QSqlDatabase.addDatabase('QODBC', 'qt_sql_default_connection')
        self.craftConnection()

    def craftConnection(self):
        self.serverName = self.l[0]
        self.userName = self.l[1]
        self.password = self.l[2]
        self.dbName = self.l[3]

        self.conn.setDatabaseName(
            f'driver={{SQL Server}};'
            f'server={self.serverName};'
            f'database={self.dbName};'
            f'uid={self.userName};'
            f'pwd={self.password}'
        )
        return self.conn.open()
