import sqlite3 as sql
import sqlquery



db = sql.connect('/home/batuhan/Documents/GitHub/Python_Egitim/Telefon_Rehberi/database.sqlite')
cur = db.cursor()

cur.execute(sqlquery.create_table)

cur.execute(sqlquery.check_data)

data = cur.fetchall()

data = int(data[0][0])

print("Database de {} adet veri var".format(data))

cur.execute(sqlquery.list_data)

test = cur.fetchall()
print("İsim","Soyisim","Telefon","Mail")

print(test,sep='\n',end=",")

# type(test)
# print(test)
# username = input("İsminizi Giriniz : ")
# surname = input("Soyisminizi Giriniz : ")
# phone = input("Telefon Numaranızı Giriniz : ")
# mail = input("Mail adresinizi giriniz : ")

# information = {"username":username, "surname":surname, "phone":phone, "mail":mail}

# cur.execute(sqlquery.insert_data.format(**information))



db.commit()

db.close()
