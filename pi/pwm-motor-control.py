import time    
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)  # Positionsnummern: Pins 1-40
GPIO.setwarnings(False)

controlPin = 35   

GPIO.setup(controlPin, GPIO.OUT)
pwm = GPIO.PWM(controlPin, 500) 
pwm.start(0)                    

try:         
  while True:                     
    duty = int(input('Eingabe: Tastgrad (0 to 100): '))
    if duty < 0 or duty > 100:
      print('0 to 100')
    else:
      pwm.ChangeDutyCycle(duty)
        
finally:  
  print("Cleaning up")
  GPIO.cleanup()