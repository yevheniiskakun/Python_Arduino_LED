from tkinter import *

window = Tk()

window.title("Python Arduino LED")

window.geometry("900x600")

window.configure(bg = "orange")

Label(text = "This is a Label", bg = "black", fg = "white").pack()

Button(text = "Click me", bg = "white", fg = "black").pack()


window.mainloop()