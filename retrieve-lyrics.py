import requests
from bs4 import BeautifulSoup as bs
import os

artist = input("Enter artist name: ")
artistIndex = artist.replace(" ", "").lower()
#print (artist)

song = input("Enter song title: ")
songIndex = song.replace(" ", "").lower()
#print (song)

url = "https://www.azlyrics.com/lyrics/" + artistIndex + "/" + songIndex + ".html"

# download page for parsing
page = requests.get(url)
soup = bs(page.text, "html.parser")

# scrape lyrics off page
song_lyrics = soup.findAll("div", {"class": None, "id": None})

# create directory for lyrics
if not os.path.exists("song-lyrics"):
    os.makedirs("song-lyrics")

# move to new directory
os.chdir("song-lyrics")

# write lyrics onto text file
for lyrics in song_lyrics:
    try:
        with open(song + '-lyrics.text', 'w') as f:
            f.write(song.upper() + " by " + artist.upper())
            f.write(lyrics.text)
        f.close()
    except:
        pass
