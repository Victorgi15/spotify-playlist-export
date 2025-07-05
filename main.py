from auth import get_token
from spotify_api import list_all_songs_in_playlist
from exporter import export_as_csv, export_as_json

if __name__ == "__main__":
    playlist_id = "4X3xjeYjdVvEAAZF7tbTsV"  # remplace par ton ID
    token = get_token()
    tracks = list_all_songs_in_playlist(playlist_id, token)
    export_as_csv(tracks, "playlist_export.csv")
    export_as_json(tracks, "playlist_export.json")