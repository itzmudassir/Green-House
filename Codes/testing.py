from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import tkinter as tk
from itertools import count, cycle
import customtkinter
import serial
from tkVideoPlayer import TkinterVideo
import threading


app = tb.Window(themename="united", title="Green House")
app.geometry("800x480")
app.iconbitmap("Images\plant.ico")


ser = serial.Serial('COM3', 9600, timeout=1)
global modified
global values

def read():
    global values
    global modified
    global soil_moistureñ
    global temperature
    global Humidity
    global Light
    global Soil_Temperature
    
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
            temp_meter.set_value(temperature)
            
            
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
            temp_meter.configure(amountused=temperature)
            hum_meter.configure(amountused=Humidity)
            soil_temperature_meter.configure(amountused=Soil_Temperature)
            soil_moisture_meter.configure(amountused=soil_moisture)
            ldr_meter.configure(amountused=Light)
            
    label1.after(2000, read)


def checkbox_event_1():
    if(var1.get() == 0):
        # fan_status_Label.configure(text="Non Active")
        # fan_status_Label.configure(fg_color="red")
        fanoff_label.configure(image=fanoff)
        
    else:
        # fan_status_Label.configure(text="Activated")
        # fan_status_Label.configure(fg_color="green")
        fanoff_label.configure(image=fanon)

               
def checkbox_event_2():
    if(var2.get() == 0):
        # light_status_Label.configure(text="Non Active")
        # light_status_Label.configure(fg_color="red")
        lightoff_label.configure(image=lightoff)
        
    else:
        # light_status_Label.configure(text="Activated")
        # light_status_Label.configure(fg_color="green")
        lightoff_label.configure(image=lighton)
        
def home():
    global main_frame
    global label_frame
    global home_label
    global fanoff
    global fanon
    global lightoff
    global lighton
    global var1
    global var2
    global temp_meter
    global hum_meter
    global soil_temperature_meter
    global soil_moisture_meter
    global ldr_meter
    global fanoff_label
    global lightoff_label
    global fan_status_Label
    global light_status_Label
    global label1
    # Create a main frame to contain the widgets and pack it into the main window
    main_frame = Frame(app)
    main_frame.pack(fill=BOTH, expand=True)

    # Create a LabelFrame widget and give it a position within the main frame
    label_frame = tb.LabelFrame(main_frame)
    label_frame.grid(row=0, column=0, padx = 310, pady = 2, sticky="w", columnspan=4)

    # Create a Label widget and give it a "HOME" label, using a font size of 20 and bold style
    home_label = tb.Label(label_frame,
                        bootstyle="warning",
                        text="Green House",
                        font=("Arial", 20, "bold")
                            )
    home_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    #Importing the images
    fanoff = ImageTk.PhotoImage(Image.open("Images\\fanoff.png").resize((100, 100)))
    fanon = ImageTk.PhotoImage(Image.open("Images\\fanon.png").resize((100, 100)))
    lightoff = ImageTk.PhotoImage(Image.open("Images\lightsoff.png").resize((100, 100)))
    lighton = ImageTk.PhotoImage(Image.open("Images\lighton.png").resize((100, 110)))

    # Variable to store the state of the checkbutton
    var1 = IntVar()
    var2 = IntVar()

    # Create a Meter widget to display temperature and give it a position within the main frame
    temp_meter = tb.Meter(main_frame,
                        bootstyle="primary",
                        interactive= True,
                        subtext="Temperature",
                        subtextfont=("Times", 10, "bold"),
                        textright='°C',
                        metersize= 150,
                        metertype="semi",
                        meterthickness= 10
                        )
    temp_meter.grid(row=1, column=0, padx=10, columnspan=1, pady=10)

    # Create a Meter widget to display humidity and give it a position within the main frame
    hum_meter = tb.Meter(main_frame,
                        bootstyle="info",
                        interactive= True,
                        subtext="Humidity",
                        textright='%',
                        metersize= 155,
                        stripethickness=2,
                        meterthickness= 10
                        )
    hum_meter.grid(row=1, column=1, padx=10, pady=10)

    # Create a Meter widget to display light intensity and give it a position within the main frame
    ldr_meter = tb.Meter(main_frame,
                        bootstyle="success",
                        interactive= True,
                        subtext="Light Intensity",
                        textright='%',
                        metersize= 155,
                        stripethickness=10,
                        meterthickness= 10
                        )
    ldr_meter.grid(row=1, column=2, padx=30, pady=10)

    # Create a Meter widget to display soil temperature and give it a position within the main frame
    soil_temperature_meter = tb.Meter(main_frame,
                        bootstyle="dark",
                        interactive= True,
                        subtext="Soil Temperature",
                        textright='°C',
                        arcrange=180,
                        arcoffset=-180,
                        metersize= 155,
                        meterthickness= 10
                        )
    soil_temperature_meter.grid(row=2, column=0, padx=10, pady=10)


    # Create a Meter widget to display soil moisture and give it a position within the main frame
    soil_moisture_meter = tb.Meter(main_frame,
                        bootstyle="warning",
                        interactive= True,
                        subtext="Soil Moisture",
                        textright='%',
                        metersize= 155,
                        meterthickness= 10
                        )
    soil_moisture_meter.grid(row=2, column=1, padx=10, pady=10)

    # Fan on/off image label
    fanoff_label = tb.Label(main_frame,
                            image=fanoff    
                            )
    fanoff_label.grid(row=2, column=2, sticky="w", padx=30, pady=10)


    # Light on/off image label
    lightoff_label = tb.Label(main_frame,
                            image=lightoff
                            )
    lightoff_label.grid(row=2, column=3, sticky="w", padx=30, pady=10)
    
    # Plant Health Label
    plant_health_label = customtkinter.CTkLabel(master=main_frame,
                                 text="Plant Health: ",
                                    text_color="#7433FF",
                                    font=("Arial", 20, "bold"),
                                    width=150,
                                    height=30,
                                    corner_radius=8)

    plant_health_label.grid(row=3, column=0, padx=30, pady=10, sticky="w")
    
    # Plant Health Value Label
    plant_health_label_value = customtkinter.CTkLabel(master=main_frame,
                               text="Good",
                               text_color="white",
                               font=("Arial", 20, "bold"),
                               width=150,
                               height=30,
                               fg_color=("#36FF33"),
                               corner_radius=8)
    plant_health_label_value.grid(row=3, column=1, sticky="w")

    label1 = Label(main_frame, text=" ")
    label1.grid(row=4, column=0, padx=10, pady=10, sticky="w")


#Creating the Splash Screen
frame_video=Frame(app, width=800, height=480)
frame_video.pack(expand=True, fill="both")
videoplayer = TkinterVideo(frame_video, scaled=True)
videoplayer.load(r'Images\splash.mp4')
videoplayer.pack(expand=True, fill="both")
videoplayer.play()

app.after(2000,frame_video.destroy)    # Destroying the splash screen after 3 seconds
app.after(2000,home)


app.mainloop()