
import os
from pytube import Playlist, YouTube, exceptions

def download_video(video_url, download_path="Videos/", downloaded_videos=set()):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    yt = YouTube(video_url)

    if yt.title in downloaded_videos:
        print(f"Video '{yt.title}' already downloaded. Skipping...")
        return

    try:
        print(f"Downloading video: {yt.title}")
        yt.streams.get_highest_resolution().download(output_path=download_path)
        downloaded_videos.add(yt.title)
    except exceptions.AgeRestrictedError:
        print(f"Video '{yt.title}' is age restricted and cannot be downloaded without logging in. Skipping...")

def download_playlist(playlist_url, download_path="Videos/", downloaded_videos=set()):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    playlist = Playlist(playlist_url)
    for video in playlist.videos:
        if video.title in downloaded_videos:
            print(f"Video '{video.title}' already downloaded. Skipping...")
            continue

        try:
            print(f"Downloading video: {video.title}")
            video.streams.get_highest_resolution().download(output_path=download_path)
            downloaded_videos.add(video.title)
        except exceptions.AgeRestrictedError:
            print(f"Video '{video.title}' is age restricted and cannot be downloaded without logging in. Skipping...")

if __name__ == "__main__":
    links = links = ["https://www.youtube.com/watch?v=JN4mnVLP0rU&pp=ygUVbWlkZGxlIGVhc3QgZXhwbGFpbmVk",

"https://www.youtube.com/watch?v=ty3QbOBj7zI&pp=ygUVbWlkZGxlIGVhc3QgZXhwbGFpbmVk",

"https://www.youtube.com/watch?v=YnOdULpV810&pp=ygUVbWlkZGxlIGVhc3QgZXhwbGFpbmVk",

"https://www.youtube.com/watch?v=iRYZjOuUnlU&pp=ygUVbWlkZGxlIGVhc3QgZXhwbGFpbmVk",

"https://www.youtube.com/watch?v=ghSIIBBj9to&list=PLYYurDCekg22TqTXKqtJKNI7-DJDI-ozL&pp=iAQB",

"https://www.youtube.com/watch?v=llH160HPHRw&pp=ygUOYW1hbGEgZWtwdW5vYmk%3D",

"https://www.youtube.com/watch?v=CxaY6v7Lduo&t=132s&pp=ygUFc3lyaWE%3D",

"https://www.youtube.com/watch?v=zAzZgK_IpQk&t=905s&pp=ygURd2FyZ3JhcGhpY3Mgc3lyaWE%3D",

"https://www.youtube.com/watch?v=5orWgIPj2Iw&list=PLfFTgttNviBqCzygMeMnp3fV_r5hz-DFj&pp=iAQB",

"https://www.youtube.com/watch?v=Pyw0JYz1xlc&list=PLfFTgttNviBrBgFrAgfZUqFdoLqXQagCI&pp=iAQB",

"https://www.youtube.com/watch?v=O2OLdE6peHY&list=PLfFTgttNviBq1UhlrLc8iAiGcQXOGG-6y&pp=iAQB",

"https://www.youtube.com/watch?v=DBG1Wgg32Ok&list=PL5uULy4b0kV78_Vt-Hbf9urhgL9XcgMp2&pp=iAQB",
"https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc",]


    path = input("Enter the download path (default is 'Videos/'): ")
    download_path = path if path else "Videos/"
    downloaded_videos = set()

    for url in links:
        # Check if the link is a playlist link or a single video link
        if "list=" in url:
            download_playlist(url, download_path, downloaded_videos)
        else:
            download_video(url, download_path, downloaded_videos)


