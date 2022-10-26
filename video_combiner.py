from moviepy.editor import *

def mergeAudioAndVideo(videoPath: str, audioPath: str, outputName: str):
    videoclip = VideoFileClip(f"{videoPath}")
    audioclip = AudioFileClip(f"{audioPath}")

    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(f"{outputName}.mp4")