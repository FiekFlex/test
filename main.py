from tkinter import *
import random
import time
from playsound import playsound
import winsound
import threading

def showscore(canvas, score):
    global scoretext
    if scoretext is not None:
        canvas.delete(scoretext)
    scoretext=canvas.create_text(20,20, text=score, fill="green", font=('Helvetica 20 bold'))

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                global score
                score += 1
                showscore(self.canvas, score)
#                winsound.Beep(660, 25)
                play()
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-a>', self.turn_left)
        self.canvas.bind_all('<KeyPress-d>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2


def restart():
    canvas.delete('all')
    global dead
    dead = False
    global paddle
    paddle = Paddle(canvas, 'blue')
    global ball
    ball = Ball(canvas, paddle, 'red')
    global score
    score = 0
    showscore(canvas, score)


def onKeyPress(event):
    if not dead:
        return
    if event.char == " ":
        restart()

def play():
    threading.Thread(target=playsound, args=('sound.mp3',), daemon=True).start()

scoretext=None
tk = Tk()
tk.title("Arkanoid")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
tk.bind('<KeyPress>', onKeyPress)
W = 500
H = 400
canvas = Canvas(tk, width=W, height=H, bd=0, highlightthickness=0, bg='cyan')
canvas.pack()
tk.update()
restart()


def gameover():
    canvas.create_text(W / 2, H / 2 - 30, text="Game over", fill="red", font=('Helvetica 35'))
    canvas.create_text(W / 2 + 5, H / 2 + 25, text="Press space button", fill="green", font=('Helvetica 20'))
    global dead
    dead = True


while 1:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    else:
        gameover()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.007)