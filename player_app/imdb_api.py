# imports
import json
import pdb
import logging
from imdbpie import Imdb

# models
from .models import Movie, MovieDetails

# setup logger
# usage: logger.info("hello info!")
logger = logging.getLogger(__name__)

# movies count for placeholder movies
MOVIES_COUNT = 30

# initialize imdb instance 
imdb = Imdb(anonymize=True)

# gets top 250 movies from imdb
# example model is in docs/movie.json
# should return models.Movie
def get_top_250_movies():

    return _get_placeholder_movies(MOVIES_COUNT)

# gets popular movies from imdb
# example model is in docs/movie.json
# should return models.Movie
def get_popular_movies():

    return _get_placeholder_movies(MOVIES_COUNT)

# gets popular shows from imdb
# example model is in docs/movie.json
# should return models.Movie
def get_popular_shows():

    return _get_placeholder_movies(MOVIES_COUNT)

# gets one movie from imdb
# example model is in docs/movie-details.json
# should return models.MovieDetails
def get_movie_details_by_id(id):

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

# creates a number of placeholder movies using test data. 
# returns a list of models.Movie
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

# creates a placeholder movie detail object
# returns models.MovieDetails
def _get_placeholder_movie_details():
    
    image_url = "http://via.placeholder.com/125x175"
    trailer_url = "https://github.com/bower-media-samples/big-buck-bunny-1080p-30s/blob/master/video.mp4?raw=true"

    movie_details_model = MovieDetails.create(
        "id", 
        "Movie title", 
        "2017",
        "Some plot",
        8.2,
        image_url,
        trailer_url)

    return movie_details_model