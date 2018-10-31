from tkinter import *       
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)  # (1)
# led
ledPin1 = 35
ledPin2 = 33
ledPin3 = 37
# motor
antriebVor = 12
antriebBack = 16
lenkungLeft = 18
lenkungRight = 22
# led
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)
# motor
GPIO.setup(antriebVor, GPIO.OUT) 
GPIO.setup(antriebBack, GPIO.OUT) 
GPIO.setup(lenkungLeft, GPIO.OUT) 
GPIO.setup(lenkungRight, GPIO.OUT) 
# led
pwmRed = GPIO.PWM(ledPin1, 500) # (2)
pwmRed.start(0)
pwmGreen = GPIO.PWM(ledPin2, 500)
pwmGreen.start(0)
pwmBlue = GPIO.PWM(ledPin3, 500)
pwmBlue.start(0)
# motor
pwmVor = GPIO.PWM(antriebVor, 500)
pwmVor.start(0)
pwmBack = GPIO.PWM(antriebBack, 500)
pwmBack.start(0)
pwmLeft = GPIO.PWM(lenkungLeft, 500)
pwmLeft.start(0)
pwmRight = GPIO.PWM(lenkungRight, 500)
pwmRight.start(0)

class App:
    
    def __init__(self, master): #(3)
        frame = Frame(master)  #(4)
        frame.pack()
        # led
        Label(frame, text='Red').grid(row=0, column=0) # (5)
        Label(frame, text='Green').grid(row=1, column=0)
        Label(frame, text='Blue').grid(row=2, column=0)
        # motor
        Label(frame, text='Antrieb vor').grid(row=3, column=0) 
        Label(frame, text='Antrieb back').grid(row=4, column=0)
        Label(frame, text='Lenkung links').grid(row=5, column=0)
        Label(frame, text='Lenkung rechts').grid(row=6, column=0)
        
        # led
        scaleRed = Scale(frame, from_=0, to=100,     # (6)
              orient=HORIZONTAL, command=self.updateRed)
        scaleRed.grid(row=0, column=1)
        scaleGreen = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.updateGreen)
        scaleGreen.grid(row=1, column=1)
        scaleBlue = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.updateBlue)
        scaleBlue.grid(row=2, column=1)

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

    # led
    def updateRed(self, duty):     # (7)
        # Ändert die LED-Helligkeit entsprechend der Reglerstellung
        pwmRed.ChangeDutyCycle(float(duty))

    def updateGreen(self, duty):
        pwmGreen.ChangeDutyCycle(float(duty))
    
    def updateBlue(self, duty):
        pwmBlue.ChangeDutyCycle(float(duty))

    # motor
    def updateVor(self, duty):     # (7)
        # Ändert die Motorgeschwindigkeit entsprechend der Reglerstellung
        pwmVor.ChangeDutyCycle(float(duty))

    def updateBack(self, duty):
        pwmBack.ChangeDutyCycle(float(duty))
    
    def updateLeft(self, duty):
        pwmLeft.ChangeDutyCycle(float(duty))

    def updateRight(self, duty):
        pwmRight.ChangeDutyCycle(float(duty))

root = Tk()  # (8)
root.wm_title('LED & Motor Control')
app = App(root)
root.geometry("300x300+0+0")
try:
    root.mainloop()
finally:  
    print("Cleaning up")
    GPIO.cleanup()
