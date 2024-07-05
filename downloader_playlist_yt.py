import os
import sys
from pytube import Playlist


def make_alpha_numeric(string):
    return "".join(char for char in string if char.isalnum())


def download_file(link):
    yt_playlist = Playlist(link)
    folderName = make_alpha_numeric(yt_playlist.title)
    os.mkdir(folderName)
    totalVideoCount = len(yt_playlist.videos)
    print("Total videos in playlist: 🎦", totalVideoCount)
    for index, video in enumerate(yt_playlist.videos, start=1):
        print("Downloading:", video.title)
        video_size = video.streams.get_highest_resolution().filesize
        print("Size:", video_size // (1024**2), "🗜 MB")
        video.streams.filter(only_audio=True, mime_type="audio/mp4").order_by(
            "abr"
        ).desc().first().download(output_path=folderName)
        print("Downloaded:", video.title, "✨ successfully!")
        print("Remaining Videos:", totalVideoCount - index)
    print("All videos downloaded successfully! 🎉")


def load_links_from_file(file):
    with open(file, "r") as file:
        links = file.readlines()
    return links


def main(file_links):
    links = load_links_from_file(file_links)
    for link in links:
        download_file(link)


if __name__ == "__main__":
    # read name file from argument
    file = sys.argv[1]
    main(file)
    print("All playlist downloaded successfully! 🎉")


# link = input("Enter YouTube Playlist URL: ✨")

# yt_playlist = Playlist(link)

# folderName = make_alpha_numeric(yt_playlist.title)
# os.mkdir(folderName)

# totalVideoCount = len(yt_playlist.videos)
# print("Total videos in playlist: 🎦", totalVideoCount)

# for index, video in enumerate(yt_playlist.videos, start=1):
#     print("Downloading:", video.title)
#     video_size = video.streams.get_highest_resolution().filesize
#     print("Size:", video_size // (1024**2), "🗜 MB")
#     # video.streams.get_highest_resolution().download(output_path=folderName)
#     video.streams.filter(only_audio=True, mime_type="audio/mp4").order_by(
#         "abr"
#     ).desc().first().download(output_path=folderName)

#     print("Downloaded:", video.title, "✨ successfully!")
#     print("Remaining Videos:", totalVideoCount - index)

# print("All videos downloaded successfully! 🎉")
