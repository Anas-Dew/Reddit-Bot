from moviepy.editor import *
from cprint import *

def mergeAudioAndVideo(videoPath: str, audioPath: str, outputName: str):

    videoclip = VideoFileClip(f"{videoPath}")
    audioclip = AudioFileClip(f"{audioPath}")
    cprint.info('Merging videos...')
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(f"{outputName}.mp4")
    cprint.ok('Completed..!')