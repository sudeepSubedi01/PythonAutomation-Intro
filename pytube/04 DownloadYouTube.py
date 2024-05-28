from pytube import YouTube

# Specify the URL of the video
url = 'https://www.youtube.com/watch?v=xdcIwXC_Ouk'
yt = YouTube(url)

# Get the highest resolution stream available
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download('D:\\PythonAutomation')
print('Done')