from redvid import Downloader
from cprint import *

def redditDownload(videoLink: str):
    reddit = Downloader()
    reddit.min = True
    reddit.url = f'https://www.reddit.com/{videoLink}'
    try:
        cprint.info('Downloading...')
        reddit.path = './export_videos'
        reddit.download()
    except:
        pass
    cprint.ok('Download Completed..!')

if __name__ == "__main__" :
    redditDownload('r/Unexpected/comments/yecitb/happy_birthday/')