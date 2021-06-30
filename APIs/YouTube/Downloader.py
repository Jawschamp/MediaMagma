import asyncio

from youtube_dl import YoutubeDL

from FileOperations.FileOperations import *

class YTLData:
    song_id = "svFVstOPi_A"
    video_link = "https://www.youtube.com/watch?v={}".format(song_id)
    with YoutubeDL({'format': 'mp4'}) as ydl:
        video_info = ydl.extract_info(video_link, download=False)
        ydl.download([video_link])
        title = video_info.get('title', None)
        print(title)

    def get_data():
        everything = YTLData.title + "-" + YTLData.song_id + ".mp4"
        return everything
