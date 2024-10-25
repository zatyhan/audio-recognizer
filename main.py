import requests
from pydub import AudioSegment
import os
import base64
from dotenv import load_dotenv
import json
from pytubefix import YouTube
from pytubefix.cli import on_progress
from io import BytesIO

load_dotenv()
url = "https://shazam.p.rapidapi.com/songs/v2/detect"
querystring = {"timezone":"America/Chicago","locale":"en-US"}

headers = {
	"x-rapidapi-key": "20255aac57msh804c236292b3ec2p12abd6jsna3d7d7386a44",
	"x-rapidapi-host": "shazam.p.rapidapi.com",
	"Content-Type": "text/plain"
}

# audio = AudioSegment.from_file("audio.mp3", format="mp3").split_to_mono()[0]
yt = YouTube("https://www.youtube.com/watch?v=9hK-BnCjhWs", on_progress_callback=on_progress)

buffer= BytesIO()
stream = yt.streams.filter(only_audio=True).first().stream_to_buffer(buffer)
buffer.seek(0)
audio= AudioSegment.from_file(buffer, format='mp4', duration=7).split_to_mono()[0]
audio_data = base64.b64encode(audio._data).decode('utf-8')

response = requests.request("POST", url, headers=headers, params=querystring, data=audio_data)
print(response.status_code)
print(json.dumps(response.json(), indent=2))




