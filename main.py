import sys
import glob
import serial
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
com_port_choosen = ttk.Combobox(window, width = 27,  
                            textvariable = n) 
  
com_port_choosen['values'] = ('Please choose COM port',  
                          ) 

connected_serial_ports = serial_ports()

for port in connected_serial_ports:
    available_port = str(port)
    com_port_choosen['values'] = com_port_choosen['values'] + (available_port,)

# Adding combobox drop down list 

com_port_choosen.place(x = 10, y = 10)
  
# Shows february as a default value 
com_port_choosen.current()  

info_label = Label(text = "Here", bg = label_info_background_color, fg=label_info_font_color, font=("Verdana", 14))
info_label.place(x = 100, y = 100)




window.mainloop()