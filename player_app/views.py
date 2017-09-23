from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Movie

from player_app import imdb_api

import logging
logger = logging.getLogger(__name__)

# app constants 
APP_NAME = "My video streaming app"
FOOTER_TEXT = "AV Workshop @ 2017"

def index(request):

    template = loader.get_template("player_app/index.html")

    movies_count = 15

    top_250 = imdb_api.get_top_250_movies()[:movies_count]
    popular_movies = imdb_api.get_popular_movies()[:movies_count]
    popular_shows = imdb_api.get_popular_shows()[:movies_count]

    context = {
        'app_name': APP_NAME,
        'sections':
        [
            {
                'title': "Top 250 movies",
                'movies': top_250
            },
            {
                'title': "Popular movies",
                'movies': popular_movies
            },
            {
                'title': "Popular shows",
                'movies': popular_shows
            }
        ],
        'footer_text': FOOTER_TEXT
    }

    return HttpResponse(template.render(context, request))

def player(request, title="No title"):
    
    template = loader.get_template("player_app/player.html")

    context = {
        'app_name': APP_NAME,
        'title' : request.GET['title'],
        'footer_text': FOOTER_TEXT
    }

    return HttpResponse(template.render(context, request))

def _get_movies(count):
    movies = []

    for i in range(1, count+1):
        movie = Movie.create("Movie " + str(i))
        movies.append(movie)
    
    return movies
