import os
import
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('API_KEY')
SEARCH_MOVIE_URL = 'http://www.omdbapi.com/?apikey=' + API_KEY + '&t='


def search_movie(movie_name: str):
    search_term = movie_name.strip().replace(' ', '+')





