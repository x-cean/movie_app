import os

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, insert

from datamanager.sqlite_data_manager import SQLiteDataManager
from datamanager.sql_data_models import db, User, Movie, user_movies


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'data', 'data.sqlite')


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app) # links the instance of SQLAlchemy to the Flask application instance app

# create tables if they do not exist
with app.app_context(): # activate the app context to use db
    inspector = inspect(db.engine)
    if not inspector.get_table_names():
        db.create_all()

data_manager = SQLiteDataManager(db)


@app.route('/')
def home():
    return "Welcome to MovieWeb App!"


@app.route('/users', methods=['GET'])
def list_users():
    users = data_manager.get_all_users()
    return str(users)


@app.route('/users/<user_id>', methods=['GET'])
def list_user_movies(user_id: int):
    movies = data_manager.get_user_movies(user_id)
    return str(movies)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    user = User(name='hana')
    db.session.add(user)
    db.session.commit()
    return str(user)


@app.route('/users/<user_id>/add_movie', methods=['GET', 'POST'])
def add_movie(user_id: int):
    # movie info
    movie = Movie(name='Pulp Fiction', year=1994, rating=8, director='Quentin Tarantino')

    # add movie
    db.session.add(movie)
    db.session.commit()

    # update the relationship table too
    relate_user_movi = insert(user_movies).values(user_id=user_id, movie_id=movie.id)

    # execute and commit
    db.session.execute(relate_user_movi)
    db.session.commit()
    return str(movie)


@app.route('/users/<user_id>/update_movie/<movie_id>', methods=['GET', 'POST'])
def update_movie(user_id: int, movie_id: int):
    return "Welcome to MovieWeb App!"


@app.route('/users/<user_id>/delete_movie/<movie_id>', methods=['POST'])
def delete_movie(user_id: int, movie_id: int):
    return "Welcome to MovieWeb App!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)