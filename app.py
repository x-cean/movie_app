import os

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, insert

from datamanager.sql_data_models import db, User, Movie, user_movies
from datamanager.sqlite_data_manager import SQLiteDataManager
from datamanager.api_omdb import search_movie


# get the path safely, if data/ does not exist, create it
basedir = os.path.abspath(os.path.dirname(__file__)) # get the absolute path
data_dir = os.path.join(basedir, 'data')
os.makedirs(data_dir, exist_ok=True) # when the data folder is there, nothing happens
db_path = os.path.join(data_dir, 'data.sqlite')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SECRET_KEY'] = 'secret_key_one'

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
    return render_template('users.html', users=users)


@app.route('/users/<user_id>', methods=['GET'])
def list_user_movies(user_id: int):
    movies = data_manager.get_user_movies(user_id)
    user_name = data_manager.get_username_by_id(user_id)
    if user_name is not None:
        return render_template('list_movies.html',
                           movies=movies, user_id=user_id, user_name=user_name)
    else:
        return render_template('404.html'), 404


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        user = User(name=user_name)
        data_manager.add_user(user)
        flash(f'User: {user.name} added!')
        return redirect(url_for('list_user_movies', user_id=user.id))
    return render_template('add_user.html')


@app.route('/users/<user_id>/add_movie', methods=['GET', 'POST'])
def add_movie(user_id: int):
    # user name
    user_name = data_manager.get_username_by_id(user_id)
    if request.method == 'POST':
        # movie info
        movie_name = request.form.get('movie_name')
        movie_info = search_movie(movie_name)
        if 'Error' in movie_info: # no movie found in api database
            movie = Movie(name=movie_name)
            flash(f'Detailed info not found! Please update manually!')
        else: # movie found
            movie_name = movie_info.get('Title')
            movie_year = movie_info.get('Year')
            movie_rating = movie_info.get('imdbRating')
            movie_director = movie_info.get('Director')
            movie = Movie(
                name=movie_name,
                year=movie_year,
                rating=movie_rating,
                director=movie_director
            )
        # add movie
        data_manager.add_movie(movie=movie, user_id=user_id)
        flash(f'Movie: {movie.name} added to island of {user_name}!')
        return redirect(url_for('list_user_movies', user_id=user_id))
    return render_template('add_movie.html', user_id=user_id,
                           user_name=user_name)


@app.route('/users/<user_id>/update_movie/<movie_id>', methods=['GET', 'POST'])
def update_movie(movie_id: int, user_id: int):

    # this is for html template to get prefilled text
    movie = data_manager.get_movie_by_id(movie_id)
    user_name = data_manager.get_username_by_id(user_id)

    # edge case: movie or user not exist
    if movie is None or user_name is None:
        return render_template('404.html'), 404

    else:
        if request.method == 'POST':
            # collect info from the form
            new_name = request.form.get('movie_name')
            new_director = request.form.get('movie_director')
            new_year = request.form.get('movie_year')
            new_rating = request.form.get('movie_rating')
            # update if new info of movie is collected
            data_manager.update_movie(movie_id=movie_id, user_id=user_id,
                                      new_name=new_name, new_director=new_director,
                                      new_year=new_year, new_rating=new_rating)
            flash(f'Movie {movie.name} updated!')
            return redirect(url_for('list_user_movies', user_id=user_id))

        return render_template('update_movie.html',
                           user_id=user_id, movie_id=movie_id, movie=movie,
                           user_name=user_name)


@app.route('/users/<user_id>/delete_movie/<movie_id>', methods=['POST'])
def delete_movie(user_id: int, movie_id: int):
    movie = data_manager.get_movie_by_id(movie_id)
    data_manager.delete_movie(movie_id=movie_id, user_id=user_id)
    flash(f'Movie {movie.name} deleted!')
    return redirect(url_for('list_user_movies', user_id=user_id))


@app.errorhandler(404)
def page_not_found(e, msg=None):
    # TODO: update the figure
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)