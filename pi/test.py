import RPi.GPIO as GPIO  # (1)
import time              # (2)

GPIO.setmode(GPIO.BCM)   # (3)

control_pin = 18           # (4)
GPIO.setup(control_pin, GPIO.OUT)


try:         		  # (5)
    while True:       # (6)
        GPIO.output(control_pin, False) # (7)
        print("led aus - warte 5s")
        time.sleep(5) 
        GPIO.output(control_pin, True)
        print("led ein- warte 2s")
        time.sleep(2)                 
        
finally:  
    print("Cleaning up")
    GPIO.cleanup()
