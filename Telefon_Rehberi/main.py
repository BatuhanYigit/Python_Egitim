import sqlite3 as sql

db = sql.connect('/home/batuhan/Documents/GitHub/Python_Egitim/Telefon_Rehberi/database.sqlite')

cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS deneme (name, surname, phone, mail)""")


cur.execute("""INSERT INTO deneme VALUES ('batuhan', 'Yiğit', '011111111', 'batuhan@gmail.com')""")

db.close()
