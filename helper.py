import spotipy
from spotipy.oauth2 import SpotifyPKCE
from dotenv import load_dotenv
import os 

# # load_dotenv("C:/Users/Investment Officer/Downloads/eizzaty/audio-recognizer/.env")
# SPOTIFY_CLIENT_ID="d3eb6ef85c20439d89f4c6b100024b20"
# scope='playlist-modify-public'
# # print(os.getenv("SPOTIPY_CLIENT_ID"))
# auth_manager = SpotifyPKCE(client_id=SPOTIFY_CLIENT_ID, redirect_uri="https://youtify.streamlit.app/", scope=scope)
# sp= spotipy.Spotify(auth_manager=auth_manager)
# print(sp.search("spotify:search:Walk%20NCT%20127"))

yt = YouTube("https://www.youtube.com/watch?v=YTFpRqdINqI")

video = yt.streams.filter(only_audio=True).first()


