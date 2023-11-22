import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Load environment variables from the .env file
load_dotenv()

# Constants
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

class YouTubePlaylistCreator:
    def __init__(self):
        self.api_key = YOUTUBE_API_KEY
        self.youtube = self.youtube = self.authenticate_youtube()
        self.playlist_id = None
    
    def authenticate_youtube(self):
        """Authenticate with YouTube using OAuth2."""
        credentials_path = './credentials.json'  # Replace with your credentials file path

        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
        credentials = flow.run_local_server(port=8080)

        return build('youtube', 'v3', credentials=credentials)

    def create_playlist(self, title, description=''):
        """Create a YouTube playlist."""
        try:
            playlist_response = self.youtube.playlists().insert(
                part='snippet,status',
                body={
                    'snippet': {
                        'title': title,
                        'description': description
                    },
                    'status': {
                        'privacyStatus': 'public'
                    }
                }
            ).execute()

            self.playlist_id = playlist_response['id']
            print(f'Playlist "{title}" created successfully. Playlist ID: {self.playlist_id}')

        except HttpError as e:
            print(f'An error occurred: {e}')

    def add_video_to_playlist(self, video_id):
        """Add a video to the YouTube playlist."""
        if not self.playlist_id:
            print("Error: Playlist not created.")
            return

        try:
            self.youtube.playlistItems().insert(
                part='snippet',
                body={
                    'snippet': {
                        'playlistId': self.playlist_id,
                        'resourceId': {
                            'kind': 'youtube#video',
                            'videoId': video_id
                        }
                    }
                }
            ).execute()

            print(f'Video with ID {video_id} added to the playlist successfully.')

        except HttpError as e:
            print(f'An error occurred: {e}')

