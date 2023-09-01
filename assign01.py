from pytube import YouTube
video_url = 'https://www.youtube.com/watch?v=BsqrmY91nUQ'
try:
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    output_path = "downloaded_video.mp4"
    stream.download(output_path=output_path)
    print("Video downloaded successfully!")
except Exception as e:
    print(f"An error occurred: {str(e)}")