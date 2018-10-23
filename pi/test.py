# ssh
# ip addr
# ssh ip-adresse -l pi
# git clone https://github.com/simonmonk/make_action.git
# cd /home/pi/make_action
# git pull
# python test.py
# python3 test.py

import RPi.GPIO as GPIO  # (1)
import time              # (2)

GPIO.setmode(GPIO.BCM)   # (3)

control_pin = 18           # (4)
GPIO.setup(control_pin, GPIO.OUT)


try:         		  # (5)
    while True:       # (6)
        GPIO.output(control_pin, False) # (7)
        print("led aus")
        time.sleep(5) 
        GPIO.output(control_pin, True)
        print("led ein")
        time.sleep(2)                 
        
finally:  
    print("Cleaning up")
    GPIO.cleanup()
