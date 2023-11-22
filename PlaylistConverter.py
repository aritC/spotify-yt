from SpotifyPlaylistReader import SpotifyPlaylistReader
from YoutubePlaylistCreator import YouTubePlaylistCreator

class PlaylistConverter:
    def __init__(self, spotify_playlist_id):
        self.spotify_reader = SpotifyPlaylistReader(spotify_playlist_id)
        self.youtube_creator = YouTubePlaylistCreator()

    def run(self):
        """Run the script."""
        # Get tracks from Spotify playlist
        self.spotify_reader.get_playlist_tracks()

        # Create a YouTube playlist
        playlist_title = "S1mple's Spotify Playlist"  # Replace with the desired title
        self.youtube_creator.create_playlist(playlist_title)

        # Add Spotify tracks to the YouTube playlist
        for track in self.spotify_reader.tracks:
            video_id = track['track']['external_urls']['youtube']
            self.youtube_creator.add_video_to_playlist(video_id)

if __name__ == "__main__":
    # Replace 'your_spotify_playlist_id' with actual value
    spotify_playlist_id = '31yAukRQGxqF1b0eC4RwT8'

    manager = PlaylistConverter(spotify_playlist_id)
    manager.run()