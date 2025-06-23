from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from .data_manager_interface import DataManagerInterface
from .sql_data_models import User, Movie


class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_object):
        try:
            self.db = db_object # initiate, self.db = db object (SQLAlchemy instance)
        except SQLAlchemyError as e:
            print(e)


    def get_all_users(self):
        if User:
            users = User.query.all()
        else:
            users = []
        return users


    def get_user_movies(self, user_id: int):
        user = User.query.get(user_id, None)
        if user:
            return user.movies
        else:
            return 'User not found'


    def add_user(self, user: User):
        pass

    def add_movie(self, movie: Movie):
        pass

    def update_movie(self, movie: Movie):
        pass

    def delete_movie(self, movie: Movie):
        pass




