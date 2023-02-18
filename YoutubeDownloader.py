import sys
from pathlib import Path
from pytube import YouTube

def main():
    link = input("Youtube Video URL: ")
    title = input("Give a title: ")
    video_downloader = YouTube(link, on_progress_callback = progress_function)

    print("Download in progress")

    output_path = str(Path.home() / "Downloads")
    filename = f"{title}.mp4"
    video_downloader.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution().download(output_path=output_path, filename=filename)

    print("Video downloaded", link)


def progress_function(chunk, file_handle, bytes_remaining):
    filesize = chunk.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()


if __name__=="__main__":
    main()
