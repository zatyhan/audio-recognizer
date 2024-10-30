import spotipy
from spotipy.oauth2 import SpotifyPKCE
from dotenv import load_dotenv
import os
import json
import requests
from urllib.parse import urlencode

class PlaylistMaker():
    def __init__(self, name):
        load_dotenv()
        self.playlist_name = name
        self.__clientID__ = os.getenv('SPOTIFY_CLIENT_ID')
        self.__scope__='playlist-modify-public'
        self.__auth_manager__ = SpotifyPKCE(client_id=self.__clientID__, redirect_uri="https://youtify.streamlit.app/", scope=self.__scope__)
        self.__sp__ = spotipy.Spotify(auth_manager=self.__auth_manager__)
        self.user_id= self.__sp__.me()['id']
        self.playlist_id = self.__sp__.user_playlist_create(self.user_id, self.playlist_name)['id'] #add template for description later

    def lookup(self, isrc):
        query= f"isrc:{isrc}"
        # print(query)
        # access_token= self.__auth_manager__.get_access_token()
        # # print(access_token)
        # headers= {
        #     "Authorization": f"Bearer {access_token}"
        # }
        # endpoint= "https://api.spotify.com/v1/search"
        # data = urlencode({
        #     "q": query,
        #     "type": "track"
        # })
        # lookup_url= f"{endpoint}?{data}"
        # results= requests.get(lookup_url, headers=headers).json()
        results = self.__sp__.search(query, type="track")
        # with open('search.json', 'w') as f:
            # f.write(json.dumps(results, indent=2))
        track_id= results['tracks']['items'][0]['id']
        duration= results['tracks']['items'][0]['duration_ms']/1000
        track_title= results['tracks']['items'][0]['name']
        return track_id, track_title, duration

    def add_to_playlist(self, track_id):
        self.__sp__.user_playlist_add_tracks(self.user_id, self.playlist_id, [track_id])
        # print(self.__sp__.user_playlist_tracks(self.user_id, self.playlist_id))

pm= PlaylistMaker('test 2')
# track_id,  track_title, duration = pm.lookup("KRMIM2021578")
track_id, track_title, duration = pm.lookup("GXBAV2441946")
print(track_title)
# pm.add_to_playlist(track_id)
# pm.add_to_playlist(track_id)
