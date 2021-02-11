import tkinter
import tkinter.font
import pyglet
from threading import Thread




root = tkinter.Tk()
root.title("Python Gui Test")
#root.resizable(False, False)
root.resizable(True, True)

root.config(width=1920, height=1080, bg="black")   #root의 크기를 지정한다
#root.config(bg="black")   #root의 크기를 지정한다


root.attributes("-fullscreen", True)


font = tkinter.font.Font(family='NanumBarunGothic Regular', size=80,weight='bold')
title_font = tkinter.font.Font(family='NanumBarunGothic Regular', size=80,weight='bold')

root.grid_columnconfigure(1,weight=1) # the text and entry frames column
#root.grid_rowconfigure(1,weight=1) # all frames row



SetButton= tkinter.Button(root, text="주문번호", bg = "black",fg ="yellow" , font = title_font)
ReadyButton= tkinter.Button(root, text="준비중", bg="black",fg ="white" , font = title_font)
NameButton = tkinter.Button(root, text="중앙대학교 중앙휴게실", bg="black",fg ="white" , font = title_font)

ListSet1= tkinter.Button(root, text="00A",bg = "black",fg ="yellow", font = font)
ListSet2= tkinter.Button(root, text="00B",bg="black",fg ="white" , font = font)
ListSet3= tkinter.Button(root, text="00C",bg="black",fg ="white" , font = font)
ListSet4= tkinter.Button(root, text="00D",bg="black",fg ="white" , font = font)
ListSet5= tkinter.Button(root, text="00E",bg="black",fg ="white" , font = font)

ListReady1= tkinter.Button(root, text="001",bg="black",fg ="white" ,  font = font)
ListReady2= tkinter.Button(root, text="002",bg="black",fg ="white" ,  font = font)
ListReady3= tkinter.Button(root, text="003",bg="black",fg ="white" ,  font = font)
ListReady4= tkinter.Button(root, text="004",bg="black",fg ="white" ,  font = font)
ListReady5= tkinter.Button(root, text="005",bg="black",fg ="white" ,  font = font)
ListReady6= tkinter.Button(root, text="006",bg="black",fg ="white" ,  font = font)


SetButton.grid(row=0, column=0, columnspan=2, sticky='EW')
ReadyButton.grid(row=0, column=2, columnspan=2, sticky='EW')
ListSet1.grid(row=1, column=0, columnspan=2, sticky='EWNS')

ListSet2.grid(row=2, column=0, columnspan=1, sticky='EWNS')
ListSet3.grid(row=2, column=1, columnspan=1, sticky='EWNS')

ListSet4.grid(row=3, column=0, columnspan=1, sticky='EWNS')
ListSet5.grid(row=3, column=1, columnspan=1, sticky='EWNS')




ListReady1.grid(row=1, column=2, columnspan=1, sticky='EWNS')
ListReady2.grid(row=1, column=3, columnspan=1, sticky='EWNS')
ListReady3.grid(row=2, column=2, columnspan=1, sticky='EWNS')
ListReady4.grid(row=2, column=3, columnspan=1, sticky='EWNS')
ListReady5.grid(row=3, column=2, columnspan=1, sticky='EWNS')
ListReady6.grid(row=3, column=3, columnspan=1, sticky='EWNS')

NameButton.grid(row=4,column=0,columnspan=4, sticky='EWNS')


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


root.bind('<Key>', key_input) 

def real_playsound():
    song = pyglet.media.load('bell.wav')
    song.play()
    pyglet.app.run()

def soundplay():
    global play_thread
    play_thread = Thread(target=real_playsound)
    play_thread.start()

def READ():
    ListSet1.configure(text=das)


root.focus_set()
root.mainloop() #프로그램의 다른 동작이 진행될 때 까지 기다린다.