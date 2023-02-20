from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import ttkbootstrap as tb

app = tb.Window(themename="simplex", title="Green House")
app.geometry("800x480")
app.iconbitmap("plant.ico")

def gif_play():
    global img, animating
    if animating:
        img = next(frames)
        img = img.resize((150, 140))
        img = ImageTk.PhotoImage(img)
        img_label.configure(image=img)
        img_label.image = img # needed to prevent garbage collection
        app.after(20, gif_play)

img = Image.open("plant.gif")
frames = ImageSequence.Iterator(img)
img = next(frames)

img_label = tb.Label(app)
img_label.grid(row=1, column=3)

img = img.resize((150, 140))
img = ImageTk.PhotoImage(img)
img_label.configure(image=img)

animating = True
gif_play()

app.mainloop()
