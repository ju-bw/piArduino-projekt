#!/usr/bin/python3
# coding: utf-8
# python3 transistor.py

#https://bw1.eu/
#2017-09-16 13:02


#4-fach-Relaisboard
#Relais VCC + rasPi pin2 (5V)
#Relais GND + NPN-Transistor 1. Collector
#Relais Out + 12V Verbraucher - Schaltung

#NPN-Transistor BC547
#NPN-Transistor 1. Collector + Relais GND
#NPN-Transistor 2. Base      + 1k + rasPi pin 26
#NPN-Transistor 3. Emitter   + rasPi GND

#Raspberry Pi 2 - 900MHz quad-core ARM Cortex-A7 CPU, 1GB LPDDR2 SDRAM
#1x LED (1x Rot)
#1x Widerstand (220 Ohm)

#Schaltung
#LED (-) kurzer Pin + rasPi GND
#LED (+) langer Pin + Widerstand 220 + NPN-Transistor 3. Emitter

import time, sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
#physische Pin-Nummerierung
GPIO.setmode(GPIO.BOARD)

# Variablen ANPASSEN
#===================
info = "Info: Relais"

print(info)

#PIN-Nummer definieren
LED_01_PIN = 26

# Schaltet Pin in den Ausgabemodus
GPIO.setup(LED_01_PIN,GPIO.OUT)

print("LED an", sep="")
GPIO.output(LED_01_PIN, GPIO.HIGH)
time.sleep(5)
print("LED aus", sep="")
GPIO.output(LED_01_PIN, GPIO.LOW)
time.sleep(5)

#alle GPIO-Pins in Standardzustand
GPIO.cleanup()

print()
