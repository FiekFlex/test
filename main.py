from tkinter import *
import random
import time

tk = Tk()
tk.title("Игра")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

import turtle
avery = turtle.Pen()
kate= turtle.Pen()
avery.forward(50)
avery.forward(90)
avery.forward(20)
kate.left(90)
kate.forward(100)

jacob= turtle.Pen()
jacob.left(180)
jacob.forward(80)
