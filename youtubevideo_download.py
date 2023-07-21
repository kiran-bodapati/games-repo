from pytube import YouTube       #importing youtube method from pytube module
link=input("enter an youtube link to be downloaded")     #Taking   video link as input from the 
youtube_1=YouTube(link)       #providing link as an argument to the youtube() method
print(youtube_1.title)        #gives  the title of the link/video
print(youtube_1.thumbnail_url)   #gives the thumbnail of the video
videos=youtube_1.streams.all()     #gets the video links' full details like with 144p,360p etc
vid=list(enumerate(videos))      #coverts the above details in form of a list
for i in vid:
    print(i)                    #prints all the details in the above list
print()
strm=int(input("enter: "))      #entering the index number of the above list to download a particular video
videos[strm].download()        #The video is downloaded with the name of this file
print("successfull")
