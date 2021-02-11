import tkinter as tk
from tkinter import ttk
import tkinter.font
import pyglet

from threading import Thread


win = tk.Tk()
win.title("Python Gui Test")
win.resizable(False, False)
win.geometry("320x240")
#win.attributes("-fullscreen", True)

font = tkinter.font.Font(family='NanumBarunGothic Regular', size=30)
label1 = ttk.Label(win, text="", font=font)
label1.grid(column=0, row=0)
global das
das = ""

def key_input(value):
    global das
    if not repr(value.char) == "''":
        numbers = '1234567890'
        operators = '/*+-='
        if value.char in numbers :
            print(value.char)
            das = das + str(value.char)
        elif value.char in operators :
            print(das)
        elif value.keysym == "Return":
            das = das +","
            READ()
            soundplay()
            print("equal button pressed")
        # elif value.keysym == "Enter":
        #     print('AC button pressed')

        return das


win.bind('<Key>', key_input) 

def real_playsound():
    song = pyglet.media.load('bell.wav')
    song.play()
    pyglet.app.run()

def soundplay():
    global play_thread
    play_thread = Thread(target=real_playsound)
    play_thread.start()

def READ():
    label1.configure(text=das)


win.focus_set()
win.mainloop()
