import sqlite3

con = sqlite3.connect('base.db')

cur = con.cursor()

text_sql = '''
select ved.id, ved.family, deps.title from ved join deps on ved.id_deb = deps.id_deb
'''

text_sql1 = '''
select ved.id, ved.family, deps.title, city.name 
from ved
 join deps on ved.id_deb = deps.id_deb
  join city on deps.id_city = city.id
'''

cur.execute(text_sql1)
for row in cur.fetchall():
    print(row)


con.commit()

con.close()