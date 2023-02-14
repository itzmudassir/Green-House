from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

app = tb.Window(themename="simplex", title="Green House")
app.geometry("800x480")
app.iconbitmap("plant.ico")

def camera_view():
    top = Toplevel()
    top = tb.Window(themename="simplex", title="Camera View")
    top.geometry("800x480")
    top.title("Camera View")
    top.iconbitmap("plant.ico")
    top.resizable(False, False)
    top.attributes('-topmost', True)
    


button1 = tb.Button(app, text="Camera View", command=camera_view)
button1.grid(row=0, column=0, padx=10, pady=10)



app.mainloop()