# tables name
TABLES_NAME = """
    SELECT TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_TYPE='BASE TABLE'
"""

# get columns name
COLUMNS_NAME = """
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = ?
"""

# get columns auto increment
COLUMNS_PRIMARY_KEY = """
    SELECT OBJECT_SCHEMA_NAME(object_id) + '.' + OBJECT_NAME(object_id), name
    FROM sys.identity_columns
    WHERE OBJECT_NAME(object_id) = ?;
"""

# insert values
INSERT_TO_TABLE = """
    INSERT INTO {} ({})
    VALUES ({})
"""
