import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build
from urllib.parse import urlparse
import time
from pytube import YouTube
import logging
from tqdm import tqdm

# Load credentials from .env
load_dotenv()

# Initialize logging
logging.basicConfig(filename='tubify.log', level=logging.INFO)

# Initialize Spotify API client
def init_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri='http://localhost:8888/callback',
        scope='user-library-read playlist-read-private'
    ))

# Initialize YouTube Data API client
def init_youtube_client():
    youtube_api_key = os.getenv("YOUTUBE_API_KEY")
    return build('youtube', 'v3', developerKey=youtube_api_key)

# Output directories for downloaded files
mp3_output_directory = "downloaded_files/MP3"
mp4_output_directory = "downloaded_files/MP4"

# Initialize YouTube client
youtube = init_youtube_client()

# Function to create directories if they don't exist
def create_directories():
    if not os.path.exists(mp3_output_directory):
        os.makedirs(mp3_output_directory)
    if not os.path.exists(mp4_output_directory):
        os.makedirs(mp4_output_directory)

def get_youtube_link(track_name, artist_name):
    search_query = f'{track_name} {artist_name} official music video'
    search_response = youtube.search().list(q=search_query, type='video', part='id').execute()

    if 'items' in search_response:
        video_id = search_response['items'][0]['id']['videoId']
        youtube_link = f'https://www.youtube.com/watch?v={video_id}'
        return youtube_link
    return None

def download_media(youtube_link, track_name, artist_name, is_audio=True):
    try:
        yt = YouTube(youtube_link)
        # Get the stream based on audio or video preference
        stream = yt.streams.filter(only_audio=is_audio).first() if is_audio else yt.streams.get_highest_resolution()

        if not stream:
            logging.error(f"No suitable {'audio' if is_audio else 'video'} stream found for: {track_name} by {artist_name}")
            return False

        extension = 'mp3' if is_audio else 'mp4'
        file_name = f"{track_name} by {artist_name}.{extension}"
        output_directory = mp3_output_directory if is_audio else mp4_output_directory
        stream.download(output_path=output_directory, filename=file_name)
        return True
    except Exception as e:
        logging.error(f"Failed to download {'audio' if is_audio else 'video'}: {e}")
        return False

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

def process_playlist(playlist_url, output_file, download_choice):
    # Extract the playlist ID from the URL
    playlist_id = get_playlist_id_from_url(playlist_url)

    if playlist_id:
        sp = init_spotify_client()
        # Fetch playlist tracks
        playlists = sp.playlist_tracks(playlist_id)

        with open(output_file, "a") as file:
            for track in tqdm(playlists['items'], desc="Processing", unit="track"):
                track_name = track['track']['name']
                artist_name = track['track']['artists'][0]['name']
                youtube_link = get_youtube_link(track_name, artist_name)
                if youtube_link:
                    file.write(f"Track: {track_name} by {artist_name}\n")
                    file.write(f"YouTube Link: {youtube_link}\n")
                    file.write("\n")
                    logging.info(f"Processed: {track_name} by {artist_name}")

                    if download_choice == "aa" or (download_choice == "custom" and input("Download as audio (a), video (v), or skip (s): ").lower() == "a"):
                        success = download_media(youtube_link, track_name, artist_name, is_audio=True)
                        if success:
                            logging.info(f"Downloaded audio (MP3) for: {track_name} by {artist_name}")
                    elif download_choice == "av" or (download_choice == "custom" and input("Download as audio (a), video (v), or skip (s): ").lower() == "v"):
                        success = download_media(youtube_link, track_name, artist_name, is_audio=False)
                        if success:
                            logging.info(f"Downloaded video (MP4) for: {track_name} by {artist_name}")
                else:
                    logging.warning(f"Track not found on YouTube: {track_name} by {artist_name}")
        return True
    else:
        logging.error("Invalid or unsupported Spotify playlist URL. Please check the URL format.")
        return False

def main():
    create_directories()  # Create the output directories

    num_playlists = int(input("Enter the number of playlists to process: "))
    download_choice = input("Download all tracks as audio (aa), all tracks as video (av), custom (c), or skip (s): ")
    output_file = "youtube_links.txt"

    for i in range(num_playlists):
        playlist_url = input(f"Enter the Spotify playlist URL {i + 1}: ")
        success = process_playlist(playlist_url, output_file, download_choice)
        if not success:
            logging.warning(f"Failed to process playlist: {playlist_url}")

        # Add a delay to avoid hitting API rate limits
        time.sleep(2)

    print(f"MP3 files have been saved to {mp3_output_directory}")
    print(f"MP4 files have been saved to {mp4_output_directory}")

if __name__ == "__main__":
    main()