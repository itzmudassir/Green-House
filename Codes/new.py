import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk, ImageSequence
import threading
import customtkinter
import serial
from tkVideoPlayer import TkinterVideo
from tkinter import *

root = tk.Tk()
root.geometry("800x480")
root.title("Green House")
root.iconbitmap("Images\plant.ico")
style = ttk.Style("simplex")

ser = serial.Serial('COM3', 9600, timeout=1)
global modified
global values


def read():
    global values
    global modified
    global soil_moisture
    global temperature
    global Humidity
    global Light
    global Soil_Temperature
    global label1
    global b1
    global b2
    global b3
    global b4
    global b5
    
    try:
        line = ser.readline().decode()   # read a byte
        sensor=line.split(",")
        modified = []
        values = []
        for line in sensor:
            modified.append(line.strip())
        if len(modified) == 5:
            values.append(modified)
            soil_moisture = values[0][0]
            temperature = values[0][1]
            Humidity = values[0][2]
            Light = values[0][3]
            Soil_Temperature = values[0][4]
            b1.configure(amountused=temperature)
            b2.configure(amountused=Humidity)
            b4.configure(amountused=Soil_Temperature)
            b5.configure(amountused=soil_moisture)
            b3.configure(amountused=Light)
            
            
            
    except Exception as e:
        line = ser.readline().decode()   # read a byte
        sensor=line.split(",")
        modified = []
        values = []
        for line in sensor:
            modified.append(line.strip())
        if len(modified) == 5:
            values.append(modified)
            soil_moisture = values[0][0]
            temperature = values[0][1]
            Humidity = values[0][2]
            Light = values[0][3]
            Soil_Temperature = values[0][4]
            b1.configure(amountused=temperature)
            b2.configure(amountused=Humidity)
            b4.configure(amountused=Soil_Temperature)
            b5.configure(amountused=soil_moisture)
            b3.configure(amountused=Light)
            
    label1.after(1000, read)

def home():
    global lightoff
    global fanoff
    global tapoff
    global b1
    global b2
    global b3
    global b4
    global b5
    global label1
    # label
    main_frame=ttk.Frame(root)
    main_frame.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)

    Label_frame=ttk.LabelFrame(main_frame)
    Label_frame.grid(row=0,column=0, columnspan=4)
    title_label=ttk.Label(Label_frame,text="GREEN HOUSE",font=("Helvetica",20),bootstyle="DANGER")
    title_label.grid(row=0,column=0)

    health_frame=ttk.Frame(main_frame)
    health_frame.grid(row=2,column=2,rowspan=2)
    plant_health_label=ttk.Label(health_frame,text="PLANT HEALTH",font=("Helvetica",20),bootstyle="WARNING")
    plant_health_label.grid(row=0,column=0)

    health_Status_label=ttk.Label(health_frame,text="GOOD",font=("Helvetica",20),bootstyle="WARNING")
    health_Status_label.grid(row=1,column=0)


    pictures_frame=ttk.Frame(main_frame)
    pictures_frame.grid(row=1,column=3,rowspan=2)

    # fan_image
    fanoff = ImageTk.PhotoImage(Image.open("Images/fanoff.png").resize((60, 60)))
    fan_off_label=ttk.Label(pictures_frame, image=fanoff)
    fan_off_label.grid(row=0,column=0, padx=20, pady=10)

    # light_image
    lightoff = ImageTk.PhotoImage(Image.open("Images\lightsoff.png").resize((60, 60)))
    light_off_label=ttk.Label(pictures_frame, image=lightoff)
    light_off_label.grid(row=1,column=0, padx=20, pady=10)

    # tap_image

    tapoff = ImageTk.PhotoImage(Image.open("Images\\tapoff.png").resize((60, 60)))
    tap_off_label=ttk.Label(pictures_frame, image=tapoff)
    tap_off_label.grid(row=2,column=0, padx=20, pady=10)


    # meters

    b1 = ttk.Meter(
        main_frame,
        metersize=180,
        padding=8,
        amountused=25,
        metertype="full",
        subtext="Temperature",
        textright="c",
        textfont=['Times',26,'bold'],
        bootstyle='WARNING',
        interactive=True,
        stripethickness=8
    )
    b1.grid(row=1, column=0, padx=10, pady=10)

    b2 = ttk.Meter(
        main_frame,
        metersize=180,
        padding=8,
        amountused=25,
        metertype="full",
        textright="%",
        textfont=['Times',26,'bold'],
        subtext="Humidity",
        bootstyle='DANGER',
        interactive=True,
        stripethickness=8
    )
    b2.grid(row=1, column=1, padx=10, pady=10)

    b3 = ttk.Meter(
        main_frame,
        metersize=180,
        padding=8,
        amountused=25,
        textfont=['Times',26,'bold'],
        metertype="full",
        textright="%",
        subtext="Light Intensity",
        bootstyle='PRIMARY',
        interactive=True,
        stripethickness=8
    )
    b3.grid(row=1, column=2, padx=10, pady=10,)

    b4 = ttk.Meter(
        main_frame,
        metersize=180,
        padding=8,
        amountused=25,
        metertype="full",
        textfont=['Times',26,'bold'],
        textright="%",
        subtext="Soil Temperature",
        bootstyle='INFO',
        interactive=True,
        stripethickness=8
    )
    b4.grid(row=2, column=0, padx=10, pady=10)
    b5 = ttk.Meter(
        main_frame,
        metersize=180,
        padding=8,
        amountused=25,
        textfont=['Times',26,'bold'],
        metertype="full",
        subtext="Soil Moisture",
        textright="%",
        bootstyle='success',
        interactive=True,
        stripethickness=8
    )
    b5.grid(row=2, column=1, padx=10, pady=10)
    
    label1 = ttk.Label(main_frame, text=" ")
    label1.grid(row=4, column=0)

#Creating the Splash Screen
frame_video=Frame(root, width=800, height=480)
frame_video.pack(expand=True, fill="both")
videoplayer = TkinterVideo(frame_video, scaled=True)
videoplayer.load(r'Images\splash.mp4')
videoplayer.pack(expand=True, fill="both")
videoplayer.play()

root.after(2000,frame_video.destroy)    # Destroying the splash screen after 3 seconds
root.after(2000,home)

root.after(2000, read)    # Calling the read function after 3 seconds
root.mainloop()