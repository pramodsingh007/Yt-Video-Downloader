from pytube import YouTube
from pathlib import Path




class YtDownloader():
    def __init__(self,link):
        self.yt = YouTube(link)
        self.title = self.yt.title
        self.thumbnail = self.yt.thumbnail_url
        self.id = self.yt.video_id
        self.downloads_path = str(Path.home() / "Downloads")

    def Download_video(self):
        try:
            self.mp4 = self.yt.streams.get_highest_resolution().download(output_path=self.downloads_path)
        except:
            print("Failed to download")

    
    def Download_audio(self):
        try:
            self.mp4 = self.yt.streams.get_audio_only().download(output_path=self.downloads_path)

        except:
            print("Failed to Download")




