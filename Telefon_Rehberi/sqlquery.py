create_table = """CREATE TABLE IF NOT EXISTS deneme (name, surname, phone, mail)"""

check_data = """SELECT COUNT(*) FROM deneme"""

insert_data = """INSERT INTO deneme VALUES ('{username}', '{surname}', '{phone}', '{mail}')"""

list_data = """SELECT * FROM deneme"""