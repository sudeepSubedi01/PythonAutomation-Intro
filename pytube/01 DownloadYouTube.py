from pytube import YouTube    #YouTube is a class

url = 'https://youtu.be/0bfk90rWV9U?list=RDxdcIwXC_Ouk'
yt = YouTube(url) 	    #instantiation of YouTube class; yt has access to streams, captions,title,length... of the video

print('Title: ', yt.title)
print('Views: ', yt.views)
print('Description: ', yt.description)
print('Author: ', yt.author)
print('Length: ', yt.length)
print('Streams: ',yt.streams)

# stream = yt.streams.get_highest_resolution()
stream = yt.streams.filter(only_audio=False).first()

stream.download('C:\\Users\\Acer1\\Pictures\\D drive files',filename='got.mp4')
print('Done')

#streams is an attribute of YouTube object that is an instance of StreamQuery class
#get_highest_resolution() is a method inside StreamQuery class