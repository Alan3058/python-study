import os

from moviepy.editor import *


def join(dirName=None, tofileName=None):
    L = []
    files = os.listdir(dirName)
    files.sort()
    for fileName in files:
        filePath = os.path.join(dirName, fileName)
        video = VideoFileClip(filePath)
        L.append(video)
    final_clip = concatenate_videoclips(L)
    final_clip.to_videofile(tofileName)


if __name__ == '__main__':
    join("E:/other/b1421jg33xz/b1421jg33xz.hd", "E:/other/b1421jg33xz/test.mp4")
