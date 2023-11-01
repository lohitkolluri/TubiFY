# TubiFY

TubiFY is a Python script that helps you convert your favorite Spotify playlists into YouTube links for easy access to the music and videos. It utilizes the Spotify API to fetch track information and the YouTube Data API to search for corresponding music videos. You can choose to download the audio or video of these tracks or customize the download format.

## Prerequisites

Before using TubiFY, ensure you have the following installed and configured:

- Python 3
- Pip (Python package manager)
- Spotify Developer Account (for API credentials)
- Google Developer Account (for YouTube Data API credentials)
- A Google API Key
- [PyTube](https://python-pytube.readthedocs.io/en/latest/user/install.html) for downloading YouTube videos
- [dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) for Spotify API integration
- [tqdm](https://tqdm.github.io/) for displaying a progress bar (optional)

You can install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Getting Started

1. Clone this repository or download the script (tubify.py) to your local machine.

2. Create a `.env` file in the same directory as tubify.py and add the following credentials:

   ```
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   YOUTUBE_API_KEY=your_youtube_api_key
   ```

   Replace `your_spotify_client_id`, `your_spotify_client_secret`, and `your_youtube_api_key` with your respective API keys.

3. Run TubiFY by executing the following command in your terminal:

   ```bash
   python3 tubify.py
   ```

4. Follow the on-screen prompts to process your Spotify playlists and download the tracks from YouTube.

## Usage

- Enter the number of playlists to process.

- Choose the download option:
  - `aa`: Download all tracks as audio (MP3).
  - `av`: Download all tracks as video (MP4).
  - `custom`: Customize the download format for each track.
  - `skip`: Skip the download process.

- For each playlist, provide the Spotify playlist URL and follow the on-screen prompts to complete the process.

- TubiFY will create a file named `youtube_links.txt` that contains the YouTube links for the tracks.

## Features

- Easily convert Spotify playlists to YouTube links.
- Choose between audio (MP3) and video (MP4) downloads.
- Customize the download format for each track.
- Progress bar for tracking playlist processing (requires tqdm).

## Troubleshooting

If you encounter any issues, please check the following:

- Ensure you have the required dependencies installed.
- Double-check your API credentials and make sure they are correctly stored in the `.env` file.
- Verify that the Spotify playlist URL is in the correct format.
