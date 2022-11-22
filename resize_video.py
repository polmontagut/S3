import os
import cv2


def get_height(resolution):  # depending on the user's choice, it will resize to the right resolution
    if "720p" in resolution:
        return 720
    if "480p" in resolution:
        return 480
    if "360x240" in resolution:
        return 240
    if "160x120" in resolution:
        return 120


def get_width(width, height, new_height):  # if our resulting width results to be odd, can causes problems with the
                                            # resize operation
    new_width = int(width * new_height / height)
    if new_height == 240:
        new_width = 360
        return new_width
    if new_height == 120:
        new_width = 160
        return new_width
    elif new_width % 2 == 0:
        return new_width
    else:
        new_width = int(width * new_height / height) + 1
        return new_width


def get_dimensions(video):  # we get the dimensions of the video we are working with
    vid = cv2.VideoCapture(video)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)  # gets the video width
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)  # gets the video height
    return width, height


def resize_video(input_video, height, width):  # resize the video and creates an mp4 in the BBB folder
    os.system("ffmpeg -i {input_video} -vf scale={width}:{height} videos/bbb_resize.mp4".format(
        input_video=input_video,
        height=height,
        width=width))


def create_resize(video, resolution):  # it creates the resized video using all the functions above
    width, height = get_dimensions(video)
    new_height = get_height(resolution)
    new_width = get_width(width, height, new_height)
    resize_video(video, new_height, new_width)


