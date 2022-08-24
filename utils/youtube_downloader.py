# Youtube downloader script 220722
""" creates a function that can be run from terminal followed by a youtube url

    example:
        python3 /Users/simon/Documents/Projects/utils/youtube_downloader.py "url"
    
    if permission is denied, then chmod +x /Users/simon/Documents/Projects/utils/youtube_downloader.py first  

    UPDATE:

    made shell script for easier acces, now, just write:

    zsh yt.sh "insert url"

    and it will download!
"""
# sys.argv allows for reading terminal arguments
from sys import argv

# youtube functionality in python
from pytube import YouTube

# timer wrapper
from timer import timer


# small conversion function to get length of video in appropriate format
def convert_time(sec: int) -> str:
    """converts seconds to hours, minutes, and seconds, returns formatted string of time."""

    # convert seconds in int to minutes and seconds
    minutes, seconds = divmod(sec, 60)

    # convert minutes in int to hours and minutes
    hours, minutes = divmod(minutes, 60)

    # if the video is one hour or longer:
    if hours >= 1:
        return f"Length: ({hours}:{minutes}:{seconds}) "

    if hours == 0:
        return f"Length: ({minutes}:{seconds}) "


@timer
def yt_downloader(url: str = None, directory: str = "/Users/simon/Downloads/"):
    """youtube downloader function"""

    # if-statement allows for both terminal and in-script function
    if url:
        # allows for entry of url in the function itself
        link = url
    else:
        # read second word in terminal entry
        link = argv[1]

    # create Youtube object from url
    yt = YouTube(link)

    # print video info to terminal
    print(f"\nTitle: {yt.title} by {yt.author}")

    print(convert_time(yt.length))

    print(f"Published: {yt.publish_date}")

    print(f"Views: {yt.views}")

    # create download object at highest available res
    yd = yt.streams.get_highest_resolution()

    # download the video to chosen directory, default is "/Users/simon/Downloads/"
    yd.download(directory)


# This function will be ran when the script is ran from here, or from terminal
def main():
    """main script"""

    # download T-pain tiny desk concert
    # yt_downloader("https://www.youtube.com/watch?v=CIjXUg1s5gc&ab_channel=NPRMusic")

    # run downloader function
    yt_downloader()


# run main function if this is the script being ran
if __name__ == "__main__":
    main()
