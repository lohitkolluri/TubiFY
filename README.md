<h1 align="center" id="title">TubiFy</h1>

<p id="description">TubiFY is a Python script that converts your favorite Spotify playlists into YouTube links providing easy access to both music and videos. It leverages the Spotify API to fetch track information and the YouTube Data API to search for corresponding music videos. You can customize the download format and choose between audio or video downloads.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Easily convert Spotify playlists to YouTube links.
*   Choose between audio (MP3) and video (MP4) downloads.
*   Customize the download format for each track.
*   Progress bar for tracking playlist processing (requires tqdm).

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone this repository or download the script (tubify.py) to your local machine.</p>

```
git clone https://github.com/lohitkolluri/TubiFY.git
```

<p>2. Install the required Python packages using pip:</p>

```
pip install -r requirements.txt
```

<p>3. Create a .env file in the same directory as tubify.py and add the following credentials:

   ```
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   YOUTUBE_API_KEY=your_youtube_api_key
   ```

   Replace `your_spotify_client_id`, `your_spotify_client_secret`, and `your_youtube_api_key` with your respective API keys.

<p>4. Run TubiFY by executing the following command in your terminal:</p>

```
 python3 tubify.py
```

<h2>⚙️ Usage</h2>

- Enter the number of playlists to process.

- Choose the download option:
  - `aa`: Download all tracks as audio (MP3).
  - `av`: Download all tracks as video (MP4).
  - `custom`: Customize the download format for each track.
  - `skip`: Skip the download process.

- For each playlist, provide the Spotify playlist URL and follow the on-screen prompts to complete the process.

- TubiFY will create a file named `youtube_links.txt` that contains the YouTube links for the tracks.
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   Spotipy
*   GoogleAPIClient
*   Pytube
*   DotENV

<h2>🛡️ License:</h2>

This project is licensed under the [MIT License](LICENSE)
