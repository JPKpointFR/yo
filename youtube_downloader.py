# Projet "Youtube Downloader"

import os
from pytube import YouTube
# import ffmpeg


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downlowded = stream.filesize - bytes_remaining
    percent = bytes_downlowded*100/stream.filesize

    print(f"Progression du téléchargement: {int(percent)}%")


def download_video(url):

    youtube_video = YouTube(url)

    youtube_video.register_on_progress_callback(on_download_progress)

    print(f"TITRE: {youtube_video.title}")
    # print(f"NB VUES: {youtube_video.views}")

    # print("")
    # print("STREAMS")
    streams = youtube_video.streams.filter(
        progressive=False, file_extension='mp4', type="video").order_by('resolution').desc()
    video_stream = streams[0]

    streams = youtube_video.streams.filter(
        progressive=False, file_extension='mp4', type="audio").order_by('abr').desc()
    audio_stream = streams[0]

    # print(video_stream)
    # print(audio_stream)

    print("Téléchargement...")
    video_stream.download()
    print("OK")
