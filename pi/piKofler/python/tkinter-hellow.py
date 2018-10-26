#!/usr/bin/python3
from tkinter import *
import tkinter.font as tkf
mywin = Tk()                  # Fenster
mywin.wm_title('Hello World') # Titel
myfont = tkf.Font(size=20)    # Schrift
mylabel = Label(mywin, text='Hello World!', font=myfont) # Textfeld
mylabel.pack()   # Fenster sichtbar machen
mywin.mainloop() # Ereignisverwaltung

