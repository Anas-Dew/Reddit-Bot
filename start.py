from video_scaper import linksOfTopVideos
from video_downloader import redditDownload

if __name__ == "__main__" :
    links = linksOfTopVideos('Unexpected')
    for i in links:
        redditDownload(i)
    pass