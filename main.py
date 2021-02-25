import sys
import datetime
import serial
import multiprocessing
import time
from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from win32api import GetSystemMetrics

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

def choose_com_port():
    choosen_port = com_port_combo_box.get()
    print(choosen_port)

def set_color():
    pass

def set_random_color():
    pass

WORKING_SERIAL_PORT = None

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

window = Tk()
window.title("Python Arduino LED")
window.geometry("{}x{}+{}+{}".format(window_width, window_height, margin_left, margin_top))
window.minsize(width=window_min_width, height=window_min_height)
window.configure(bg=main_background_color)


n = tk.StringVar() 
com_port_combo_box = ttk.Combobox(window, width = 27,  
                            textvariable = n) 
  
com_port_combo_box['values'] = ('Please choose COM port',  
                          ) 

choose_com_port_button = Button(text ="Choose COM port", command = choose_com_port)

# get list of all COM ports
connected_serial_ports = serial_ports()

# add list of COM ports to combobox
for port in connected_serial_ports:
    available_port = str(port)
    com_port_combo_box['values'] = com_port_combo_box['values'] + (available_port,)

red_slider = Scale(window, from_=0, to=255, orient=HORIZONTAL, length=int(window_width/3), bg="#212121", troughcolor="red", fg="white", activebackground='#212121')
green_slider = Scale(window, from_=0, to=255, orient=HORIZONTAL, length=int(window_width/3), bg="#212121", troughcolor="green", fg="white", activebackground='#212121')
blue_slider = Scale(window, from_=0, to=255, orient=HORIZONTAL, length=int(window_width/3), bg="#212121", troughcolor="blue", fg="white", activebackground='#212121')
red_slider.config(highlightbackground="#212121")
green_slider.config(highlightbackground="#212121")
blue_slider.config(highlightbackground="#212121")

set_color_button = Button(text ="Set color", command = set_color())
set_random_color_button = Button(text ="Random color", command = set_random_color())

# Adding combobox drop down list 
com_port_combo_box.place(x=10, y=10)
choose_com_port_button.place(x=200,y=10)
red_slider.place(x=10, y=50)
green_slider.place(x=10, y=100)
blue_slider.place(x=10, y=150)
set_random_color_button.place(x=15, y=200)
set_color_button.place(x=255, y=200)

com_port_combo_box.current()  

info_label = Label(text = "Info messages", bg = label_info_background_color, fg=label_info_font_color, font=("Verdana", 14))
info_label.place(x = int(window_width/2), y = int(window_height - 75))


window.mainloop()

