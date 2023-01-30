import sqlite3 as sql

db = sql.connect('/home/batuhan/Documents/GitHub/Python_Egitim/Telefon_Rehberi/database.sqlite')

cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS deneme (name, surname, phone, mail)""")

username = input("İsminizi Giriniz : ")
surname = input("Soyisminizi Giriniz : ")
phone = input("Telefon Numaranızı Giriniz : ")
mail = input("Mail adresinizi giriniz : ")

information = {"username":username, "surname":surname, "phone":phone, "mail":mail}

cur.execute("""INSERT INTO deneme VALUES ('{username}', '{surname}', '{phone}', '{mail}')""".format(**information))

db.commit()

db.close()
