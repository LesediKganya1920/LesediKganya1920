import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

# Function to download the video
def download_video():
    try:
        url = url_entry.get()
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download()
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create UI components
label = tk.Label(root, text="Enter YouTube Video URL:")
label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

download_button = tk.Button(root, text="Download Video", command=download_video)
download_button 