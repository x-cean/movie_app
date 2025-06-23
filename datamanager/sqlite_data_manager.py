from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from .data_manager_interface import DataManagerInterface
from .sql_data_models import User, Movie


class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_object):
        try:
            self.db = db_object
        except SQLAlchemyError as e:
            print(e)

    def get_all_users(self):
        pass

    def get_user_movies(self, user_id: int):
        pass

    def add_user(self, user: User):
        pass

    def add_movie(self, movie: Movie):
        pass

    def update_movie(self, movie: Movie):
        pass

    def delete_movie(self, movie: Movie):
        pass

    def get_movie_via_id(self, movie_id: int):
        pass


