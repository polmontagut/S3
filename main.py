import tkinter as tk
from tkinter import ttk, messagebox
import encode_video
import resize_video
import deletes


def create_video():
    resolution = resolutions.get()
    encoder = encoders.get()
    video = "bbb.mp4"
    if resolution != "" and encoder != "":
        deletes.delete_files()
        resize_video.create_resize(video, resolution)
        new_video = "videos/bbb_resize.mp4"
        encode_video.create_encode(new_video, encoder)
        deletes.delete_mp4()
    if resolution == "" and encoder == "":
        tk.messagebox.showinfo(title="Error", message="Please, select at least one value!")
        return
    if resolution == "":
        deletes.delete_files()
        encode_video.create_encode(video, encoder)
    if encoder == "":
        deletes.delete_files()
        resize_video.create_resize(video, resolution)
    tk.messagebox.showinfo(title="VideoCreated", message="Video created in the videos folder!")


window = tk.Tk()
window.config(width=300, height=200)
window.title("Video converter")

# resolution
res = tk.Label(window, text="Insert resolution (720p default) :")
res.place(x=50, y=30)

resolutions = ttk.Combobox(
    state="readonly",
    values=["", "720p", "480p", "360x240", "160x120"],

)
resolutions.place(x=50, y=60)

# encoders
enc = tk.Label(window, text="Insert encoder:")
enc.place(x=50, y=90)

encoders = ttk.Combobox(
    state="readonly",
    values=["", "VP8", "VP9", "h265", "AV1"]
)
encoders.place(x=50, y=120)

# accept button
okey = ttk.Button(text="Okey", command=create_video)
okey.place(x=50, y=150)

window.mainloop()

#width, height = resize_video.get_dimensions(video)
#resize_video.options_resize(video, width, height)  # opens the resize menu
#encode_video.convert_video_h265(video)
