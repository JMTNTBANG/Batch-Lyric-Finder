# Batch Lyric Finder
Will use the Genius API to pull lyrics for a bunch of songs from a directory and export them as text files

## Prerequisites

Have the following installed on your system:

1. **[Python 3.10+](https://www.python.org/downloads/)**
2. **[Pip](https://pip.pypa.io/en/stable/installation/)**
3. And an IDE of your own choice (**[PyCharm](https://www.jetbrains.com/pycharm/)** or **[VS-Code](https://code.visualstudio.com/)** is recommended)

## Required Pip Packages

Using **[Pip](https://pip.pypa.io/en/stable/installation/)**, please install the following packages: 

1. **[lyricsgenius](https://pypi.org/project/lyricsgenius/)**
2. **[python-dotenv](https://pypi.org/project/python-dotenv/)**

## Configuration

In order to use the script, you will need to create an account on **[genius.com](https://genius.com)** and **[create an API Client](https://genius.com/api-clients/new)**

Once you have done that, you will need to copy the access token and paste it into a .env file in the top directory. Make sure the file contains the following:

```bash
TOKEN={YOUR ACCESS TOKEN HERE}
```