import ytmp3 
from tkinter import *
from tkinter import ttk
import os

root = Tk()
root.title("Youtube to MP3")

root.geometry("500x300")
root.resizable(0,0)

title = Label(root, text="Youtube to MP3", font=("Arial", 20))
url = Label(root, text="URL: ", font=("Arial", 15))
input = Entry(root, width=30, font=("Arial", 15))
download_button = Button(root, text="Download", font=("Arial", 15), command=lambda: ytmp3.download(input.get()))

title.pack(pady=10)
url.pack()
input.pack(pady=10)
download_button.pack()

if not os.path.exists("mp3/"):
    os.mkdir("mp3/")


