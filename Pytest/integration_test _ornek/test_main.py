import main as test
import pytest
import pandas as pd
import sqlquery
import sqlite3


def test_df():
    username = "dddd"
    password = "asd"
    mail = "deneme"
    test.main(username,password,mail)
    conn = sqlite3.connect('/home/batuhan/Documents/GitHub/Python_Egitim/Pytest/integration_test _ornek/database.sqlite')
    sql_query = pd.read_sql_query(sqlquery.list_data,conn)

    df = pd.DataFrame(sql_query, columns = ['name', 'password', 'mail'])

    last = df.iloc[-1]
    assert username == last['name']
    assert password == last['password']
    assert mail == last['mail']

    print(df.iloc[-1])


test_df()