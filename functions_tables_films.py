import sqlite3

#функция добавления новой записи в таблицу фильмов
def insert_record_film(table_name,data):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f"""
            INSERT INTO {table_name} (
                film_name,
                country,
                age_lim,
                year,
                director,
                score,
                sinopsis) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(sql,data)

#функция вывода данных в форму редактирования фильмов
def get_data_record_film(table_name, id):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT film_name,country,age_lim,year,director,score,sinopsis FROM {table_name} WHERE id="{id}"'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

#функция выборки данных в таблицы пользовательской формы
def get_data_film(table_name):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT film_name, country, year, age_lim, score FROM {table_name}'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
#функция выборки данных в таблицу пользовательской детской формы
def get_data_film_kid(table_name):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT film_name, country, year, age_lim FROM {table_name} WHERE age_lim<=12'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data


#функция добавления записи в таблицу новинок
def insert_record_newfilm(data):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            INSERT INTO newFilm (
                film_name,
                country,
                age_lim,
                year,
                director,
                score,
                sinopsis,
                genre
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(sql, data)

#функция выборки данных из таблицы новинок в таблицу пользовательской формы
def get_data_newfilm():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = "SELECT film_name, genre, country, year, age_lim, score FROM newFilm"
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

#функция вывода данных из таблицы новинок в таблицу пользовательской детской формы
def get_data_newfilm_kid():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = 'SELECT film_name, genre, country, year, age_lim FROM newFilm WHERE age_lim<=12'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

#функция обновления записи таблицы фильма
def update_record_film(table_name, data, id):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'UPDATE {table_name} SET film_name="{data[0]}", country="{data[1]}", age_lim="{data[2]}", year="{data[3]}", director="{data[4]}", score="{data[5]}", sinopsis="{data[6]}" WHERE id="{id}"'
        cursor.execute(sql)
        return

#функция получения id фильма
def get_id_film(table_name, film_name):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT id FROM {table_name} WHERE film_name="{film_name}"'
        cursor.execute(sql)
        try:
            id = cursor.fetchone()[0]
            return id
        except:
            return False

#функция выборки подробных данных о фильме
def get_info_film(table_name, id):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT film_name, director, sinopsis FROM {table_name} WHERE id="{id}"'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

#функция удаления записи из таблицы фильмов
def delete_record_film(table_name, id):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'DELETE FROM {table_name} WHERE id="{id}"'
        cursor.execute(sql)
        return

#функция вывода записи при поиске
def get_data_search(table_name,id):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT film_name, country, year, age_lim, score FROM {table_name} WHERE id="{id}"'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

#функция вывода записи при поиске в детской форме
def get_data_search_kid(table_name, id):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT film_name, country, year, age_lim FROM {table_name} WHERE id="{id}" AND age_lim<=12'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

#функция вывода записи при поиске на форме новинок проката
def get_data_search_newfilm(id):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT film_name,genre,country,year,age_lim, score FROM newFilm WHERE id="{id}"'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

#функция вывода записи при поиске на детской форме новинок
def get_data_search_newfilm_kid(id):
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = f'SELECT film_name,genre,country,year,age_lim FROM newFilm WHERE id="{id}" AND age_lim<=12'
        cursor.execute(sql)
        data = cursor.fetchall()
        return data




