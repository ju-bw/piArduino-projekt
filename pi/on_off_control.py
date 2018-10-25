import RPi.GPIO as GPIO  
import time              

GPIO.setmode(GPIO.BCM)   

ledPin = 18           
GPIO.setup(ledPin, GPIO.OUT)


try:         		  
  while True:       
    GPIO.output(ledPin, False)
    print("led an")  
    time.sleep(5) # sekunden
    GPIO.output(ledPin, True)
    print("led aus")
    time.sleep(2) # sekunden

finally:
  print("Cleaning up")
  GPIO.cleanup()
