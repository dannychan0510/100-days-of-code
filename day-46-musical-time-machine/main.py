from datetime import datetime
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import sys

# Get client id and secret from env
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

# Ask for input date
date_str = input(
    "Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: "
)

# URL of the webpage to scrape
url = f"https://www.billboard.com/charts/hot-100/{date_str}"

# Send a GET request to the URL and retrieve the webpage content
r = requests.get(url)

# Extract the HTML content from the response
website = r.text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(website, "html.parser")

song_containers = soup.find_all("div", class_="o-chart-results-list-row-container")

song_list = []
artist_list = []

for song_container in song_containers:
    song_list.append(song_container.find_next("h3").text.strip())
    artist_list.append(song_container.find_next("h3").find_next("span").text.strip())

# Create Spotify client object
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
    )
)

# Search for top 10 songs
track_uri_list = []
counter = 0

# Iterate through the song_list and artist_list simultaneously
for song, artist in zip(song_list, artist_list):
    # Break the loop if counter reaches 10
    if counter == 10:
        break

    # Create a query string to search for the song and artist on Spotify
    q_string = f"track:{song} artist:{artist}"

    # Search for the query string on Spotify
    results = sp.search(q=q_string)

    # Iterate through the search results and find the first match
    for result in results["tracks"]["items"]:
        # Get the name of the song from the result
        song_result = result["name"]

        # Get the list of artists from the result
        artist_result = [ar["name"] for ar in result["artists"]]

        # Check if the song name and artist name match
        if song_result.lower() == song.lower() and any(
            artist.lower() == a.lower() for a in artist_result
        ):
            # Add the track URI to the track_uri_list
            track_uri_list.append(result["uri"])
            counter += 1
            break

# Get the current user's username
username = sp.current_user()["id"]

# Define the playlist name and details
playlist_name = f"Trial"
playlist_description = f"The top 10 songs according to the Billboard 100 on {date_str}."

# Get all playlists of the current user
playlists = sp.current_user_playlists()

# Find the playlist with the desired name
for pl in playlists['items']:
    if pl['name'] == playlist_name:
        print(f"Playlist '{playlist_name}' already exists.")
        sys.exit()

# If the playlist is not found, create a new one
playlist = sp.user_playlist_create(
    user=username,
    name=playlist_name,
    public=False,
    collaborative=False,
    description=playlist_description,
)

# Add the tracks to the playlist
sp.user_playlist_add_tracks(user=username, playlist_id=playlist['id'], tracks=track_uri_list)
