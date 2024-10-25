import requests
from pydub import AudioSegment
import os
import base64
from dotenv import load_dotenv
import json
from pytubefix import YouTube
from pytubefix.cli import on_progress
from io import BytesIO

class Processor():
    """
    Class to extract audio from youtube video, and recognizing the audio using Shazam API

    """
    def __init__(self, yt_url):

        # shazam api variables
        self.shazamapi_key = os.getenv('API_KEY')
        self.shazam_endpoint = "https://shazam.p.rapidapi.com/songs/v2/detect"
        self.querystring = {"timezone":"America/Chicago","locale":"en-US"}
        self.headers = {
            "x-rapidapi-key": "20255aac57msh804c236292b3ec2p12abd6jsna3d7d7386a44",
            "x-rapidapi-host": "shazam.p.rapidapi.com",
            "Content-Type": "text/plain"
        }

        self.yt_url = yt_url
        self.buffer = None

    def process_url(self):
        self.buffer = BytesIO()
        yt= YouTube(self.yt_url)
        
        yt.streams.filter(only_audio=True).first().stream_to_buffer(self.buffer)

        # return self.buffer

    def recognize_audio(self):
        """
        Recognize audio using Shazam API
        """
        self.buffer.seek(0)
        audio = AudioSegment.from_file(self.buffer, format="mp4", duration=7).split_to_mono()[0]
        audio_data = base64.b64encode(audio).decode("utf-8")

        response = requests.request("POST", self.shazam_endpoint, headers=self.headers, data=audio_data, params=self.querystring)
        print(response.text)