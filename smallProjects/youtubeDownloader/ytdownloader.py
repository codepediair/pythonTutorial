from pytube import YouTube
yt = YouTube('http://youtube.com/watch?v=CywxLAL2K7w')
# res = yt.streams.filter(file_extension='mp4')

stream = yt.streams.get_by_itag(137)
stream.download()
# print(res)
