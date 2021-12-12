"""
    Code by: SALMAN MALLAH
    Project: Youtube Video downloader!
"""
from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=Ige-YPaQQRQ')
vid_title  = yt.title
vid_url = yt.thumbnail_url

# stile working on it