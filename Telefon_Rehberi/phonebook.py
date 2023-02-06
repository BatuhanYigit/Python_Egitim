import sqlite3 as sql
import sqlquery
import pandas as pd
import func

with sql.connect('/home/batuhan/Documents/GitHub/Python_Egitim/Telefon_Rehberi/database.sqlite') as conn:
            cur = conn.cursor()
            cur.execute(sqlquery.create_table)
            if __name__ == "__main__":
                while True:
                    print("""
                           *********************************************************************
                           * Telefon Rehberine Hoş Geldiniz Yapmak İstediğiniz İşlemi Seçiniz! *
                           * 1- Numara Ekleme                                                  *
                           * 2- Numara Silme                                                   *
                           * 3- Rehberi Görüntüle                                              *
                           * q - Çıkış                                                         * 
                           *********************************************************************
                            """)
                    choice = input("İşlem : ")

                    if choice == '1':
                        
                        print("Numara Ekleme")
                        name = input("Kişinin İsmi : ")
                        surname = input("Kişinin Soyismi : ")
                        phone = input("Kişinin Telefon Numarası : ")
                        mail = input("Kişinin Mail Adresi : ")
                        func.add_number_test(name,surname,phone,mail)

                        

                    elif choice == '2':
                        print("Numara Silme")
                        func.delete_number()
                    elif choice == '3':
                        print("Rehberi Görüntüle")
                        func.phonebook_list()

                    elif choice == "q" or choice == "Q":
                        print("Çıkış Yapılıyor")
                        exit()
                    else:
                        print("Yanlış İşlem")



