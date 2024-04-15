import requests
from pytube import YouTube
from pydub import AudioSegment
import requests
from os import path
import os
from pathlib import Path


outdir = 'audio'
def podcastify (url,outdir):
    # url = requests.get('link')
    # url input from user
    yt = YouTube(url)

    ##@ Extract audio with 160kbps quality from video
    video = yt.streams.filter(abr='160kbps').last()

    ##@ Downloadthe file
    out_file = video.download(output_path=outdir)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.mp3')
    os.rename(out_file, new_file)
    ##@ Check success of download
    if new_file.exists():
        print(f'{yt.title} has been successfully downloaded.')
    else:
        print(f'ERROR: {yt.title}could not be downloaded!')

# podcastify("https://www.youtube.com/watch?v=jhFDyDgMVUI&ab_channel=WaitOneSecondHere", outdir)

