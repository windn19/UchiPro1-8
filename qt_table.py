import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery


con = QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('contact.db')

if not con.open():
    print(f'Database Error: {con.lastError().databaseText()}')
    sys.exit(1)
createTableQuery = QSqlQuery()
createTableQuery.exec(
    '''
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )
    '''
)

print(con.tables())