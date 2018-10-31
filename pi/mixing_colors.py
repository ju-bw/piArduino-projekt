from tkinter import *       
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)  # (1)

ledPin1 = 35
ledPin2 = 33
ledPin3 = 37

GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)


pwmRed = GPIO.PWM(ledPin1, 500) # (2)
pwmRed.start(100)

pwmGreen = GPIO.PWM(ledPin2, 500)
pwmGreen.start(100)

pwmBlue = GPIO.PWM(ledPin3, 500)
pwmBlue.start(100)

class App:
    
    def __init__(self, master): #(3)
        frame = Frame(master)  #(4)
        frame.pack()
        
        Label(frame, text='Red').grid(row=0, column=0) # (5)
        Label(frame, text='Green').grid(row=1, column=0)
        Label(frame, text='Blue').grid(row=2, column=0)
        
        scaleRed = Scale(frame, from_=0, to=100,     # (6)
              orient=HORIZONTAL, command=self.updateRed)
        scaleRed.grid(row=0, column=1)
        scaleGreen = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.updateGreen)
        scaleGreen.grid(row=1, column=1)
        scaleBlue = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.updateBlue)
        scaleBlue.grid(row=2, column=1)

    def updateRed(self, duty):     # (7)
        # change the led brightness to match the slider
        pwmRed.ChangeDutyCycle(float(duty))

    def updateGreen(self, duty):
        pwmGreen.ChangeDutyCycle(float(duty))
    
    def updateBlue(self, duty):
        pwmBlue.ChangeDutyCycle(float(duty))


root = Tk()  # (8)
root.wm_title('RGB LED Control')
app = App(root)
root.geometry("400x150+0+0")
try:
    root.mainloop()
finally:  
    print("Cleaning up")
    GPIO.cleanup()
