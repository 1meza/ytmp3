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
    download = yt_vid.order_by('resolution').desc().first().download()
    print("video downloaded", download)
    
    convert_mp3(download)
    remove(download)

def remove(download: str):
    if os.path.isfile(download):
        os.remove(download)
    else:
        print("Error: %s file not found" % download)


if __name__ == '__main__':
    downloader(sys.argv[1])
    
