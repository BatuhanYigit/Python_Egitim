import sqlite3 as sql
import pandas as pd
import sqlquery


with sql.connect('/home/batuhan/Documents/GitHub/Python_Egitim/Pytest/integration_test _ornek/database.sqlite') as conn:
    def create_table():
        cur = conn.cursor()
        cur.execute(sqlquery.create_table)


    def register(username,password,mail):
        cur = conn.cursor()
        information = {"username":username, "password":password, "mail":mail}
        cur.execute(sqlquery.insert_data.format(**information))
        conn.commit()
def main(username,password,mail):
    create_table()
        # username = input("İsminiz")
        # password = input("Şifreniz")
        # mail = input("Mail adresiniz")
    register(username,password,mail)
    

