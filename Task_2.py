
import sqlite3

conn = sqlite3.connect('base.db')

cursor = conn.cursor()

#cursor.execute('''CREATE TABLE movies(movie_id INTEGER PRIMARY KEY, name_of_movie TEXT, director TEXT)''')
cursor.execute("""INSERT INTO movies (name_of_movie, director)  values (?,?)""", [input('Enter name of the movie: '), input( 'Enter director of the movie: ')])
conn.commit()
cursor.close()