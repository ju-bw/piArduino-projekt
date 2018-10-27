#!/usr/bin/python3
from tkinter import *
import RPi.GPIO as gpio
#gpio.setmode(gpio.BOARD)
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

ledPin = 19
gpio.setup(ledPin, gpio.OUT)  
gpio.output(ledPin, gpio.LOW)

# Reaktion auf Mausklick im Fenster
def led_change():
  if ledstatus.get():
    gpio.output(ledPin, gpio.HIGH)  
    lbl.configure(text='Die LED leuchtet.')
  else:
    gpio.output(ledPin, gpio.LOW)  
    lbl.configure(text='Die LED ausgeschalten.')

# Benutzeroberfläche mit Ereignisverwaltung
mywin = Tk()
mywin.wm_title('LED ein/aus')
ledstatus = IntVar()
lbl = Label(mywin, text='Die LED ist ausgeschalten.')
ledbtn = Checkbutton(mywin, text='LED ein-/ausschalten', 
                     indicatoron=0, variable=ledstatus,
                     command=led_change, padx=10, pady=10)
lbl.grid(column=0, row=0, padx=5, pady=5)
ledbtn.grid(column=0, row=1, padx=5, pady=5)

mywin.mainloop()

#try:         		  
  #while True:       
    #mywin.mainloop()

#finally:
  #print("Cleaning up")
  #gpio.cleanup()


