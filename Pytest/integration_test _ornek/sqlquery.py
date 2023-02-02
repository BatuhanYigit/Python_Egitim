create_table = """CREATE TABLE IF NOT EXISTS test (name, password, mail)"""

check_data = """SELECT COUNT(*) FROM test"""

insert_data = """INSERT INTO test (name, password, mail) VALUES ('{username}', '{password}', '{mail}')"""

list_data = """SELECT * FROM test"""

delete_test = """DELETE FROM test WHERE id={delete_id}"""


# information = {"username":username, "surname":surname, "phone":phone, "mail":mail}

# cur.execute(sqlquery.insert_data.format(**information))