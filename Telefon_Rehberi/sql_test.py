import sqlite3
import pandas as pd




conn = sqlite3.connect('/home/batuhan/Documents/GitHub/Python_Egitim/Telefon_Rehberi/database.sqlite')

sql_query = pd.read_sql_query('''SELECT * FROM  deneme''', conn)

df = pd.DataFrame(sql_query, columns= ['name', 'surname', 'phone', 'mail'])

print(df)