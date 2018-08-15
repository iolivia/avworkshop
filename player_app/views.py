from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Movie

from player_app import imdb_api
from player_app import dash_manifest

import logging

import requests

logging.basicConfig(
    level = logging.INFO
)

logger = logging.getLogger(__name__)

# app constants 
APP_NAME = "My video streaming app"
FOOTER_TEXT = "AV Workshop @ 2017"
MOVIES_PER_ROW = 20

def index(request):

    download_timelines()

    template = loader.get_template("player_app/index.html")

    popular_titles = imdb_api.get_popular_titles()[:MOVIES_PER_ROW]
    popular_movies = imdb_api.get_popular_movies()[:MOVIES_PER_ROW]
    popular_shows = imdb_api.get_popular_shows()[:MOVIES_PER_ROW]

    logger.info("Got {} popular_titles".format(len(popular_titles)))
    logger.info("Got {} popular_movies".format(len(popular_movies)))
    logger.info("Got {} popular_shows".format(len(popular_shows)))

    context = {
        'app_name': APP_NAME,
        'sections':
        [
            {
                'title': "Popular titles",
                'movies': popular_titles
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

def download_video(url, range_start, range_end):
    logger.info("Downloading range: {} - {}".format(range_start, range_end))
    
    # headers = {"Range": "bytes={}-{}".format(range_start, range_end)}

    # r = requests.get(url, headers=headers)
    # logger.info("Request status {}, length = {}".format(r.status_code, len(r.text)))

def download_timelines():
    manifest = dash_manifest.parse_dash_manifest()

    logger.info("Downloading video")
    download_ranges(manifest.get_video().timeline)
    logger.info("Downloading audio")
    download_ranges(manifest.get_audio().timeline)

def download_ranges(timeline):
    start = 0

    for t in timeline:
        # make a request to start - t 
        url = "https://amssamples.streaming.mediaservices.windows.net/683f7e47-bd83-4427-b0a3-26a6c4547782/BigBuckBunny.ism/QualityLevels(5995983)/Fragments(video=0,format=mpd-time-csf)"
        
        end = start + t
        download_video(url, start, end)
        start = end

def player(request, id="Unknown id"):
    
    template = loader.get_template("player_app/player.html")

    # load the whole movie 
    movie_id = request.GET['id']
    movie = imdb_api.get_movie_details_by_id(movie_id)

    context = {
        'app_name': APP_NAME,
        'movie' : movie,
        'footer_text': FOOTER_TEXT
    }

    return HttpResponse(template.render(context, request))