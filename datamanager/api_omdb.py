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
    try:
        response = requests.get(SEARCH_MOVIE_URL + search_term, timeout=10)
        response.raise_for_status()
        movie_info = response.json()
    except requests.exceptions.RequestException as e:
        movie_info = {"error": f"Network error: {str(e)}"}
    return movie_info


movie_example = search_movie('The Godfather')
print(movie_example)
print(type(movie_example))
print(type(movie_example['Year']))




