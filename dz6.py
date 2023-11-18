import sqlite3
class Film:
    connection = sqlite3.connect('f.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,
                                        name VARCHAR(100) UNIQUE NOT NULL,
                                        genre VARCHAR(100) NOT NULL,
                                        year INTEGER NOT NULL,
                                        director VARCHAR(100) NOT NULL);""")

    # connection = sqlite3.connect('f.db')
    # cursor = connection.cursor()
    # cursor.execute("""INSERT INTO user(name, genre, year, director) VALUES('Oppenheimer', 'epic biographical thriller', '2023', 'Christopher Nolan'),
    #                                                                       ('Blue Beetle', ' Action, Fantasy, Adventure', '2023', 'Angel Manuel Soto'),
    #                                                                       ('Barbie', 'comedy / fantasy', '2023', 'Greta Gerwig'),
    #                                                                       ('The Flash', 'Sci-Fi, Action, Adventure, Superhero, Time Travel and Drama', '2023', 'Andres Muschetti'),
    #                                                                       ('Guardians of the Galaxy', 'fantasy, adventures, action film, comedy, space opera', '2023', 'James Francis Gunn')""")
    # connection.commit()
    # connection.close()

    connection = sqlite3.connect('f.db')
    cursor = connection.cursor()
    cursor.execute("""SELECT name, genre, year, director FROM user""")
    data = cursor.fetchall()
    print(data)
    connection.commit()
    connection.close()



class Director:
    connection = sqlite3.connect('f.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,
                                        name VARCHAR(100) UNIQUE NOT NULL,
                                        second name VARCHAR(100) UNIQUE ;""")

    # connection = sqlite3.connect('f.db')
    # cursor = connection.cursor()
    # cursor.execute("""INSERT INTO user(name, second name) VALUES('Christopher', 'Nolan'),
    #                                                                       ('Angel', 'Manuel Soto'),
    #                                                                       ('Greta', 'Gerwig'),
    #                                                                       ('Andres', 'Muschetti'),
    #                                                                       ('James', 'Francis Gunn')""")
    # connection.commit()
    # connection.close()

    connection = sqlite3.connect('f.db')
    cursor = connection.cursor()
    cursor.execute("""SELECT name, second name FROM user""")
    data = cursor.fetchall()
    print(data)
    connection.commit()
    connection.close()