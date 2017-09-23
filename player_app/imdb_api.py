import json
import pdb
from imdbpie import Imdb

from .models import Movie, MovieDetails

import logging
logger = logging.getLogger(__name__)

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

def get_movie_by_id(id):

    imdb = Imdb(anonymize=True)
    imdb_movie = imdb.get_title_by_id(id)

    movie_details = _parse_title(imdb_movie)

    return movie_details

def _parse_title(title):

    image_url = title.poster_url
    trailer_url = title.trailers[0]['url']

    movie_details_model = MovieDetails.create(
        title.imdb_id, 
        title.title, 
        title.year,
        title.plot_outline,
        title.rating,
        image_url,
        trailer_url)

    return movie_details_model

def _parse_movie(movie):

    if 'object' in movie:
        movie = movie['object']

    movie_id            = _try_get_attribute(movie, 'tconst')
    movie_title         = _try_get_attribute(movie, 'title')
    movie_image         = _try_get_attribute(movie, 'image')
    movie_image_url     = _try_get_attribute(movie_image, 'url')

    movie_model = Movie.create(
        movie_id, 
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
        movie_id = "id"
        movie_title = "Movie " + str(i)
        movie_image_url = "http://via.placeholder.com/125x175"

        movie = Movie.create(
            movie_id,
            movie_title,
            movie_image_url
        )

        movies.append(movie)
    
    return movies