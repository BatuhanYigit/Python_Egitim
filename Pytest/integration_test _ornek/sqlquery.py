create_table = """CREATE TABLE IF NOT EXISTS test (name, password, mail)"""

check_data = """SELECT COUNT(*) FROM test"""

insert_data = """INSERT INTO test VALUES ('{username}', '{password}', '{mail}')"""

list_data = """SELECT * FROM test"""


# information = {"username":username, "surname":surname, "phone":phone, "mail":mail}

# cur.execute(sqlquery.insert_data.format(**information))