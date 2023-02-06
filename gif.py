import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

def show_gif(root, file, width, height):
    im = Image.open(file)
    frames = []
    try:
        for i in count(1):
            frames.append(ImageTk.PhotoImage(im.copy().resize((width, height))))
            im.seek(i)
    except EOFError:
        pass
    frames = cycle(frames)
    try:
        delay = im.info['duration']
    except:
        delay = 100
    label = tk.Label(root, width=width, height=height)
    label.pack()
    update_frame(label, frames, delay)

def update_frame(label, frames, delay):
    if frames:
        label.config(image=next(frames))
        label.after(delay, update_frame, label, frames, delay)

root = tk.Tk()
show_gif(root, 'plant.gif', 40, 40)
root.mainloop()
