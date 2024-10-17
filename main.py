import requests
from pydub import AudioSegment
import os
import base64
from dotenv import load_dotenv
# from bitstring import BitArray

load_dotenv()
url = "https://shazam.p.rapidapi.com/songs/detect"
querystring = {"timezone":"America/Chicago","locale":"en-US"}

headers = {
	"x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
	"x-rapidapi-host": "shazam.p.rapidapi.com",
	"Content-Type": "text/plain"
}

audio = AudioSegment.from_file("audio_ori.mp3")
print(len(audio))
# split song into 30 second chunks
for i in range(0, len(audio), 7000):
	audio_chunk = audio[i:i+7000]
	audio_chunk.export("audio.mp3", format="mp3")

	base64_audio = base64.b64encode(open("audio.mp3", "rb").read())

	response = requests.post(url, data=base64_audio, headers=headers)

	# print(i, end=" ")
	if response.status_code == 200:
		if len(response.json()["matches"]) > 0:
			print(i)
			print(len(response.json()['matches']))
			break
		else:
			print(response.json())

