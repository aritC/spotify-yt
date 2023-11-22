import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

class SpotifyPlaylistReader:
    def __init__(self, playlist_id):
        load_dotenv()
        self.playlist_id=playlist_id
        self.playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
        self.spotipy_client_id = os.getenv('SPOTIPY_CLIENT_ID')
        self.spotipy_client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
        self.tracks = []

    def authenticate_spotify(self):
        """Authenticate with Spotify using client credentials."""
        client_credentials_manager = SpotifyClientCredentials(
            client_id=self.spotipy_client_id, 
            client_secret=self.spotipy_client_secret
        )
        return spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_playlist_tracks(self):
        """Get the tracks from a Spotify playlist."""
        sp = self.authenticate_spotify()

        try:
            # Get the playlist tracks
            results = sp.playlist_tracks(self.playlist_id)
            self.tracks = results['items']
        except spotipy.SpotifyException as e:
            print(f"Error: {e}")

    def print_track_names(self):
        """Print the names of tracks."""
        for track in self.tracks:
            track_name = track['track']['name']
            print(track_name)

    def run(self):
        """Run the script."""
        self.get_playlist_tracks()
        if self.tracks:
            self.print_track_names()
        else:
            print("Failed to retrieve playlist tracks.")
