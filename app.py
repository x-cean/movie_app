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


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


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
    data_manager.add_user(user)
    return str(user)


@app.route('/users/<user_id>/add_movie', methods=['GET', 'POST'])
def add_movie(user_id: int):
    # movie info
    movie = Movie(name='Pulp Fiction', year=1994, rating=8, director='Quentin Tarantino')
    # add movie
    data_manager.add_movie(movie=movie, user_id=user_id)
    return str(movie)


@app.route('/users/<user_id>/update_movie/<movie_id>', methods=['GET', 'POST'])
def update_movie(movie_id: int, user_id: int):
    data_manager.update_movie(movie_id=movie_id, new_rating=5)
    return 'updated'


@app.route('/users/<user_id>/delete_movie/<movie_id>', methods=['POST'])
def delete_movie(user_id: int, movie_id: int):
    data_manager.delete_movie(movie_id=movie_id, user_id=user_id)
    return 'deleted'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)