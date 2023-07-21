from pytube import Playlist
py=Playlist("https://www.youtube.com/watch?v=6i3EGqOBRiU&list=PLdo5W4Nhv31bZSiqiOL5ta39vSnBxpOPT&ab_channel=Jenny%27sLecturesCSIT")
print(f"Downloading:{py.title}")       #prints the title of the playlist
for video in py.videos:
    video.streams.first().download()  #downloads the playlist
