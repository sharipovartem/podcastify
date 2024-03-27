from flask import Flask
from pytube import YouTube
from pydub import AudioSegment
import requests
from flask import request, render_template
from os import path
import os
import podcastify
from pathlib import Path

app = Flask(__name__)
url = ''

@app.route("/podcastify/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        url = request.form.get("url")
        outdir = 'audio'
        podcastify.podcastify(url, outdir)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="localhost", port=8088, debug=True)
##curl "localhost:8000/podcastify?link"