import spotipy
import secrets
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secrets.client_id,
                                               client_secret=secrets.client_secret,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read user-top-read playlist-modify-public playlist-modify-private"))

playlist_id = secrets.playlist_id
newTracks = []
i = 0

while i < 10000:
    results = sp.current_user_saved_tracks(limit=50, offset=i)
    for idx, item in enumerate(results['items']):
        track = item['track']
        newTracks.append(track['id'])

    sp.playlist_replace_items(playlist_id, newTracks)

    i = i + 50
    print("done:",i)
