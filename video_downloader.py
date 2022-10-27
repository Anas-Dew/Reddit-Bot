from redvid import Downloader

def redditDownload(link: str):
    reddit = Downloader()
    reddit.min = True
    reddit.url = f'https://www.reddit.com/{link}'
    try:
        reddit.download()
    except:
        pass

if __name__ == "__main__" :
    redditDownload('r/funnyvideos/comments/ydrc4r/where_are_you_from/')