from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import tkinter as tk
import pygame 
from tkinter.font import BOLD
import customtkinter
import serial
from tkVideoPlayer import TkinterVideo
import datetime

app = ttk.Window(themename="simplex", title="Green House")
app.geometry("800x480")
app.iconbitmap("Images\plant.ico")

ser = serial.Serial('COM3', 9600, timeout=1)
global modified
global values
global now

def read():
    global values
    global modified
    global now
    global soil_moisture
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
            tem.configure(amountused=temperature)
            hum.configure(amountused=Humidity)
            soil.configure(amountused=Soil_Temperature)
            mos.configure(amountused=soil_moisture)
            light.configure(amountused=Light)
            # temp_meter.set_value(temperature)
            soil_moisture=int(soil_moisture)
            temperature=int(temperature)
            
            now = datetime.datetime.now()
            f = open("Values.txt", "a")
            f.write("Temperature is : " + temperature + " Humidity is : " + Humidity + " Soil Temperature is : " + Soil_Temperature + " Soil Moisture is : " + soil_moisture + " Light Intensity is : " + Light + " \n" + now.strftime("%Y-%m-%d %H:%M:%S"))
            f.close()
            
            if temperature > 18 and temperature < 25:
                print("OK")
                plant_health_label_value.configure(text="Good Condition")
                plant_health_label_value.configure(fg_color="green")
            
        
            elif temperature < 18:
                print("Light is on")
                fan_label.configure(image=light_on)
                plant_health_label_value.configure(text="Maintain Temperature")
                plant_health_label_value.configure(fg_color="red")
            elif temperature >26:
                print("Fan is On")
                fan_label.configure(image=fan_on)
                plant_health_label_value.configure(text="Maintain Temperature")
                plant_health_label_value.configure(fg_color="red")
                
            elif soil_moisture < 50:
                print("Water is on")
                pump_label.configure(image=pump_on)
                plant_health_label_value.configure(text="Maintain Soil Moisture")
                plant_health_label_value.configure(fg_color="red")
            
            elif soil_moisture > 50:
                print("Water is off")
                pump_label.configure(image=pump_off)
                plant_health_label_value.configure(text="Good Condition")
                plant_health_label_value.configure(fg_color="green")
                
            
            
            
            
            
            
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
            tem.configure(amountused=temperature)
            hum.configure(amountused=Humidity)
            soil.configure(amountused=Soil_Temperature)
            mos.configure(amountused=soil_moisture)
            light.configure(amountused=Light)
            soil_moisture=int(soil_moisture)
            temperature=float(temperature)
            now = datetime.datetime.now()
            f = open("Values.txt", "a")
            f.write("Temperature is : " + str(temperature) + " Humidity is : " + str(Humidity) + " Soil Temperature is : " + str(Soil_Temperature) + " Soil Moisture is : " + str(soil_moisture) + " Light Intensity is : " + str(Light) + " \n" + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            f.close()
            if temperature > 18 and temperature < 25:
                print("OK")
                plant_health_label_value.configure(text="Good Condition")
                plant_health_label_value.configure(fg_color="green")
            
        
            elif temperature < 18:
                print("Light is on")
                fan_label.configure(image=light_on)
                plant_health_label_value.configure(text="Maintain Temperature")
                plant_health_label_value.configure(fg_color="red")
            elif temperature >26:
                print("Fan is On")
                fan_label.configure(image=fan_on)
                plant_health_label_value.configure(text="Maintain Temperature")
                plant_health_label_value.configure(fg_color="red")
            
            elif soil_moisture < 50:
                print("Water is on")
                pump_label.configure(image=pump_on)
                plant_health_label_value.configure(text="Maintain Soil Moisture")
                plant_health_label_value.configure(fg_color="red")
            
            elif soil_moisture > 50:
                print("Water is off")
                pump_label.configure(image=pump_off)
                plant_health_label_value.configure(text="Good Condition")
                plant_health_label_value.configure(fg_color="green")
            
    light.after(1000,read)
            
    
def home():
    global tem
    global hum
    global light
    global mos
    global soil
    global plant_health_label
    global plant_health_label_value
    title_frame=ttk.LabelFrame(main_frame)
    title_frame.grid(column=0,row=0,columnspan=4)
    title_label = ttk.Label(title_frame, text="Green House",bootstyle=WARNING,font=("kanit",18,BOLD ))
    title_label.grid(column=0,row=0,padx=5,columnspan=4)
    tem = ttk.Meter(
        main_frame,
        metersize=150,
        padding=5,
        
        metertype="full",
        subtext="Temperture",
        interactive=False,
        bootstyle="primary",
        textright=(chr(176),"C")
    )
    tem.grid(column=0,row=1,padx=20,pady=5)
    hum = ttk.Meter(
        main_frame,
        metersize=150,
        padding=5,
        
        metertype="full",
        subtext="Humidity",
        interactive=False,
        bootstyle="secondary",
        textright=("%"),
        stripethickness=5
    )
    hum.grid(column=1,row=1,padx=5,pady=5)
    light = ttk.Meter(
        main_frame,
        metersize=150,
        padding=5,
        
        metertype="full",
        subtext="Light Intensity ",
        interactive=False,
        bootstyle="success",
        textright=("%"),
        stripethickness=10
    )
    light.grid(column=2,row=1,padx=5,pady=5)
    mos = ttk.Meter(
        main_frame,
        metersize=150,
        padding=5,
        
        metertype="full",
        subtext="Soil Moisture",
        interactive=False,
        bootstyle="info",
        textright=("%"),
        stripethickness=15
    )
    mos.grid(column=0,row=2,padx=5,pady=10)
    soil = ttk.Meter(
        main_frame,
        metersize=150,
        padding=5,
        
        metertype="full",
        subtext="Soil Temperture",
        interactive=False,
        bootstyle="warning",
        textright=(chr(176),"C"),
        stripethickness=20
    )

    soil.grid(column=1,row=2,padx=5,pady=10)

    picture_frame=ttk.Frame(main_frame)
    picture_frame.grid(row=1,column=3,rowspan=2)
    global fan_label
    global fan_off
    global fan_on

    fan_on=Image.open("Images\\fanon.png")
    fan_on=fan_on.resize((100,100), resample=Image.Resampling.LANCZOS)
    fan_on=ImageTk.PhotoImage(fan_on)
    
    fan_off=Image.open("Images\\fanoff.png")
    fan_off=fan_off.resize((100,100), resample=Image.Resampling.LANCZOS)
    fan_off=ImageTk.PhotoImage(fan_off)
    fan_label=ttk.Label(picture_frame,image=fan_off)
    fan_label.image=fan_off
    fan_label.grid(row=0,column=0,pady=10,padx=15)
    
    global light_label
    global light_off
    global light_on
    light_on=Image.open("Images\lighton.png")
    light_on=light_on.resize((100,100), resample=Image.Resampling.LANCZOS)
    light_on=ImageTk.PhotoImage(light_on)

    light_off=Image.open("Images\\lightsoff.png")
    light_off=light_off.resize((100,100), resample=Image.Resampling.LANCZOS)
    light_off=ImageTk.PhotoImage(light_off)
    light_label=ttk.Label(picture_frame,image=light_off)
    light_label.image=light_off
    light_label.grid(row=1,column=0,pady=10,padx=15)
    global pump_label
    global pump_off
    global pump_on
    pump_on=Image.open("Images\pumpon.png")
    pump_on=pump_on.resize((100,100), resample=Image.Resampling.LANCZOS)
    pump_on=ImageTk.PhotoImage(pump_on)
    
    
    pump_off=Image.open("Images\pumpoff.png")
    pump_off=pump_off.resize((100,100), resample=Image.Resampling.LANCZOS)
    pump_off=ImageTk.PhotoImage(pump_off)
    pump_label=ttk.Label(picture_frame,image=pump_off)
    pump_label.image=pump_off
    pump_label.grid(row=2,column=0,pady=10,padx=15)
    
    
    
    health_frame=ttk.Frame(main_frame)
    health_frame.grid(column=2,row=2,rowspan=2)
    plant_health_label = customtkinter.CTkLabel(master=health_frame,
                                 text="PLANT HEALTH",
                                    text_color="#cc9900",
                                    font=("Arial", 22, "bold", "underline"),
                                    width=150,
                                    height=30,
                                    corner_radius=8)

    plant_health_label.grid(row=0, column=0)
    
    # Plant Health Value Label
    plant_health_label_value = customtkinter.CTkLabel(master=health_frame,
                               text="GOOD",
                               text_color="white",
                               font=("Arial", 20, "bold"),
                               width=150,
                               height=30,
                               fg_color=("#36FF33"),
                               corner_radius=8)
    plant_health_label_value.grid(row=1, column=0,pady=10)

    

main_frame=ttk.Frame(app)
main_frame.pack(fill=BOTH,expand=True)

frame_video=Frame(main_frame, width=800, height=480)
frame_video.pack(expand=True, fill="both")
videoplayer = TkinterVideo(frame_video, scaled=True)
videoplayer.load(r'Images\splash.mp4')
videoplayer.pack(expand=True, fill="both")
videoplayer.play()

app.after(2000,frame_video.destroy)    # Destroying the splash screen after 3 seconds
app.after(2000,home)
app.after(2000,read)

app.mainloop()