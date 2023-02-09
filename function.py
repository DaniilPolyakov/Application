import sqlite3

#функция добавления записи в таблицу users
def insert_record_users(data):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            INSERT INTO users (
                username,
                password,
                name,
                age,
                email,
                checkword) VALUES (?, ?, ?, ?, ?, ?)
                """
        cursor.execute(sql,data)

#функция вывода всех записей таблицы данных пользователей на форме администратора
def get_all_table_users():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = 'SELECT id, name, age, email, username, password, checkword FROM users'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

#функция обновления поля пароля записи таблицы users
def update_passwd(username,new_passwd):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'UPDATE users SET password="{new_passwd}" WHERE username="{username}"'
        cursor.execute(sql)
        return


#обновление полей записи таблицы пользователей
def update_account(id,data):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'UPDATE users SET name="{data[0]}", age="{data[1]}", email="{data[2]}", username="{data[3]}", password="{data[4]}", checkword="{data[5]}" WHERE id ="{id}"'
        cursor.execute(sql)
        return

#функция удаления записи из таблицы users
def delete_account(id):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'DELETE FROM users WHERE id="{id}"'
        cursor.execute(sql)
        return


#функция возвращающая значения полей пользвателя с определенным ником
def get_data(login):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT name, age, email, username, password, checkword FROM users WHERE username="{login}"'
        cursor.execute(sql)
        data = cursor.fetchall()
        print("Геттер данных прошел", data)
        return data

#функция получения id пользователя
def get_id(login):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        print("Геттер id дошел до запроса")
        sql = f'SELECT id FROM users WHERE username="{login}"'
        print("Геттер id прошел этап запроса")
        cursor.execute(sql)
        id = cursor.fetchone()[0]
        print("Геттер id выполняется", id)
        return id
#геттер id учетной записи из таблицы users
def get_id_user(login):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT id FROM users WHERE username="{login}"'
        cursor.execute(sql)
        try:
            id = cursor.fetchone()[0]
            return id
        except:
            return False
#геттер данных одной учетной записи при поиске в таблице на форме
def get_all_data(id):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT id, name, age, email, username, password, checkword FROM users WHERE id="{id}"'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data


#функция получения пароля пользователя с определенным ником, используется при входе в систему
def get_passwd(login):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT password FROM users WHERE username="{login}"'
        cursor.execute(sql)
        passwd = cursor.fetchone()[0]
        return passwd

#функция получения возраста пользователя с определенным ником
def get_age(login):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT age FROM users WHERE username="{login}"'
        cursor.execute(sql)
        age = cursor.fetchone()[0]
        return age

#функция получения логина пользователя 
def get_login(id):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT username FROM users WHERE id="{id}"'
        cursor.execute(sql)
        username = cursor.fetchone()[0]
        return username

        
#функция получения контрольного слова, используется в форме сброса пароля
def get_checkword(username):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT checkword FROM users WHERE username="{username}"'
        cursor.execute(sql)
        checkword = cursor.fetchone()[0]
        return checkword

#проверка на отсутствие записи с выбранным пользователем логином
def check_loggin(loggin):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT * FROM users WHERE username="{loggin}";'
        cursor.execute(sql)
        data = cursor.fetchall()
        if data != []:
            print("существующая запись с таким ником нашлась")
            return False
        else:
            return True



