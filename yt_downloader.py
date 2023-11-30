from pytube import YouTube

option = 5
link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
print("Paste the link here:")
link = input()
yt = YouTube(link)
print("Options:")
print("1. Video")
print("2. Audio")
while option != 1 and option != 2:
 option = input()
 if option == '1':
  ytdownload = yt.streams.get_highest_resolution()
  ytdownload.download(r'C:\Users\jmtro\Videos\Youtube Downloads')
  break
 elif option == '2': 
  ytdownload = yt.streams.get_audio_only()
  ytdownload.download(r'C:\Users\jmtro\Music\YT Music')
  break
 else:
  print("Please select a valid input:")