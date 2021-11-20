# pyqt
from PyQt5.QtSql import QSqlDatabase


def craftConnection(params):
    conn = QSqlDatabase.addDatabase(
        'QODBC',
        'qt_sql_default_connection'
    )
    serverName = params[0]
    userName = params[1]
    passWord = params[2]
    dbName = params[3]
    conn.setDatabaseName(
        f'driver={{SQL Server}};'
        f'server={serverName};'
        f'database={dbName};'
        f'uid={userName};'
        f'pwd={passWord}'
    )
    return conn.open(), conn
