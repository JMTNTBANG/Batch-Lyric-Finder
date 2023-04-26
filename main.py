from dotenv import load_dotenv
from os import getenv
from lyricsgenius import Genius

load_dotenv()
token = getenv('ACCESS_TOKEN')
if token is None:
    raise ValueError('Please Paste your Access Token in the .env file')
try:
    genius = Genius(token)
except TypeError:
    raise ValueError('Please try a new Access Token as this one did not work...')

