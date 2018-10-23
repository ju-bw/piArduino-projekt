#!/usr/bin/python3
# coding: utf-8
# python3 led_blinken.py

#https://bw1.eu/
#2017-09-16 13:02


#LED blinken

#Raspberry Pi 2 - 900MHz quad-core ARM Cortex-A7 CPU, 1GB LPDDR2 SDRAM
#1x LED (1x Rot)
#1x Widerstand (220 Ohm)

#Schaltung
#LED (-) kurzer Pin + rasPi GND
#LED (+) langer Pin + Widerstand 220 + rasPi Pin 26

import time, sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
#physische Pin-Nummerierung
GPIO.setmode(GPIO.BOARD)

# Variablen ANPASSEN
#===================
info = "Info: LED blinken"

print(info)

#PIN-Nummer definieren
LED_01_PIN = 26

# Schaltet Pin in den Ausgabemodus
GPIO.setup(LED_01_PIN,GPIO.OUT)

#Schleife 5x range(von,bis,schritt)
for i in range(1,6,1):
	print(i, "x ", "LED an", sep="")
	GPIO.output(LED_01_PIN, GPIO.HIGH)
	time.sleep(1)
	print(i, "x ", "LED aus", sep="")
	GPIO.output(LED_01_PIN, GPIO.LOW)
	time.sleep(1)

#alle GPIO-Pins in Standardzustand
GPIO.cleanup()

print()
