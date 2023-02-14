from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import ttkbootstrap as tb
import time


app = tb.Window(themename="simplex", title="Green House")
app.geometry("800x480")
app.iconbitmap("plant.ico")

def play_gif():
    img1=Image.open("light.gif")
    img2=Image.open("fan.gif")
    image1=Label(main_frame)
    image1.grid(row=1, column=1, padx=5, pady=5)
    image2=Label(main_frame)
    image2.grid(row=1, column=2, padx=5, pady=5)
    for img1,img2 in ImageSequence.Iterator(img1, img2):
        img1=img1.resize((150, 140))
        img2=img2.resize((150, 140))
        img2=ImageTk.PhotoImage(img2)
        image2.config(image=img2)
        img1=ImageTk.PhotoImage(img1)
        image1.config(image=img1)
        app.update()
        time.sleep(0.10)
    
    image1.after(0,play_gif)
 
# def play_gif1():
# 	global img1
# 	global image2
# 	img1=Image.open("light.gif")
# 	image2=Label(main_frame)
# 	image2.grid(row=1, column=1, padx=5, pady=5)
# 	for img1 in ImageSequence.Iterator(img1):
# 		img1=img1.resize((150, 140))
# 		img1=ImageTk.PhotoImage(img1)
# 		image2.config(image=img1)
# 		app.update()
# 		time.sleep(0.10)
# 	image2.after(0,play_gif1)

main_frame = Frame(app)
main_frame.pack(fill=BOTH, expand=True)
play_gif()

app.mainloop()
