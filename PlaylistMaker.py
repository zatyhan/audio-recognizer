import requests
import os
from io import BytesIO
import spotipy
from spotipy.oauth2 import SpotifyPKCE

class PlaylistMaker():
    def __init__(self, name):
        self.playlist_name = name
        self.__clientID__ = "d3eb6ef85c20439d89f4c6b100024b20"
        self.__scope__='playlist-modify-public'
        self.__auth_manager__ = SpotifyPKCE(client_id=self.__clientID__, redirect_uri="https://youtify.streamlit.app/", scope=self.__scope__)
        self.__sp__ = spotipy.Spotify(auth_manager=self.__auth_manager__)
        self.user_id= self.__sp__.me()['id']
        self.playlist_id = self.__sp__.user_playlist_create(self.user_id, self.playlist_name)['id'] #add template for description later

    def lookup(self, track_name, artist_name, album=None):
        query= f"q=remaster%%2520track%%3A{track_name.replace(' ', '+')}%%2520artist%%3A{artist_name.replace(' ', '+')}%%2520"
        results = self.__sp__.search(query, type="track")
           
        return results['tracks']['items'][0]['id'], results['tracks']['items'][0]['duration_ms']/1000

    def add_to_playlist(self, track_id):
        self.__sp__.user_playlist_add_tracks(self.user_id, self.playlist_id, [track_id])
        # print(self.__sp__.user_playlist_tracks(self.user_id, self.playlist_id))

# pm= PlaylistMaker('test 2')
# track_id,  duration = pm.lookup('Supernatural', 'NewJeans')
# pm.add_to_playlist(track_id)
# track_id,  duration = pm.lookup('Berharap Kau Kembali', 'Fabio Asher')
# pm.add_to_playlist(track_id)
