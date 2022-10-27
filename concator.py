from moviepy.editor import VideoFileClip, concatenate_videoclips
# def mixClips(videoClips: list):
#     clip1 = VideoFileClip("myvideo.mp4")

#     final_clip = concatenate_videoclips([])
#     final_clip.write_videofile("my_concatenation.mp4")

final_clip = concatenate_videoclips(['./export_videos/1.mp4', './export_videos/2.mp4'])
final_clip.write_videofile("my_concatenation.mp4")