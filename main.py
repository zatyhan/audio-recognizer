from PlaylistMaker import PlaylistMaker
from Processor import Processor

yt_url = input('Enter youtube URL: ')
playlist_name = input('Enter playlist name: ')

try: 
    track = Processor(yt_url)
except:
    print('Invalid URL')

try:
    track.process_url()
except:
    print('Failed to process track')

playlist= PlaylistMaker(playlist_name)
start_time=0
video_length= track.video_length()
# print(video_length)

# track_title, artist=  track.recognize_audio(start_time=start_time)
# print(track_title,  artist)

# track_id, duration= playlist.lookup(track_name=track_title, artist_name=artist)
# print(track_id, duration)

# playlist.add_to_playlist(track_id)
# start_time+=duration +1
# print(start_time)
while start_time< video_length:
    try:
        track_title, artist=  track.recognize_audio(start_time=start_time)
        print("track found: ", track_title)
        track_id, duration= playlist.lookup(track_name=track_title, artist_name=artist)
        
        playlist.add_to_playlist(track_id)
        start_time+=duration +1

    except:
        print('Something went wrong')
    
print('Playlist created successfully!')