#!/usr/bin/python3
from tkinter import *
import RPi.GPIO as gpio, signal
gpio.setmode(gpio.BOARD)#Pins 1-40
gpio.setwarnings(False)  

pin1 = 37
pin2 = 35
pin3 = 33

gpio.setup(pin1, gpio.OUT) 
gpio.setup(pin2, gpio.OUT) 
gpio.setup(pin3, gpio.OUT) 

pwm1 = gpio.PWM(pin1, 1000)    # Frequenz: 1000 Hertz
pwm1.start(50)                 # Duty:     anfangs 50%
pwm2 = gpio.PWM(pin2, 1000)    # Frequenz: 1000 Hertz
pwm2.start(50)                 # Duty:     anfangs 50%
pwm3 = gpio.PWM(pin3, 1000)    # Frequenz: 1000 Hertz
pwm3.start(50)                 # Duty:     anfangs 50%



# Reaktion auf Mausklick im Fenster
def pwmChange1(value):
  pwm1.ChangeDutyCycle(float(value))
def pwmChange2(value):
  pwm2.ChangeDutyCycle(float(value))
def pwmChange3(value):
  pwm3.ChangeDutyCycle(float(value))
  
  
# Programmende durch Windows-Close-Button
def win_close():
  gpio.cleanup()
  root.quit()

# Programmende durch Strg+C im Terminal
def strg_c(signal, frame):
  win_close()

# regelmäßiger Aufruf, damit Strg+C funktioniert
def do_nothing():
  root.after(200, do_nothing)

# Benutzeroberfläche
root = Tk()         # Fenster
root.wm_title('PWM')# Titel

lbl = Label(root, text='pin1 mit PWM steuern')
lb2 = Label(root, text='pin2 mit PWM steuern')
lb3 = Label(root, text='pin3 mit PWM steuern')

pinscale1 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=pwmChange1)
pinscale1.set(50)
pinscale2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=pwmChange2)
pinscale2.set(50)
pinscale3 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=pwmChange3)
pinscale3.set(50)

lbl.grid(row=0, column=0, padx=5, pady=5)
lb2.grid(row=0, column=1, padx=5, pady=5)
lb3.grid(row=0, column=2, padx=5, pady=5)

pinscale1.grid(row=1, column=0, padx=5, pady=5)
pinscale2.grid(row=1, column=1, padx=5, pady=5)
pinscale3.grid(row=1, column=2, padx=5, pady=5)

# Ereignisse
root.protocol("WM_DELETE_WINDOW", win_close) # ordentliches Programmende, wenn Fenster geschlossen wird
signal.signal(signal.SIGINT, strg_c) # auf Strg+C in Terminal reagieren
root.after(200, do_nothing)          # damit Strg+C funktioniert

root.mainloop()

