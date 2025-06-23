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
    def get_movie(self, movie_id):
        pass
