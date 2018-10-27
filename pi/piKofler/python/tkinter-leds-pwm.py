#!/usr/bin/python3
from tkinter import *
import RPi.GPIO as gpio, signal
gpio.setmode(gpio.BOARD)#Pins 1-40
gpio.setwarnings(False)  

led1 = 37
led2 = 35
led3 = 33
gpio.setup(led1, gpio.OUT) 
gpio.setup(led2, gpio.OUT) 
gpio.setup(led3, gpio.OUT) 
pwm1 = gpio.PWM(led1, 1000)    # Frequenz: 1000 Hertz
pwm1.start(50)                 # Duty:     anfangs 50%
pwm2 = gpio.PWM(led2, 1000)    # Frequenz: 1000 Hertz
pwm2.start(50)                 # Duty:     anfangs 50%
pwm3 = gpio.PWM(led3, 1000)    # Frequenz: 1000 Hertz
pwm3.start(50)                 # Duty:     anfangs 50%



# Reaktion auf Mausklick im Fenster
def pwm_change(value):
  pwm1.ChangeDutyCycle(float(value))
  pwm2.ChangeDutyCycle(float(value))
  pwm3.ChangeDutyCycle(float(value))
  
# Programmende durch Windows-Close-Button
def win_close():
  gpio.cleanup()
  mywin.quit()

# Programmende durch Strg+C im Terminal
def strg_c(signal, frame):
  win_close()

# regelmäßiger Aufruf, damit Strg+C funktioniert
def do_nothing():
  mywin.after(200, do_nothing)

# Benutzeroberfläche
mywin = Tk()
mywin.wm_title('LED-Helligkeit')
lbl = Label(mywin, text='LED1 mit PWM steuern')
lb2 = Label(mywin, text='LED2 mit PWM steuern')
lb3 = Label(mywin, text='LED3 mit PWM steuern')
ledscale = Scale(mywin, from_=0, to=100, orient=HORIZONTAL, command=pwm_change)
ledscale.set(50)
lbl.grid(column=0, row=0, padx=5, pady=5)
lb2.grid(column=1, row=0, padx=5, pady=5)
lb3.grid(column=2, row=0, padx=5, pady=5)
ledscale.grid(column=0, row=1, padx=5, pady=5)
ledscale.grid(column=1, row=1, padx=5, pady=5)
ledscale.grid(column=2, row=1, padx=5, pady=5)

# Ereignisse
mywin.protocol("WM_DELETE_WINDOW", win_close) # ordentliches Programmende, wenn Fenster geschlossen wird
signal.signal(signal.SIGINT, strg_c) # auf Strg+C in Terminal reagieren
mywin.after(200, do_nothing)         # damit Strg+C funktioniert
mywin.mainloop()

