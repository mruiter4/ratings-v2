"""Create and seed all tables"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

#drop and recreate ratings db
os.system('dropdb ratings')
os.system('createdb ratings')

#connect to the db and create all tables
model.connect_to_db(server.app)
model.db.create_all()

#load data from json file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

#create movies and store them in a list so we can use the list
#to create ratings
movies_in_db = []
for movie in movie_data:
    title = movie['title']
    overview = movie['overview']
    poster_path=movie['poster_path']
    #convert date from string to datetime object
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

    #create a new movie
    #append to db
    new_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(new_movie)
print(movies_in_db)

#create 10 users
for n in range(10):
    user = crud.create_user(f'user{n}@test.test', 'test')
    for i in range(10):
        crud.create_rating(user, choice(movies_in_db), randint(1,5))