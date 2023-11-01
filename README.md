# TubiFY

This Python script allows you to convert a Spotify playlist into a list of YouTube links for the songs in that playlist. It uses the Spotify and YouTube Data APIs to retrieve the playlist information and search for corresponding YouTube videos.

## Prerequisites

Before using the script, make sure you have the following:

1. Spotify Developer Account:
   - You need to create a Spotify Developer account and set up a Spotify Application to obtain the necessary API credentials (Client ID and Client Secret).

2. Spotify Redirect URI:
   - Specify a Redirect URI when setting up your Spotify Application. You will use this URI in the script.

3. YouTube Data API Key:
   - Obtain a YouTube Data API Key from the [Google Developers Console](https://console.developers.google.com/).

4. Python Environment:
   - You should have Python 3.x installed on your system.

## Installation

1. Clone the repository or download the script.

2. Install the required Python packages using pip:

   ```
   pip install spotipy google-auth google-auth-httplib2 google-api-python-client python-dotenv
   ```

3. Create a `.env` file in the same directory as the script with the following contents:

   ```plaintext
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   YOUTUBE_API_KEY=your_youtube_api_key
   ```

   Replace `your_spotify_client_id`, `your_spotify_client_secret`, and `your_youtube_api_key` with your actual credentials.

## Usage

1. Run the script using the following command:

   ```
   python tubify.py
   ```

2. You will be prompted to enter the Spotify playlist URL.

3. The script will extract the playlist ID and fetch the playlist's tracks.

4. It will then search for YouTube links for each song and save them to a `youtube_links.txt` file in the same directory.

5. The generated YouTube links will be available in the `youtube_links.txt` file.

## Notes

- The script may not always find the exact official music video on YouTube, so the generated links might not be perfect, but they should be close.
- Ensure that your Spotify Application and Redirect URI are correctly configured in both the script and your Spotify Developer Dashboard.

## Acknowledgments

- This script utilizes the Spotipy library for Spotify API interactions.
- It uses the Google API Client for YouTube Data API requests.
- Created by Lohit Kolluri.