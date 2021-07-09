# Youtube Downloader using Python 

from pytube import YouTube

link = input("Enter your YouTube URL: ")
yt = YouTube(link)
videos = yt.streams.all()


video = list(enumerate(videos))

for i in video:
    print(i)

print("Enter the desired option to downlod the format")
dn_option = int(input("Enter the Option: "))
dn_video = videos[dn_option]
dn_video.download()

print("Video Downloaded Successfully...")