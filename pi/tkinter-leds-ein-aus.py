#!/usr/bin/python3
from tkinter import *
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)#Pins 1-40
gpio.setwarnings(False)  

pin1 = 37
pin2 = 35
pin3 = 33

gpio.setup(pin1, gpio.OUT)  
gpio.output(pin1, gpio.LOW)
gpio.setup(pin2, gpio.OUT)  
gpio.output(pin2, gpio.LOW)
gpio.setup(pin3, gpio.OUT)  
gpio.output(pin3, gpio.LOW)


# Reaktion auf Mausklick im Fenster
def pinChange1():
  if pinStatus1.get():
    gpio.output(pin1, gpio.HIGH)  
    lb1.configure(text='LED high')
  else:
    gpio.output(pin1, gpio.LOW)  
    lb1.configure(text='LED low')
def pinChange2():
  if pinStatus2.get():
    gpio.output(pin2, gpio.HIGH)  
    lb2.configure(text='LED high')
  else:
    gpio.output(pin2, gpio.LOW)  
    lb2.configure(text='LED low')
def pinChange3():
  if pinStatus3.get():
    gpio.output(pin3, gpio.HIGH)  
    lb3.configure(text='LED high')
  else:
    gpio.output(pin3, gpio.LOW)  
    lb3.configure(text='LED low')
    

# Benutzeroberfläche mit Ereignisverwaltung
root = Tk()
root.wm_title('LED ein/aus')#Titel
pinStatus1 = IntVar()
pinStatus2 = IntVar()
pinStatus3 = IntVar()
lb1 = Label(root, text='LED ist low')
btn1 = Checkbutton(root, text='LED ein/aus', indicatoron=0, variable=pinStatus1,command=pinChange1, padx=10, pady=10)
lb2 = Label(root, text='LED ist low')
btn2 = Checkbutton(root, text='LED ein/aus', indicatoron=0, variable=pinStatus2,command=pinChange2, padx=10, pady=10)
lb3 = Label(root, text='LED ist low')
btn3 = Checkbutton(root, text='LED ein/aus', indicatoron=0, variable=pinStatus3,command=pinChange3, padx=10, pady=10)
#grid
lb1.grid(row=0, column=0, padx=5, pady=5)
btn1.grid(row=1, column=0, padx=5, pady=5)
lb2.grid(row=0, column=1, padx=5, pady=5)
btn2.grid(row=1, column=1, padx=5, pady=5)
lb3.grid(row=0, column=3, padx=5, pady=5)
btn3.grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
gpio.cleanup()

#try:         		  
  #while True:       
    #root.mainloop()

#finally:
  #print("Cleaning up")
  #gpio.cleanup()


