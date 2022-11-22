import os


def convert_video_vp8(video):
    os.system("ffmpeg -i {video} -c:v libvpx -b:v 128k -c:a libvorbis videos/bbb_coded_vp8.webm".format(video=video))


def convert_video_vp9(video):
    os.system("ffmpeg -i {video} -c:v libvpx-vp9 -b:v 128k videos/bbb_coded_vp9.webm".format(video=video))


def convert_video_h265(video):
    os.system("ffmpeg -i {video} -c:v libx265 -b:v 128k -c:a aac videos/bbb_coded_h265.mov".format(video=video))


def convert_video_av1(video):
    os.system("ffmpeg -i {video} -c:v libsvtav1 -b:v 128k videos/bbb_coded_av1.mkv".format(video=video))


def create_encode(video, encoder):
    if "VP8" in encoder:
        convert_video_vp8(video)
    if "VP9" in encoder:
        convert_video_vp9(video)
    if "h265" in encoder:
        convert_video_h265(video)
    if "AV1" in encoder:
        convert_video_av1(video)
