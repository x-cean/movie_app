from flask_sqlalchemy import SQLAlchemy
from .data_manager_interface import DataManagerInterface


class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        self.db = SQLAlchemy(db_file_name)

    def get_all_users(self):
        print("1")

    def get_user_movies(self, user_id):
        print("2")

    def get_movie(self, movie_id):
        print("3")