import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

def show_gif(root, file, width, height, grid_row, grid_column, padx, pady):
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
    label.grid(row=grid_row, column=grid_column, padx=padx, pady=pady)
    update_frame(label, frames, delay)

def update_frame(label, frames, delay):
    if frames:
        label.config(image=next(frames))
        label.after(delay, update_frame, label, frames, delay)

root = tk.Tk()
show_gif(root, 'fan.gif', 40, 40, 0, 0, 5, 5)
root.mainloop()
