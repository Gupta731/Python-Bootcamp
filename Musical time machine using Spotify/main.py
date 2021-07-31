import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
REDIRECT_URL = 'http://example.com'
BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100'

user_date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
year = user_date.split('-')[0]
track_uris = []


def scrap_top_100_songs():
    response = requests.get(f'{BILLBOARD_URL}/{user_date}')
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    songs = soup.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')
    return [song.text for song in songs]


def auth_spotify_user():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                   client_secret=SPOTIFY_CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URL,
                                                   scope='playlist-modify-private',
                                                   show_dialog=True,
                                                   cache_path='token.txt'))
    return sp


def get_song_uri():
    for track in songs_list:
        try:
            track_info = spotify_user.search(q=f'track:{track} year: {year}', type='track', limit=1, offset=0)
            track_uri = track_info["tracks"]["items"][0]["uri"]
            track_uris.append(track_uri)
            print(f'{track_uri}')
        except:
            print(f"{track} doesn't exist in Spotify. Skipped.")
            continue


def add_songs_to_playlist():
    playlist = spotify_user.user_playlist_create(user=spotify_user.current_user()['id'],
                                                 name=f'{user_date} Billboard 100',
                                                 public=False,
                                                 collaborative=False,
                                                 description=f'{user_date} Billboard 100')
    spotify_user.playlist_add_items(playlist_id=playlist['id'], items=track_uris)


songs_list = scrap_top_100_songs()
spotify_user = auth_spotify_user()
get_song_uri()
add_songs_to_playlist()
