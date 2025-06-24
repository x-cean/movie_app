from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from .data_manager_interface import DataManagerInterface
from .sql_data_models import db, User, Movie


class SQLiteDataManager(DataManagerInterface):

    def __init__(self, db_object):
        try:
            self.db = db_object # initiate, self.db = db object (SQLAlchemy instance)
        except SQLAlchemyError as e:
            print(e)


    def get_all_users(self):
        try:
            return User.query.all()
        except SQLAlchemyError as e:
            print(e)
            return []


    def get_user_movies(self, user_id: int):
        try:
            user = User.query.get(user_id)
            if user:
                return user.movies
            else:
                return []
        except SQLAlchemyError as e:
            print(e)
            return []


    def add_user(self, user: User):
        try:
            if isinstance(user, User):
                db.session.add(user)
                db.session.commit()
            else:
                raise TypeError("User must be a User instance")
        except SQLAlchemyError as e:
            print(e)


    def add_movie(self, movie: Movie):
        try:
            if isinstance(movie, Movie):
                db.session.add(movie)
                db.session.commit()
            else:
                raise TypeError("Movie must be a Movie instance")
        except SQLAlchemyError as e:
            print(e)


    def update_movie(self, movie: Movie, new_name: str=None, new_director: str=None,
                     new_year: int=None, new_rating: int=None):
        try:
            if isinstance(movie, Movie):
                if new_name is not None:
                    movie.name = new_name # have to think about how to update
                if new_director is not None:
                    movie.director = new_director
                if new_year is not None:
                    movie.year = new_year
                if new_rating is not None:
                    movie.rating = new_rating
                self.db.session.commit()
            else:
                raise TypeError("Movie must be a Movie instance")
        except SQLAlchemyError as e:
            print(e)
            self.db.session.rollback() # undo any partial change


    def delete_movie(self, movie: Movie):
        pass




