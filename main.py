from moviepy.editor import *
import os
import random

def main():
    # Background
    bg_file = os.listdir("background_clips")[random.randrange(0, len(os.listdir("background_clips")))]
    background = VideoFileClip(bg_file)
    # print(bg_file)

    content = VideoFileClip("./family_guy_clips/swedish_bakery.mp4").subclip(0, 10)
    print(content)
    combined = clips_array([[content], [background]])
    combined.write_videofile("test.mp4")

    # backgroundClip = ColorClip((720, 1280), (0, 0, 255), duration=2)
    # videoClip = backgroundClip
    # videoClip = CompositeVideoClip([videoClip])
    # videoClip.write_videofile("test.mp4", fps=30)


if __name__ == '__main__':
    main()
