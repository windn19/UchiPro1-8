from PyQt5.QtSql import QSqlDatabase


con = QSqlDatabase.addDatabase('QSQLITE', 'con')
con.setDatabaseName('contact.db')

print(con.databaseName())
print(con.connectionName())

print(con.open())
print(con.isOpen())