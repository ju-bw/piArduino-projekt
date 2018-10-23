#!/usr/bin/python3
# coding: utf-8
# python3 taster.py

#https://bw1.eu/
#2017-09-16 13:02

#Raspberry Pi 2 - 900MHz quad-core ARM Cortex-A7 CPU, 1GB LPDDR2 SDRAM
#1x Led
#1x Widerstand (220)
#1x Widerstand (10k)
#1x Taster

#Schaltung:
#LED (-) kurzer Pin + rasPi GND
#LED (+) langer Pin + Widerstand 220 + rasPi Pin 24

#Taster one side    + rasPi GND
#Taster second side + Widerstand 10k + rasPi pin 26

import RPi.GPIO as GPIO
import time, sys

GPIO.setwarnings(False)
#physische Pin-Nummerierung
GPIO.setmode(GPIO.BOARD)

# Variablen ANPASSEN
#===================
INFO = "Info: Taster"

print(INFO)

#PIN-Nummer definieren
LED_01_PIN = 24
TASTER_01_PIN = 26


# Pin als Ausgang
GPIO.setup(LED_01_PIN, GPIO.OUT)
# Pin als Eingang
#internen Pull-up-Widerstand aktivieren
GPIO.setup(TASTER_01_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(LED_01_PIN, False)

def led_an (TASTER_01_PIN):
	if GPIO.input (TASTER_01_PIN) == True:
		GPIO.output(LED_01_PIN, False)
		print ("LED aus")
	else:
		GPIO.output(LED_01_PIN, True)
		print ("LED ein")

# Event
# GPIO.BOTH = auf Zustandswechsel reagieren
# Überwachung des Tasters
GPIO.add_event_detect(TASTER_01_PIN,GPIO.BOTH)
GPIO.add_event_callback(TASTER_01_PIN, led_an)

#Programm schläft und wartet auf Taster oder Strg + C
#dadurch CPU-Auslastung minimal
try:
	while True:
		time.sleep(3)
		print("Programm schläft und wartet auf [Taster betätigen] oder [Strg + C]")
except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit



