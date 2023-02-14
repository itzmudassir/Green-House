from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import customtkinter as ct
import time


app = tb.Window(themename="simplex", title="Green House")
app.geometry("800x480")
app.iconbitmap("plant.ico")

def gif_play():
    img = Image.open("plant.gif")
    img_label = Label(app)
    img_label.pack()
    for img in ImageSequence.Iterator(img):
        img.resize((100, 100))
        img = ImageTk.PhotoImage(img)
        img_label.configure(image=img)
        app.update()
        time.sleep(0.01)
    img_label.after(0, gif_play)
    
gif_play()
    
app.mainloop()