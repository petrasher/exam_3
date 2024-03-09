from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///base_2.db')

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    name_of_movie = Column(String)
    director = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

movies_data = [
    {'name_of_movie': 'Movie 1', 'director': 'Director 1'},
    {'name_of_movie': 'Movie 2', 'director': 'Director 2'},
    {'name_of_movie': 'Movie 3', 'director': 'Director 3'}
]

for movie_data in movies_data:
    movie = Movie(**movie_data)
    session.add(movie)

session.commit()

session.close()
