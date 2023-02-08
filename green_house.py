from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter as tk
from itertools import count, cycle
import customtkinter as ct

# Create the main window using the "simplex" theme and title it "Green House"
app = tb.Window(themename="simplex", title="Green House")
app.geometry("800x480")
app.iconbitmap("plant.ico")

def show_gif(app, file, width, height, grid_row, grid_column, padx, pady):
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
    label = tk.Label(main_frame, width=width, height=height)
    label.grid(row=grid_row, column=grid_column, padx=padx, pady=pady)
    update_frame(label, frames, delay)

def update_frame(label, frames, delay):
    if frames:
        label.config(image=next(frames))
        label.after(delay, update_frame, label, frames, delay)
        
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

# Create a main frame to contain the widgets and pack it into the main window
main_frame = Frame(app)
main_frame.pack(fill=BOTH, expand=True)

# Create a LabelFrame widget and give it a position within the main frame
label_frame = tb.LabelFrame(main_frame)
label_frame.grid(row=0, column=0, padx = 5, pady = 2, sticky="w")

# Create a Label widget and give it a "HOME" label, using a font size of 20 and bold style
home_label = tb.Label(label_frame,
                       bootstyle="warning",
                       text="HOME",
                       font=("Arial", 20, "bold")
                        )
home_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

#Importing the images
fanoff = ImageTk.PhotoImage(Image.open("fanoff.png").resize((40, 40)))
fanon = ImageTk.PhotoImage(Image.open("fanon.png").resize((40, 40)))
lightoff = ImageTk.PhotoImage(Image.open("lightsoff.png").resize((40, 40)))
lighton = ImageTk.PhotoImage(Image.open("lighton.png").resize((40, 40)))

# Variable to store the state of the checkbutton
var1 = IntVar()
var2 = IntVar()

# Create a Meter widget to display temperature and give it a position within the main frame
temp_meter = tb.Meter(main_frame,
                      amountused = 25,
                      bootstyle="danger",
                      interactive= True,
                      subtext="Temperature",
                      metersize= 155,
                      meterthickness= 10
                    )
temp_meter.grid(row=1, column=0, padx=10, pady=10)

# Create a Meter widget to display humidity and give it a position within the main frame
hum_meter = tb.Meter(main_frame,
                      amountused = 25,
                      bootstyle="info",
                      interactive= True,
                      subtext="Humidity",
                      metersize= 155,
                      meterthickness= 10
                    )
hum_meter.grid(row=1, column=1, padx=10, pady=10)

# Create a Meter widget to display light intensity and give it a position within the main frame
ldr_meter = tb.Meter(main_frame,
                      amountused = 25,
                      bootstyle="success",
                      interactive= True,
                      subtext="Light Intensity",
                      metersize= 155,
                      meterthickness= 10
                    )
ldr_meter.grid(row=1, column=2, padx=10, pady=10)

# Create a Meter widget to display soil temperature and give it a position within the main frame
soil_temperature_meter = tb.Meter(main_frame,
                      amountused = 25,
                      bootstyle="dark",
                      interactive= True,
                      subtext="Soil Temperature",
                      metersize= 155,
                      meterthickness= 10
                    )
soil_temperature_meter.grid(row=2, column=0, padx=10, pady=10)


# Create a Meter widget to display soil moisture and give it a position within the main frame
soil_moisture_meter = tb.Meter(main_frame,
                      amountused = 25,
                      bootstyle="warning",
                      interactive= True,
                      subtext="Soil Moisture",
                      metersize= 155,
                      meterthickness= 10
                    )
soil_moisture_meter.grid(row=2, column=1, padx=10, pady=10)


# Play a gif image
show_gif(main_frame, 'plant.gif', 150, 140, 1, 3, 10, 10)

# A button to turn on/off the watering system
watering_system_button = tb.Button(main_frame,
                                    text="Turn On/Off Watering System",
                                    bootstyle="warning"
                                    )
watering_system_button.grid(row=3, column=0,padx=10, pady=10, sticky="w")

# A checkbutton to turn on/off the fan
fan_checkbutton = tb.Checkbutton(main_frame,
                                    text="Turn On/Off Fan",
                                    bootstyle="primary-round-toggle",
                                    variable=var1,
                                    onvalue=1,
                                    offvalue=0,
                                    command=checkbox_event_1
                                    )
fan_checkbutton.grid(row=3, column=1, sticky="w")

# Fan on/off image label
fanoff_label = tb.Label(main_frame,
                        image=fanoff    
                        )
fanoff_label.grid(row=3, column=2, sticky="w")

# A checkbutton to turn on/off the light
light_checkbutton = tb.Checkbutton(main_frame,
                                    text="Turn On/Off Light",
                                    bootstyle="success-round-toggle",
                                    variable=var2,
                                    onvalue=1,
                                    offvalue=0,
                                    command=checkbox_event_2
                                    )
light_checkbutton.grid(row=3, column=3, sticky="w")


# Light on/off image label
lightoff_label = tb.Label(main_frame,
                        image=lightoff
                        )
lightoff_label.grid(row=3, column=4, sticky="w")

# # Fan status label
# fan_status_Label= ct.CTkLabel(master=main_frame,
#                                       text="OFF",
#                                       font=("Arial", 15, "bold"),
#                                       fg_color="red",
#                                       corner_radius=13,
#                                       text_color="white")
# fan_status_Label.grid(row=2, column=3, sticky="e")

# # Light status label
# light_status_Label= ct.CTkLabel(master=main_frame,
#                                         text="OFF",
#                                         font=("Arial", 15, "bold"),
#                                         fg_color="red",
#                                         corner_radius=13,
#                                         text_color="white")
# light_status_Label.grid(row=3, column=3, sticky="se")

# main loop
app.mainloop()
