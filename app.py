import os

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

from datamanager.sqlite_data_manager import SQLiteDataManager
from datamanager.sql_data_models import db, User, Movie


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'data', 'data.sqlite')


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app) # links the instance of SQLAlchemy to the Flask application instance app

# create tables if they do not exist
with app.app_context():
    inspector = inspect(db.engine)
    if not inspector.get_table_names():
        db.create_all()

data_manager = SQLiteDataManager(db)

# just for testing whether data_manager worked
# with app.app_context():
#     users = data_manager.get_all_users()
#     print(users)


@app.route('/')
def home():
    return "Welcome to MovieWeb App!"


@app.route('/users', methods=['GET'])
def list_users():
    users = data_manager.get_all_users()
    return str(users)


@app.route('/users/<user_id>', methods=['GET'])
def list_user_movies(user_id: int):
    return "Welcome to MovieWeb App!"


@app.route('/add_user', methods=['GET', 'POST'])
def add_user(user_id: int):
    return "Welcome to MovieWeb App!"


@app.route('/users/<user_id>/add_movie', methods=['GET', 'POST'])
def add_movie(user_id: int):
    return "Welcome to MovieWeb App!"


@app.route('/users/<user_id>/update_movie/<movie_id>', methods=['GET', 'POST'])
def update_movie(user_id: int, movie_id: int):
    return "Welcome to MovieWeb App!"


@app.route('/users/<user_id>/delete_movie/<movie_id>', methods=['POST'])
def delete_movie(user_id: int, movie_id: int):
    return "Welcome to MovieWeb App!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)