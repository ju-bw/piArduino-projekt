import time    
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)  # Positionsnummern: Pins 1-40
GPIO.setwarnings(False)

controlPin = 35

GPIO.setup(controlPin, GPIO.OUT)

try:         
  while True:
    GPIO.output(controlPin, False)  
    print("low - Signal: 5s")
    time.sleep(5)                 
    GPIO.output(controlPin, True) 
    print("high - Signal: 2s")
    time.sleep(2)                 
        
finally:  
  print("Cleaning up")
  GPIO.cleanup()