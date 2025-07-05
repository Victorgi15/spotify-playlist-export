import requests
from typing import List, Dict
from auth import get_auth_header

def list_all_songs_in_playlist(playlist_id: str, token: str) -> List[Dict[str, str]]:
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_auth_header(token)
    songs: List[Dict[str, str]] = []

    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Erreur API: {response.status_code}")
            break
        data = response.json()
        for item in data['items']:
            track = item['track']
            title: str = track['name']
            artists: str = ", ".join(artist['name'] for artist in track['artists'])
            songs.append({'Titre': title, 'Artistes': artists})
        url = data['next']

    return songs
