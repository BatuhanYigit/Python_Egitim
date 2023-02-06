import sqlquery
import phonebook
import sqlite3 as sql
import pandas as pd

def add_number_test(name, surname, phone, mail):
        print(""" 
                **************Numara Ekleme************
                """)

        info = {"name":name, 
                "surname":surname,
                "phone":phone,
                "mail":mail,
                }
        phonebook.cur.execute(sqlquery.insert_data.format(**info))
        phonebook.conn.commit()
        print("Kullanıcı Rehbere Eklendi.")
        print("""EKLENEN Kişi
                 İsim : {}
                 Soyisim : {}
                 Telefon : {}
                 Mail : {}
              """.format(name, surname, phone, mail))
        

def phonebook_list():
        query = pd.read_sql_query(sqlquery.list_data,phonebook.conn)
        df = pd.DataFrame(query, columns=['ID','name','surname','phone','mail'])

        if df.empty:
                print("Rehberinizde kimse bulunmuyor")
        
        else:
                print(df)

def delete_number():
        phonebook_list()

        id = input("Silmek İstediğiniz Numaranın ID sini giriniz : ")
        delete_info = {"delete_id":id}
        question = input("Numarayı Silmek İstediğine Emin Misin? (E/H) : ")
        if question == "e" or question == "E":

                phonebook.cur.execute(sqlquery.delete_number.format(**delete_info))
                phonebook.conn.commit()
                
                print("Numara Silindi")
                phonebook_list()
        else:
                print("Numara silinmedi")

