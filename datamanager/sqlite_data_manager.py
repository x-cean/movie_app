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


    def update_movie(self, movie: Movie):
        pass

    def delete_movie(self, movie: Movie):
        pass




