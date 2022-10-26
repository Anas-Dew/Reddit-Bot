from redvid import Downloader

def redditDownload(link: str):
    reddit = Downloader()
    reddit.max = True
    reddit.url = f'https://www.reddit.com/{link}'
    reddit.download()

if __name__ == "__main__" :
    redditDownload('r/LeakedReality/comments/v88hxm/we_still_need_funny_videos_too_right/')