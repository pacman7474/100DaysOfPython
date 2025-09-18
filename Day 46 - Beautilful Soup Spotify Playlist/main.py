import os

import requests
import lxml
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth


scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#auth_manager = SpotifyClientCredentials()
#sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()["id"]

playlist_year = "2020-07-24" #input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {'user-agent': "my-app/0.0.1"}

year = playlist_year.split("-")[0]

billboard_url = f"https://www.billboard.com/charts/hot-100/{playlist_year}"
response = requests.get(billboard_url,headers=header)
soup = BeautifulSoup(response.text,"lxml")
#title_anchor = soup.find_all(name="h3",class_=["c-title.a-font-basic"],id="title-of-a-story")
title_anchor = soup.select("h3.c-title.lrv-u-font-size-16")
#print(title_anchor)
titles = [song.getText().strip() for song in title_anchor]
#print(titles)

song_uris = []
#for song in titles:
for i in range(0,4):
    result = sp.search(q=f"track:{titles[i]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doe not exist in Spotify. Skipped")
#print(type(song_uris))
#for i in range(0,4):
#    print(song_uris[i])
playlist = sp.user_playlist_create(user_id,f"{year}-Billboard Top 100",False)
sp.playlist_add_items(playlist["id"],song_uris)
