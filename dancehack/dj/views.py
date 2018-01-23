from django.shortcuts import render
from django.http import HttpResponse


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import json
import time

CLIENT_ID 		= # insert your client id here
CLIENT_SECRET 	= # insert your client secret here
SPOTIFY_USER	= # insert your spotify username here


# Spotify credentials
client_credentials_manager = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret = CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username = SPOTIFY_USER
scope = 'user-modify-playback-state user-read-currently-playing'




def index(request):

	context = {}

	return render(request, template_name='dj/base.html', context=context)
