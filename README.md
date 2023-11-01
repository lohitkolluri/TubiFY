# TubiFY: Spotify Playlist to YouTube Downloader

TubiFY is a Python script that enables you to convert your Spotify playlists into YouTube links and download the corresponding audio or video. You can choose to download all tracks as audio, all tracks as video, or make a custom choice for each track. The script also provides an option to skip tracks.

## Prerequisites

Before you can use TubiFY, you need to set up your environment and obtain the necessary credentials:

1. **Spotify API Credentials**: You'll need a Spotify API client ID and client secret. Create a Spotify Developer application to obtain these credentials.

2. **YouTube API Key**: You'll need a YouTube Data API key. Follow the Google API Console's instructions to create a project and obtain an API key.

3. **Python Libraries**: Make sure to install the required Python libraries using `pip`:

   ```bash
   pip install spotipy google-api-python-client pytube python-dotenv
   ```

## Configuration

1. Create a `.env` file in the same directory as your script and add the following environment variables:

   ```env
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   YOUTUBE_API_KEY=your_youtube_api_key
   ```

2. Configure the `redirect_uri` for Spotify OAuth to 'http://localhost:8888/callback' in your Spotify Developer application settings.

## Usage

1. Run the script by executing it in your terminal:

   ```bash
   python TubiFY.py
   ```

2. The script will prompt you to enter the following information:

   - The number of playlists to process.
   - Download choice: 'aa' for audio, 'av' for video, 'custom' to make a custom choice, or 's' to skip tracks.

3. Follow the script's instructions to enter the Spotify playlist URLs.

4. The script will process the playlists, find YouTube links for the tracks, and download the selected audio or video files.

5. All YouTube links will be saved to a `youtube_links.txt` file in the script's directory.
