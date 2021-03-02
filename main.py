import sys
import datetime
import serial
import multiprocessing
import time
from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from win32api import GetSystemMetrics
import random

WORKING_SERIAL_PORT = None
baud_rate = 9600

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def open_serial_connection():
    try:
        ser = serial.Serial(WORKING_SERIAL_PORT, baud_rate)
    except:
        info_label = Label(text = "Please choose COM port", bg = label_info_background_color, fg=red, font=("Verdana", 14))

def choose_com_port():
    choosen_port = com_port_combo_box.get()
    global WORKING_SERIAL_PORT
    WORKING_SERIAL_PORT = choosen_port
    print("Choosen port: ", choosen_port)

def set_basic_color():
    color_name = color_button["text"]
    print("Choosen basic color ", color_name)

def set_custom_color():
    custom_color = ""
    red_value = int(red_var.get())
    green_value = int(green_var.get())
    blue_value = int(blue_var.get())
    custom_color = '#{:02x}{:02x}{:02x}'.format( red_value, green_value , blue_value )
    print("Custom color: ", custom_color)

def set_effect():
    effect_name = effect_button["text"]
    print("Choosen effect is ", effect_name)

def set_random_color():
    #time.sleep(0.1)
    random_color = "#%06x" % random.randint(0, 0xFFFFFF)
    info_label = Label(text = "This color was choosen", bg = label_info_background_color, fg=random_color, font=("Verdana", 14))
    info_label.place(x = int(window_width/2), y = int(window_height - 75))
    print("Random color is ", random_color)

def set_brightness():
    led_brightness = 0
    brightness_value = int(brightness_var.get())
    print("Brightness", brightness_value)


screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

window_width = 900
window_height = 600
window_min_width = window_width
window_min_height = window_height

margin_left = int(screen_width / 2 - window_min_width / 2)
margin_top = int(screen_height / 2 - window_min_height / 2)

main_background_color = "#212121"

label_info_background_color = "#212121"
label_info_font_color = "white"

colors_list = ["white", "blue", "red", "yellow", "purple", "light blue", "green", "aqua", "violet", "orange", "pink", "fuchsia", "lime", "cyan", "off"]
effects_list = ["fire immitation", "fading lights", "running lights", "rain effect", "equalizer mode"]

color_button_x_margin = 400
color_button_y_margin = 70

effect_button_x_margin = 30
effect_button_y_margin = 350

button_font = ("Verdana", 10)

window = Tk()
window.title("Python Arduino LED v1.0.0")
window.geometry("{}x{}+{}+{}".format(window_width, window_height, margin_left, margin_top))
window.minsize(width=window_min_width, height=window_min_height)
window.configure(bg=main_background_color)
# add resizable in future
window.resizable(0, 0)

n = tk.StringVar() 
com_port_combo_box = ttk.Combobox(window, width = 27,  
                            textvariable = n) 
  
com_port_combo_box['values'] = ('Please choose COM port',  
                          ) 

choose_com_port_button = Button(text ="Choose COM port", command = choose_com_port, font=button_font)

# get list of all COM ports
connected_serial_ports = serial_ports()

# add list of COM ports to combobox
for port in connected_serial_ports:
    available_port = str(port)
    com_port_combo_box['values'] = com_port_combo_box['values'] + (available_port,)


red_var = DoubleVar()
green_var = DoubleVar()
blue_var = DoubleVar()
brightness_var = DoubleVar()

red_slider = Scale(window, variable=red_var, from_=0, to=255, orient=HORIZONTAL, length=int(window_width/3), bg="#212121", troughcolor="red", fg="white", activebackground='#212121')
green_slider = Scale(window, variable=green_var, from_=0, to=255, orient=HORIZONTAL, length=int(window_width/3), bg="#212121", troughcolor="green", fg="white", activebackground='#212121')
blue_slider = Scale(window, variable=blue_var, from_=0, to=255, orient=HORIZONTAL, length=int(window_width/3), bg="#212121", troughcolor="blue", fg="white", activebackground='#212121')
brightness_slider = Scale(window, variable=brightness_var, from_=0, to=255, orient=HORIZONTAL, length=int(window_width/3), bg="#212121", troughcolor="white", fg="white", activebackground='#212121')
red_slider.config(highlightbackground="#212121")
green_slider.config(highlightbackground="#212121")
blue_slider.config(highlightbackground="#212121")
brightness_slider.config(highlightbackground="#212121")


set_color_button = Button(text ="Set color", command = set_custom_color, font=button_font)
set_random_color_button = Button(text ="Random color", command = set_random_color, font=button_font)
set_brightness_button = Button(text ="Set brightness", command = set_brightness, font=button_font)

# Adding combobox drop down list 
com_port_combo_box.place(x=10, y=10)
choose_com_port_button.place(x=200,y=10)
red_slider.place(x=10, y=50)
green_slider.place(x=10, y=100)
blue_slider.place(x=10, y=150)
brightness_slider.place(x=10, y=235)

set_random_color_button.place(x=15, y=200)
set_color_button.place(x=255, y=200)
set_brightness_button.place(x=220, y=285)

com_port_combo_box.current()  


for color in colors_list:
    color_button = Button(text =color, command = set_color, font=button_font, command=set_basic_color) 
    if color_button_x_margin >= 800:
        color_button.place(x=color_button_x_margin, y=color_button_y_margin)
        color_button_y_margin += 50
        color_button_x_margin = 400
    else:
        color_button.place(x=color_button_x_margin, y=color_button_y_margin)
        color_button_x_margin += 100

effects_label = Label(text = "Effects", bg = label_info_background_color, fg=label_info_font_color, font=("Verdana", 14))
effects_label.place(x = int(window_width/2 - 50), y = 300)

for effect in effects_list:
    effect_button = Button(text =effect, command = set_effect, font=button_font, command=set_effect) 
    if effect_button_x_margin >= 800:
        effect_button.place(x=effect_button_x_margin, y=effect_button_y_margin)
        effect_button_y_margin += 50
        effect_button_x_margin = 30
    else:
        effect_button.place(x=effect_button_x_margin, y=effect_button_y_margin)
        effect_button_x_margin += 120

info_label = Label(text = "Info messages", bg = label_info_background_color, fg=label_info_font_color, font=("Verdana", 14))
info_label.place(x = int(window_width/2), y = int(window_height - 75))


window.mainloop()

