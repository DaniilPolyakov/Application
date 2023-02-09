import sqlite3

#создание таблицы пользователей
def create_table_users():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            CREATE TABLE users (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                username VARCHAR NOT NULL,
                password VARCHAR(10) NOT NULL,
                name VARCHAR NOT NULL,
                age VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                checkword VARCHAR NOT NULL
            )
        """
        cursor.execute(sql)

#создание таблицы комедий
def create_table_comedy():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            CREATE TABLE comedy (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                film_name VARCHAR NOT NULL,
                country VARCHAR NOT NULL,
                age_lim INTEGER NOT NULL,
                year VARCHAR NOT NULL,
                sinopsis TEXT,
                director VARCHAR NOT NULL,
                score VARCHAR NOT NULL
            )
        """
        cursor.execute(sql)

#создание таблицы мультфильмов
def create_table_cartoon():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            CREATE TABLE cartoons (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                film_name VARCHAR NOT NULL,
                country VARCHAR NOT NULL,
                age_lim INTEGER NOT NULL,
                year VARCHAR NOT NULL,
                sinopsis TEXT,
                director VARCHAR NOT NULL,
                score VARCHAR NOT NULL
            )
        """
        cursor.execute(sql)

#создание таблицы драм
def create_table_dram():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            CREATE TABLE dram (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                film_name VARCHAR NOT NULL,
                country VARCHAR NOT NULL,
                age_lim INTEGER NOT NULL,
                year VARCHAR NOT NULL,
                sinopsis TEXT,
                director VARCHAR NOT NULL,
                score VARCHAR NOT NULL
            )
        """
        cursor.execute(sql)

#создание таблицы фантастики
def create_table_fantasy():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            CREATE TABLE fantasy (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                film_name VARCHAR NOT NULL,
                country VARCHAR NOT NULL,
                age_lim INTEGER NOT NULL,
                year VARCHAR NOT NULL,
                sinopsis TEXT,
                director VARCHAR NOT NULL,
                score VARCHAR NOT NULL
            )
        """
        cursor.execute(sql)

#создание таблицы боевиков
def create_table_action():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            CREATE TABLE action (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                film_name VARCHAR NOT NULL,
                country VARCHAR NOT NULL,
                age_lim INTEGER NOT NULL,
                year VARCHAR NOT NULL,
                sinopsis TEXT,
                director VARCHAR NOT NULL,
                score VARCHAR NOT NULL
            )
        """
        cursor.execute(sql)

#создание таблицы исторических фильмов
def create_table_history():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            CREATE TABLE history (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                film_name VARCHAR NOT NULL,
                country VARCHAR NOT NULL,
                age_lim INTEGER NOT NULL,
                year VARCHAR NOT NULL,
                sinopsis TEXT,
                director VARCHAR NOT NULL,
                score VARCHAR NOT NULL
            )
        """
        cursor.execute(sql)

#создание таблицы фильмов ужасов
def create_table_horror():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            CREATE TABLE horror (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                film_name VARCHAR NOT NULL,
                country VARCHAR NOT NULL,
                age_lim INTEGER NOT NULL,
                year VARCHAR NOT NULL,
                sinopsis TEXT,
                director VARCHAR NOT NULL,
                score VARCHAR NOT NULL
            )
        """
        cursor.execute(sql)

#создание таблицы детективов
def create_table_detective():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            CREATE TABLE detective (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                film_name VARCHAR NOT NULL,
                country VARCHAR NOT NULL,
                age_lim INTEGER NOT NULL,
                year VARCHAR NOT NULL,
                sinopsis TEXT,
                director VARCHAR NOT NULL,
                score VARCHAR NOT NULL
            )
        """
        cursor.execute(sql)

#создание таблицы сериалов
def create_table_serial():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            CREATE TABLE serial (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                film_name VARCHAR NOT NULL,
                country VARCHAR NOT NULL,
                age_lim INTEGER NOT NULL,
                year VARCHAR NOT NULL,
                sinopsis TEXT,
                director VARCHAR NOT NULL,
                score VARCHAR NOT NULL
            )
        """
        cursor.execute(sql)
#создание таблицы новинок
def create_table_new_film():
    connector = sqlite3.connect("database.db")
    with connector as db:
        cursor = db.cursor()
        sql = """
            CREATE TABLE newFilm (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                film_name VARCHAR NOT NULL,
                genre VARCHAR NOT NULL,
                country VARCHAR NOT NULL,
                age_lim INTEGER NOT NULL,
                year VARCHAR NOT NULL,
                sinopsis TEXT,
                director VARCHAR NOT NULL,
                score VARCHAR NOT NULL
            )
        """
        cursor.execute(sql)

def main():
    create_table_users()
    create_table_cartoon()
    create_table_comedy()
    create_table_dram()
    create_table_fantasy()
    create_table_action()
    create_table_history()
    create_table_horror()
    create_table_detective()
    create_table_serial()
    create_table_new_film()
    print("\n\tTables successfully created!")

if __name__=="__main__":
    main()
