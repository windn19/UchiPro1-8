import sqlite3


con = sqlite3.connect('base.db')

cur = con.cursor()

data = [("Иванов", "Начальник", 15, 1000), ("Петров", "Инженер", 15, 500), ("Сидоров", "Менеджер", 10, 700)]
data_deb = [(15, 1, 'Производственный отдел'), (10, 2, 'Отдел продаж')]
data_city = [('Минск',), ('Москва',)]

cur.executemany("INSERT INTO ved (family, job, id_deb, salary) VALUES(?, ?, ?, ?)", data)
# con.commit()

cur.executemany("INSERT INTO deps VALUES(?, ?, ?)", data_deb)
# con.commit()

cur.executemany("INSERT INTO city (name) VALUES(?)", data_city)
con.commit()

con.close()