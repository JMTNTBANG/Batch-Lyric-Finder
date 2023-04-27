from dotenv import load_dotenv
from os import getenv
from lyricsgenius import Genius
import music_tag
import os

supported_formats = (
    'aac',
    'aiff',
    'dsf',
    'flac',
    'm4a',
    'mp3',
    'ogg',
    'opus',
    'wav',
    'wv'
)

load_dotenv()
token = getenv('ACCESS_TOKEN')
if token is None:
    raise ValueError('Please Paste your Access Token in the .env file')
try:
    genius = Genius(token)
except TypeError:
    raise ValueError('Please try a new Access Token as this one did not work...')

while True:
    music_directory = input('Please enter the directory of your Music: ')
    try:
        os.listdir(music_directory)
    except Exception as exception:
        print(exception)
    else:
        break

while True:
    lyric_directory = input('Please enter the output directory of the lyrics: ')
    try:
        os.listdir(lyric_directory)
    except Exception as exception:
        print(exception)
    else:
        break

for file in os.listdir(music_directory):
    if file.endswith(supported_formats):
        song = music_tag.load_file(music_directory+'/'+file)
        lyrics = genius.search_song(str(song['tracktitle']), str(song['artist'])).lyrics
