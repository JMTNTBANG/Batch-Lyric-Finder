import sys
import time

import requests.exceptions
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
illegal_characters = '#%&{}\\<>*?/$!:@+`|='

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


def get_lyrics(music_directory):
    for file in os.listdir(music_directory):
        if os.path.isfile(music_directory+'/'+file):
            if file.endswith(supported_formats):
                song = music_tag.load_file(music_directory+'/'+file)
                while True:
                    try:
                        lyrics = genius.search_song(str(song['tracktitle']), str(song['artist'])).lyrics
                    except AttributeError:
                        print('Skipping...')
                        break
                    except requests.exceptions.Timeout:
                        print('Connection Timed out, trying again in 5 seconds')
                        time.sleep(5)
                    else:
                        directory = f'{lyric_directory}/{song["artist"]}/{song["album"]}/'
                        if int(song['totaldiscs']) > 1:
                            directory += f'CD {song["discnumber"]}/'
                        while True:
                            try:
                                file_name = f'{song["tracktitle"]}'
                                final_name = ''
                                for i in file_name:
                                    if i in illegal_characters:
                                        final_name += '_'
                                    else:
                                        final_name += i
                                file = open(f'{directory}{song["tracknumber"]} {final_name}', 'w')
                            except FileNotFoundError:
                                os.makedirs(directory)
                            else:
                                file.write(lyrics)
                                file.close()
                                break
                        break
        else:
            print(f'Checking Sub-Directory \"{file}\"')
            get_lyrics(music_directory+'/'+file)


get_lyrics(music_directory)
