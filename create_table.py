import sqlite3


con = sqlite3.connect('base.db')
cur = con.cursor()

with open('create_table.sql') as f:
    sql_request = f.read()
    
cur.executescript(sql_request)
con.commit()


con.close()