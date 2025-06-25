from sqlalchemy import insert, delete
from sqlalchemy.exc import SQLAlchemyError

from .data_manager_interface import DataManagerInterface
from .sql_data_models import db, User, Movie, user_movies


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
                self.db.session.add(user)
                self.db.session.commit()
            else:
                raise TypeError("User must be a User instance")
        except SQLAlchemyError as e:
            print(e)


    def add_movie(self, user_id: int, movie: Movie):
        try:
            if isinstance(movie, Movie):
                # update the movies-table
                self.db.session.add(movie)
                self.db.session.commit()

                # update the relationship table too
                relate_user_movi = insert(user_movies).values(user_id=user_id, movie_id=movie.id)

                # execute and commit
                self.db.session.execute(relate_user_movi)
                self.db.session.commit()
            else:
                raise TypeError("Movie must be a Movie instance")
        except SQLAlchemyError as e:
            print(e)


    def update_movie(self, user_id: int, movie_id: int, new_name: str=None, new_director: str=None,
                     new_year: int=None, new_rating: int=None):
        try:
            movie = Movie.query.get(movie_id)
            if movie is not None:
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
                print("Movie not found in the database")
        except SQLAlchemyError as e:
            print(e)
            self.db.session.rollback() # undo any partial change


    def delete_movie(self, movie_id: int, user_id: int):
        try:
            movie = Movie.query.get(movie_id)
            if movie is not None:
                # delete it from movies
                self.db.session.delete(movie)
                self.db.session.commit()
                # delete it from the relationship table
                delete_user_movie = delete(user_movies).where(
                    (user_movies.c.user_id == user_id) & (user_movies.c.movie_id == movie_id)
                )
                self.db.session.execute(delete_user_movie)
                self.db.session.commit()
            else:
                print("Movie not found in the database")
        except SQLAlchemyError as e:
            print(e)
            self.db.session.rollback()


    def get_user_by_id(self, user_id: int):
        try:
            user = User.query.get(user_id)
            if user is not None:
                return user.name
            else:
                return None
        except SQLAlchemyError as e:
            print(e)




