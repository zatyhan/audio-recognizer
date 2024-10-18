import requests
from pydub import AudioSegment
import os
import base64
from dotenv import load_dotenv
# from bitstring import BitArray

load_dotenv()
url = "https://shazam.p.rapidapi.com/songs/v2/detect"
querystring = {"timezone":"America/Chicago","locale":"en-US"}

headers = {
	"x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
	"x-rapidapi-host": "shazam.p.rapidapi.com",
	"Content-Type": "text/plain"
}

audio = AudioSegment.from_file("audio.mp3", format="mp3").split_to_mono()[0]

audio_data = base64.b64encode(audio._data).decode('utf-8')

response = requests.request("POST", url, headers=headers, params=querystring, data=audio_data)
print(response.status_code)
print(response.json())



