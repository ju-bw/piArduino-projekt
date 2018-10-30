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
gpio.output(pin1, gpio.LOW)
gpio.output(pin2, gpio.LOW)
gpio.output(pin3, gpio.LOW)

# pwm
pwm1 = gpio.PWM(pin1, 1000)    # Frequenz: 1000 Hertz
pwm1.start(0)                 # Duty:     anfangs 50%
pwm2 = gpio.PWM(pin2, 1000)    # Frequenz: 1000 Hertz
pwm2.start(0)                 # Duty:     anfangs 50%
pwm3 = gpio.PWM(pin3, 1000)    # Frequenz: 1000 Hertz
pwm3.start(0)                 # Duty:     anfangs 50%

# Reaktion auf Mausklick im Fenster
def pwmChange1(value):
  pwm1.ChangeDutyCycle(float(value))
#def pwmChange2(value):
  #pwm2.ChangeDutyCycle(float(value))
#def pwmChange3(value):
  #pwm3.ChangeDutyCycle(float(value))

# ein/aus
# Reaktion auf Mausklick im Fenster
def pinChange1():
  if pinStatus1.get():
    pwmChange1
    gpio.output(pin1, gpio.HIGH)  
    lb1.configure(text='high') 
  else:
    gpio.output(pin1, gpio.LOW)  
    lb1.configure(text='low')
def pinChange2():
  if pinStatus2.get():
    gpio.output(pin2, gpio.HIGH)  
    lb2.configure(text='high')
  else:
    gpio.output(pin2, gpio.LOW)  
    lb2.configure(text='low')
def pinChange3():
  if pinStatus3.get():
    gpio.output(pin3, gpio.HIGH)  
    lb3.configure(text='high')
  else:
    gpio.output(pin3, gpio.LOW)  
    lb3.configure(text='low')
  
  
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
root.wm_title('LED Ein/Aus - PWM')# Titel

# ein/aus
pinStatus1 = IntVar()
pinStatus2 = IntVar()
pinStatus3 = IntVar()
# label - ein/aus
lb1 = Label(root, text='LED ist low')
btn1 = Checkbutton(root, text='LED ein/aus', indicatoron=0, variable=pinStatus1,command=pinChange1, padx=10, pady=10)
lb2 = Label(root, text='LED ist low')
btn2 = Checkbutton(root, text='LED ein/aus', indicatoron=0, variable=pinStatus2,command=pinChange2, padx=10, pady=10)
lb3 = Label(root, text='LED ist low')
btn3 = Checkbutton(root, text='LED ein/aus', indicatoron=0, variable=pinStatus3,command=pinChange3, padx=10, pady=10)

# label - pwm
lb4 = Label(root, text='PWM 1 steuern')
lb5 = Label(root, text='PWM 2 steuern')
lb6 = Label(root, text='PWM 3 steuern')

# scale - pwm
pinscale4 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=pinChange1)
pinscale4.set(0)
#pinscale5 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=pwmChange2)
#pinscale5.set(50)
#pinscale6 = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=pwmChange3)
#pinscale6.set(50)


# grid - ein/aus
# label - 1. Zeile u. 1., 2., 3. Spalte
lb1.grid(row=0, column=0, padx=5, pady=5)
lb2.grid(row=0, column=1, padx=5, pady=5)
lb3.grid(row=0, column=2, padx=5, pady=5)
# button - 2. Zeile u. 1., 2., 3. Spalte 
btn1.grid(row=1, column=0, padx=5, pady=5)
btn2.grid(row=1, column=1, padx=5, pady=5)
btn3.grid(row=1, column=2, padx=5, pady=5)

# grid - pwm
# label - 3. Zeile u. 1., 2., 3. Spalte
lb4.grid(row=2, column=0, padx=5, pady=5)
lb5.grid(row=2, column=1, padx=5, pady=5)
lb6.grid(row=2, column=2, padx=5, pady=5)
# scale - 4. Zeile u. 1., 2., 3. Spalte
pinscale4.grid(row=3, column=0, padx=5, pady=5)
#pinscale5.grid(row=3, column=1, padx=5, pady=5)
#pinscale6.grid(row=3, column=2, padx=5, pady=5)

# Ereignisse
root.protocol("WM_DELETE_WINDOW", win_close) # ordentliches Programmende, wenn Fenster geschlossen wird
signal.signal(signal.SIGINT, strg_c) # auf Strg+C in Terminal reagieren
root.after(200, do_nothing)          # damit Strg+C funktioniert

root.mainloop()

