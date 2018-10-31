# gui - robot
from tkinter import *       
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)  # Pins 1-40
# led
ledPin1 = 35
ledPin2 = 33
ledPin3 = 37
# motor
antriebVorPin = 12
antriebBackPin = 16
lenkungLeftPin = 18
lenkungRightPin = 22
# led
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)
# motor
GPIO.setup(antriebVorPin, GPIO.OUT) 
GPIO.setup(antriebBackPin, GPIO.OUT) 
GPIO.setup(lenkungLeftPin, GPIO.OUT) 
GPIO.setup(lenkungRightPin, GPIO.OUT) 
# led - Pulsweitenmodulation, um helligkeit zu steuern
# Frequenz: 500 Hertz
pwmLed1 = GPIO.PWM(ledPin1, 500) 
pwmLed1.start(0) # Duty:     anfangs 0%
pwmLed2 = GPIO.PWM(ledPin2, 500)
pwmLed2.start(0)
pwmLed3 = GPIO.PWM(ledPin3, 500)
pwmLed3.start(0)
# motor
# Frequenz: 500 Hertz
pwmVor = GPIO.PWM(antriebVorPin, 500)
pwmVor.start(0) # Duty:     anfangs 0%
pwmBack = GPIO.PWM(antriebBackPin, 500)
pwmBack.start(0)
pwmLeft = GPIO.PWM(lenkungLeftPin, 500)
pwmLeft.start(0)
pwmRight = GPIO.PWM(lenkungRightPin, 500)
pwmRight.start(0)

class App:
    def __init__(self, master): 
        frame = Frame(master)  # Rahmen
        frame.pack()
        # Erstellt die Beschriftungen und platziert sie im Raster
        # led 
        Label(frame, text='LED 1').grid(row=0, column=0) 
        Label(frame, text='LED 2').grid(row=1, column=0)
        Label(frame, text='LED 3').grid(row=2, column=0)
        # motor
        Label(frame, text='Antrieb vor').grid(row=3, column=0) 
        Label(frame, text='Antrieb back').grid(row=4, column=0)
        Label(frame, text='Lenkung links').grid(row=5, column=0)
        Label(frame, text='Lenkung rechts').grid(row=6, column=0)
        # Erstellt die Schieberegler und platziert sie im Raster
        # led
        scaleLed1 = Scale(frame, from_=0, to=100,    
              orient=HORIZONTAL, command=self.updateLed1)
        scaleLed1.grid(row=0, column=1)
        scaleLed2 = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.updateLed2)
        scaleLed2.grid(row=1, column=1)
        scaleLed3 = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.updateLed3)
        scaleLed3.grid(row=2, column=1)
        # motor
        scaleVor = Scale(frame, from_=0, to=100,     
              orient=HORIZONTAL, command=self.updateVor)
        scaleVor.grid(row=3, column=1)
        scaleBack = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.updateBack)
        scaleBack.grid(row=4, column=1)
        scaleLeft = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.updateLeft)
        scaleLeft.grid(row=5, column=1)
        scaleRight = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.updateRight)
        scaleRight.grid(row=6, column=1)

    # Methoden
    # Ändert die LED-Helligkeit entsprechend der Reglerstellung
    # led
    def updateLed1(self, duty):     
        pwmLed1.ChangeDutyCycle(float(duty))
    def updateLed2(self, duty):
        pwmLed2.ChangeDutyCycle(float(duty))
    def updateLed3(self, duty):
        pwmLed3.ChangeDutyCycle(float(duty))

    # Ändert die Motorgeschwindigkeit entsprechend der Reglerstellung
    # motor
    def updateVor(self, duty):     
        pwmVor.ChangeDutyCycle(float(duty))
    def updateBack(self, duty):
        pwmBack.ChangeDutyCycle(float(duty))
    def updateLeft(self, duty):
        pwmLeft.ChangeDutyCycle(float(duty))
    def updateRight(self, duty):
        pwmRight.ChangeDutyCycle(float(duty))

# Startet die GUI und legt Namen, Größe und Position des Fensters fest
root = Tk()  # Fenster
root.wm_title('LED & Motor PWM Control')
app = App(root)
root.geometry("350x300+0+0")# breite x höhe + Posistion
try:
    root.mainloop()
finally:  
    print("Cleaning up")
    GPIO.cleanup()
