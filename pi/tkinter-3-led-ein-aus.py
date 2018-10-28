#!/usr/bin/python3
from tkinter import *
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
#gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

ledPin1 = 19
ledPin2 = 19
ledPin3 = 19

gpio.setup(ledPin1, gpio.OUT)  
gpio.output(ledPin1, gpio.LOW)
gpio.setup(ledPin2, gpio.OUT)  
gpio.output(ledPin2, gpio.LOW)
gpio.setup(ledPin3, gpio.OUT)  
gpio.output(ledPin3, gpio.LOW)


# Reaktion auf Mausklick im Fenster
def led_change1():
  if ledstatus1.get():
    gpio.output(ledPin1, gpio.HIGH)  
    lb1.configure(text='LED leuchtet.')
  else:
    gpio.output(ledPin1, gpio.LOW)  
    lb1.configure(text='LED ausgeschalten.')
def led_change2():
  if ledstatus2.get():
    gpio.output(ledPin2, gpio.HIGH)  
    lb2.configure(text='LED leuchtet.')
  else:
    gpio.output(ledPin2, gpio.LOW)  
    lb2.configure(text='LED ausgeschalten.')
def led_change3():
  if ledstatus3.get():
    gpio.output(ledPin3, gpio.HIGH)  
    lb3.configure(text='LED leuchtet.')
  else:
    gpio.output(ledPin3, gpio.LOW)  
    lb3.configure(text='LED ausgeschalten.')
    

# Benutzeroberfläche mit Ereignisverwaltung
myWin = Tk()
myWin.wm_title('LED ein/aus')
ledstatus1 = IntVar()
ledstatus2 = IntVar()
ledstatus3 = IntVar()
lb1 = Label(myWin, text='LED ist ausgeschalten.')
btn1 = Checkbutton(myWin, text='LED ein-/aus', indicatoron=0, variable=ledstatus1,command=led_change1, padx=10, pady=10)
lb2 = Label(myWin, text='LED ist ausgeschalten.')
btn2 = Checkbutton(myWin, text='LED ein-/aus', indicatoron=0, variable=ledstatus2,command=led_change2, padx=10, pady=10)
lb3 = Label(myWin, text='LED ist ausgeschalten.')
btn3 = Checkbutton(myWin, text='LED ein-/aus', indicatoron=0, variable=ledstatus3,command=led_change3, padx=10, pady=10)
#grid
lb1.grid(row=0, column=0, padx=5, pady=5)
btn1.grid(row=1, column=0, padx=5, pady=5)
lb2.grid(row=0, column=0, padx=5, pady=5)
btn2.grid(row=1, column=0, padx=5, pady=5)
lb3.grid(row=0, column=0, padx=5, pady=5)
btn3.grid(row=1, column=0, padx=5, pady=5)

myWin.mainloop()
gpio.cleanup()

#try:         		  
  #while True:       
    #myWin.mainloop()

#finally:
  #print("Cleaning up")
  #gpio.cleanup()


