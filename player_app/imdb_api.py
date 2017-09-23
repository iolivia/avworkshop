import json
from imdbpie import Imdb

from .models import Movie

MOVIES_COUNT = 30

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

def _get_placeholder_movies(count):

    movies = []

    for i in range(1, count+1):
        movie_title = "Movie " + str(i)
        movie_image_url = "http://via.placeholder.com/125x175"

        movie = Movie.create(
            movie_title,
            movie_image_url
        )

        movies.append(movie)
    
    return movies