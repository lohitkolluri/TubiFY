import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs
import time

# Load credentials from .env
load_dotenv()

# Initialize Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri='http://localhost:8888/callback',
    scope='user-library-read playlist-read-private'
))

# Initialize YouTube Data API client
youtube_api_key = os.getenv("YOUTUBE_API_KEY")
youtube = build('youtube', 'v3', developerKey=youtube_api_key)

def get_youtube_link(track_name, artist_name):
    search_query = f'{track_name} {artist_name} official music video'
    search_response = youtube.search().list(q=search_query, type='video', part='id').execute()

    if 'items' in search_response:
        video_id = search_response['items'][0]['id']['videoId']
        youtube_link = f'https://www.youtube.com/watch?v={video_id}'
        return youtube_link
    return None

def get_playlist_id_from_url(playlist_url):
    # Remove query parameters from the URL
    clean_url = playlist_url.split('?')[0]

    # Initialize playlist_id with None
    playlist_id = None

    # Parse the clean playlist URL to extract the playlist ID
    parsed_url = urlparse(clean_url)
    if parsed_url.netloc == "open.spotify.com":
        path_segments = parsed_url.path.split('/')
        if len(path_segments) >= 3 and path_segments[1] == "playlist":
            playlist_id = path_segments[2]
    return playlist_id

def process_playlist(playlist_url, output_file):
    # Extract the playlist ID from the URL
    playlist_id = get_playlist_id_from_url(playlist_url)

    if playlist_id:
        # Fetch playlist tracks
        playlists = sp.playlist_tracks(playlist_id)

        with open(output_file, "a") as file:
            for track in playlists['items']:
                track_name = track['track']['name']
                artist_name = track['track']['artists'][0]['name']
                youtube_link = get_youtube_link(track_name, artist_name)
                if youtube_link:
                    file.write(f"Track: {track_name} by {artist_name}\n")
                    file.write(f"YouTube Link: {youtube_link}\n")
                    file.write("\n")
                    print(f"Processed: {track_name} by {artist_name}")
                else:
                    print(f"Track not found on YouTube: {track_name} by {artist_name}")
        return True
    else:
        print("Invalid or unsupported Spotify playlist URL. Please check the URL format.")
        return False

def main():
    output_file = "youtube_links.txt"

    num_playlists = int(input("Enter the number of playlists to process: "))
    
    for i in range(num_playlists):
        playlist_url = input(f"Enter the Spotify playlist URL {i + 1}: ")
        success = process_playlist(playlist_url, output_file)
        if not success:
            continue

        # Add a delay to avoid hitting API rate limits
        time.sleep(2)

    print(f"YouTube links have been saved to {output_file}")

if __name__ == "__main__":
    main()
