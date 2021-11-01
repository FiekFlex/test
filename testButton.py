import turtle
from tkinter import *


def hello():
    print("привет")


tk = Tk()
btn = Button(tk, text="Закрыть", command= hello)
btn.pack()
turtle.done()