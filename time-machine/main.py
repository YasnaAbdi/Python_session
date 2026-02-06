from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import date

SPOTIPY_CLIENT_ID = "bfdab240b4104b83a7b8d90859ebc86b"
SPOTIPY_CLIENT_SECRET = "c22dd3d402fe4e5489293bfd76bd6150"
URL = "https://example.com/?code=AQDcwiD223VCm2vgkfPydeJwO0ybo2AjeP4FC1HW4CXHQR9Lv94UoQxr1DulAT0S9n1s361wkdHVzFXmrB8F0S5GhDVvCS0tpxeoA2wPbZwigyEZopzkYSVjqMLdo6HW0wmNG15BUHZHz5vodapgte43CLUZJWB1Pr1PRTtKxheDLU8PxWFz1dFCZ7XFmGc"
SPOTIFY_URL = "http://open.spotify.com/track/"

spotify_endpoint = "https://www.billboard.com/charts/hot-100/"

response = requests.get(url=(spotify_endpoint + requirement))
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song_name_span = soup.select("li ul li h3")
song_name = [song.getText().strip() for song in song_name_span]

#step2
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="yasnaabdi",
    )
)

user_id = sp.current_user()["id"]
requirement = input("what year you would like to travel to? Type in YYY-MM-DD format: ")
song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]

#step3


year = date.split("-")[0]
for song in song_name:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")




