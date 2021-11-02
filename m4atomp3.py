"""from pydub import AudioSegment
print(1)
wav_audio = AudioSegment.from_file("audio.m4a", format="m4a")
print(2)
wav_audio.export("audio1.mp3", format="mp3")"""

from __future__ import unicode_literals
import youtube_dl
file1 = file1 = open("audio.txt","r+")
links = file1.readlines()

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
for i in range(78,len(links)):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([links[i][:43]])
"""
from pytube import YouTube
import os

yt = YouTube('https://www.youtube.com/watch?v=S1T1jGLSgZ4')

video = yt.streams.filter(only_audio=True).first()

out_file = video.download(output_path=".")

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
"""
