from youtube_transcript_api import YouTubeTranscriptApi as yt

video_id=input("Enter the YouTube link, make sure subtitles are available\n").split('v=')[1]
print(video_id)
dicts=yt.get_transcript(video_id)
txt=''
for dict in dicts:
    txt+=f"{dict['text']}"
    
with open('transcript.txt', 'w+') as f:
    f.write(txt)

