from pytube import YouTube
from moviepy.editor import *
import os
import sys

def convert_mp3(video: str):

    vid = VideoFileClip(video)
    mp3Title = video[:-4]+".mp3"
    vid.audio.write_audiofile(mp3Title)
    vid.close()
    print("converted to mp3")

def downloader(url: str):
    yt_vid = YouTube(url).streams.filter(progressive=True)
    download = yt_vid.order_by('resolution').desc().first().download(output_path="mp3/")
    print("video downloaded", download)
    
    convert_mp3(download)
    remove(download)

def remove(download: str):
    if os.path.isfile(download):
        os.remove(download)
    else:
        print("Error: %s file not found" % download)

def playlist_downloader(url: str):
    yt_playlist = YouTube(url).streams.filter(progressive=True)
    for video in yt_playlist:
        download = video.download(output_path="mp3/")
        print("video downloaded", download)
        convert_mp3(download)
        remove(download)

def if_playlist(url: str):
    if "list" in url:
        playlist_downloader(url)
    else:
        downloader(url)

def download(url: str):
    if_playlist(url)

if __name__ == '__main__':
    downloader(sys.argv[1])
    
