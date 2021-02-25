from tkinter import *
from win32api import GetSystemMetrics

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



info_label = Label(text = "This is a Label", bg = label_info_background_color, fg=label_info_font_color, width=window_width, font=("Verdana", 14)).pack(side=BOTTOM)



window.mainloop()