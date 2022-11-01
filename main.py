import youtube_downloader


urls = ["https://youtu.be/kJKyyaFPxkk",
        "https://youtu.be/cuI9_HD6WIk",
        "https://youtube.com/shorts/oGBGHjlvo3A?feature=share"]

for url in urls:
    youtube_downloader.download_video(url)
