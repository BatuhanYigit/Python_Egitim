create_table = """CREATE TABLE IF NOT EXISTS PhoneBook (name, surname, phone, mail)"""

check_data = """SELECT COUNT(*) FROM PhoneBook"""

insert_data = """INSERT INTO PhoneBook (name,surname,phone,mail) VALUES ('{name}', '{surname}', '{phone}', '{mail}')"""

list_data = """SELECT * FROM PhoneBook"""

delete_number = """DELETE FROM PhoneBook WHERE ID={delete_id}"""