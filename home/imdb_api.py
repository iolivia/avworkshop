import json
from imdbpie import Imdb

from .models import Movie

def get_top_250_movies():

    imdb = Imdb(anonymize=True)
    movies = imdb.top_250()

    return list(map(lambda m: _parse_movie(m), movies))

def get_popular_movies():

    imdb = Imdb(anonymize=True)
    movies = imdb.popular_movies()

    return list(map(lambda m: _parse_movie(m), movies))

def get_popular_shows():

    imdb = Imdb(anonymize=True)
    movies = imdb.popular_shows()

    return list(map(lambda m: _parse_movie(m), movies))

def _parse_movie(movie):

    if 'object' in movie:
        movie = movie['object']

    movie_title         = _try_get_attribute(movie, 'title')
    movie_image         = _try_get_attribute(movie, 'image')
    movie_image_url     = _try_get_attribute(movie_image, 'url')

    movie_model = Movie.create(
        movie_title, 
        movie_image_url)

    return movie_model

def _try_get_attribute(obj, attribute):

    if attribute in obj:
        return obj[attribute]

    return ""