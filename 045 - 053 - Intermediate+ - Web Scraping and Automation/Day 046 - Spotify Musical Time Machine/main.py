import requests
import spotipy
from bs4 import BeautifulSoup
from auth import *
from spotipy.oauth2 import SpotifyOAuth


breaker = True
url_base = "https://www.billboard.com/charts/hot-100/"
day_to_get = "2020-10-16"

def checkdate(date):
    try:
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
    except:
        return True
    if len(date)>10 or month <= 0 or month > 12 or day <= 0 or day > 31 or year < 1950 or year > 2022 or date[4] != "-" or date[7] != "-":
        print("Invalid Input.\n")
        return True
    return False

while breaker:
    day_to_get = input("What date would you like a Spotify playlist for? (YYYY-MM-DD): ")
    breaker = checkdate(day_to_get)

page_data = requests.get(url_base+day_to_get+"/")
soup = BeautifulSoup(page_data.text, "html.parser")

songs = soup.select(selector="li h3", class_="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet")

song_titles = [song.getText().strip() for song in songs[:100]]

bad_data = ['Log Out', 'Log Out', 'Share this article on Facebook', 'Share this article on Twitter',
            'Share this article on Tumblr', 'Share this article on Pinit', '+ additional share options added',
            'Share this article on Reddit', 'Share this article on Linkedin', 'Share this article on Whatsapp',
            'Share this article on Email', 'Print this article', 'Share this article on Comment', 'NEW', '-', 'RE-\nENTRY']
for each in range(0,101):
    bad_data.append(str(each))
artists = soup.select(selector="li span")
artist_list = [artist.getText().strip() for artist in artists if artist.getText().strip() not in bad_data]
artist_list = artist_list[:100]

#print(artist_list)

playlist_name = "Hot 100 for "+day_to_get
playlist_description = "Billboard.com Hot 100 for "+day_to_get+" playlist by RamenJunkie"

scopes = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scopes,
                                               cache_path="token.txt"))


pl_response = sp.user_playlist_create(user=SPOTIFY_USERNAME,name=playlist_name,public=False,description=playlist_description)
pl_id = pl_response['id']

all_track_ids = []
year = day_to_get.split("-")[0]
for each in range(0, 100):
    artist = artist_list[each]
    track = song_titles[each]
    result = sp.search(q=f"track:{track} year:{year}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        all_track_ids.append(uri)
    except IndexError:
        print(f"{track} doesn't exist in Spotify. Skipped.")

#print(all_track_ids)
sp.playlist_add_items(playlist_id=pl_id, items=all_track_ids)






#  1979-12-23