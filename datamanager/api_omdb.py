import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('API_KEY')
if API_KEY is None: # in case .env is not there or api key not there
    SEARCH_MOVIE_URL = 'http://www.omdbapi.com/?t='
else:
    SEARCH_MOVIE_URL = 'http://www.omdbapi.com/?apikey=' + API_KEY + '&t='


def search_movie(movie_name: str):
    """
    search movie by name and gather movie info
    return dictionary
    """
    search_term = movie_name.strip().replace(' ', '+')
    response = requests.get(SEARCH_MOVIE_URL + search_term)
    movie_info = response.json()
    return movie_info







