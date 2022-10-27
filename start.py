from video_scaper import linksOfTopVideos
from video_downloader import redditDownload
from video_combiner import mergeAudioAndVideo
import os

if __name__ == "__main__" :
    links = linksOfTopVideos('funnyvideos')
    for i in links:
        redditDownload(i)
    
    raw_video_folders = [x[0] for x in os.walk('./redvid_temp/')]

    for j in range(1, len(raw_video_folders)):
        mergeAudioAndVideo(f'{raw_video_folders[j]}/video.mp4', f'{raw_video_folders[j]}/audio.m4a', f"export_videos/{j}")
    

    pass