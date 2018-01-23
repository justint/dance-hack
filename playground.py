import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
from time import sleep
import json
import time
import sys
import os



CLIENT_ID 		= # insert your client id here
CLIENT_SECRET 	= # insert your client secret here
SPOTIFY_USER	= # insert your spotify username here

def get_spotipy_client():
	client_credentials_manager = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret = CLIENT_SECRET)
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	return sp

def get_user_token():
	username = SPOTIFY_USER
	scope = 'user-modify-playback-state user-read-currently-playing'
	token = util.prompt_for_user_token(username,scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET, redirect_uri="http://127.0.0.1:8000/")
	return token


def choose_song(score, sp):
	if score <= 0.5:
		# reverie = "25iR8skNi5XI6gzqhK788r"
		sp.start_playback(uris = ["spotify:track:25iR8skNi5XI6gzqhK788r"])
		sp.seek_track(position_ms = 28000)
	else:
		# death metal pizza = "2vI1lVsqTWKSTMxzEEJwpP"
		sp.start_playback(uris = ["spotify:track:2vI1lVsqTWKSTMxzEEJwpP"])
		sp.seek_track(position_ms = 26000)

	# sonic id = "0jNRhMhYJS4e2Vo82TOajD"

def choose_volume(score, sp):
	percent = int(score * 100)

	# rescaling the percent [0, 100] to be in the range of [40, 100]
	min_range = 35
	max_range = 100

	new_volume = ((max_range - min_range) * (percent - 0) / (100 - 0)) + min_range


	print("volume percent:")
	print(new_volume)


	sp.volume(new_volume)




def run(type, score):
	token = get_user_token()

	if token:
		sp = spotipy.Spotify(auth = token)

		if type == "volume":
			choose_volume(score, sp)
		elif type== "song":
			choose_song(score, sp)

def normalize_std(std):

	# this max_std number may have to be tweaked (because std can go to infinity, but at some point we want to go to max volume, for example)
	max_std = 50
	min_std = 0

	if std > max_std:
		return 1.0
	else:
		# rescaling the std in the range of [0, 100] to be in the range of [min_range, max_range]
		min_range = 0.0
		max_range = 1.0

		normalized_std = ((max_range - min_range) * (std - min_std) / (max_std - min_std)) + min_range

	return normalized_std


def calculate_std():
	x_right_std = float(sys.argv[1])
	y_right_std = float(sys.argv[2])
	x_left_std = float(sys.argv[3])
	y_left_std = float(sys.argv[4])

	avg_std_right = (x_right_std + y_right_std) / 2.0
	avg_std_left = (x_left_std + y_left_std) / 2.0

	avg_std = (avg_std_right + avg_std_left) / 2.0

	max_std = max([x_right_std, x_left_std, y_right_std, y_left_std])

	print("max_std:")
	print(max_std)

	return max_std

# arguement "volume" -> virtual DJ will adjust volume
# arguement "song" -> virtual DJ will change tracks
run("volume", normalize_std(calculate_std()))
