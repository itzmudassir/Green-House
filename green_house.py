from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter as tk
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
    label = tk.Label(main_frame, width=width, height=height)
    label.grid(row=1, column=3, padx=10, pady=10)
    update_frame(label, frames, delay)

def update_frame(label, frames, delay):
    if frames:
        label.config(image=next(frames))
        label.after(delay, update_frame, label, frames, delay)

# Create the main window using the "simplex" theme and title it "Green House"
app = tb.Window(themename="simplex", title="Green House")
app.geometry("800x600")

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

# Create a Meter widget to display Fan and give it a position within the main frame
fan_meter = tb.Meter(main_frame,
                      amountused = 25,
                      bootstyle="primary",
                      interactive= True,
                      subtext="Fan Speed",
                      metersize= 155,
                      meterthickness= 10
                    )
fan_meter.grid(row=2, column=1, padx=10, pady=10)

# Create a Meter widget to display UV Light and give it a position within the main frame
light_meter = tb.Meter(main_frame,
                        amountused = 25,
                        bootstyle="secondary",
                        interactive= True,
                        subtext="UV Light",
                        metersize= 155,
                        meterthickness= 10
                    )
light_meter.grid(row=2, column=2, padx=10, pady=10)

# Create a Meter widget to display soil moisture and give it a position within the main frame
soil_moisture_meter = tb.Meter(main_frame,
                      amountused = 25,
                      bootstyle="warning",
                      interactive= True,
                      subtext="Soil Moisture",
                      metersize= 155,
                      meterthickness= 10
                    )
soil_moisture_meter.grid(row=2, column=3, padx=10, pady=10)

show_gif(app, 'plant.gif', 150, 140)


watering_system_button = tb.Button(main_frame,
text="Turn On/Off Watering System",
bootstyle="warning"
)
watering_system_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

app.mainloop()
