from abc import ABC, abstractmethod


# ABC (Abstract Base Classes) module - to achieve polymorphism
class DataManagerInterface(ABC):

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_user_movies(self, user_id):
        pass

    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def add_movie(self, movie, user_id):
        pass

    @abstractmethod
    def update_movie(self, user_id, movie_id):
        pass

    @abstractmethod
    def delete_movie(self, user_id, movie_id):
        pass

    @abstractmethod
    def get_username_by_id(self, user_id):
        pass

    @abstractmethod
    def get_movie_by_id(self, movie_id):
        pass
