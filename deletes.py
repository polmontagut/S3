import os
import glob


def delete_files():  # deletes all files in a folder
    path = glob.glob('videos/*')
    for filename in path:
        os.remove(filename)


def delete_mp4():
    path = glob.glob('videos/*')
    for filename in path:
        if filename.endswith(".mp4"):
            os.remove(filename)
