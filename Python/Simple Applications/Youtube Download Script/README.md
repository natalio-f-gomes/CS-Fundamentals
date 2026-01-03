# Downloader


A Python script that allows you to download YouTube videos and entire playlists to your local machine. The script ensures that videos are not downloaded twice and gracefully skips age-restricted content that can't be accessed without authentication.

### Prerequisites

1. Python installed on your machine.
2. [pytube](https://pypi.org/project/pytube/) library. Install it via pip:

```bash
pip install pytube
```

### Usage

1. Clone or download this repository to your machine.
2. Open the terminal and navigate to the directory containing the script.
3. Run the script:

```bash
python your_script_name.py
```

4. When prompted, provide a download path or press enter to use the default path (`Videos/`).

### Features

- **Individual Video Download**: Downloads individual YouTube videos.
  
- **Playlist Download**: Downloads all videos in a YouTube playlist.

- **Avoids Redundancy**: Ensures that a video isn't downloaded more than once, even if it's part of multiple playlists provided.

- **Handles Age-Restricted Content**: Skips age-restricted videos that require authentication to access.

### Adding/Modifying Video Links

The `links` list within the script contains the YouTube URLs you want to download. To download different content, replace or modify this list with the desired YouTube video or playlist URLs.

### Known Limitations

- Age-restricted content can't be downloaded without logging in. Such videos will be skipped.

- Videos that are unavailable or have been deleted from YouTube will result in an error.

### Contributing

Feel free to fork this repository, make changes, and submit pull requests. Any kind of contribution is welcome!

