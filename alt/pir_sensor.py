#!/usr/bin/python3
# coding: utf-8
# python3 pir_sensor.py

#https://bw1.eu/
#2017-09-16 13:02

# PIR-Sensor HC-SR501 = Bewegungsmelder

#Auf dem Sensormodul befinden sich an der Unterseite zwei Poti.:
#Poti1 S Empfindlichkeit: 3 bis 7 Meter
#Poti2 t Verzögerungszeit: 5 bis 300 Sekunden

#Raspberry Pi 2 - 900MHz quad-core ARM Cortex-A7 CPU, 1GB LPDDR2 SDRAM
#1x Led
#1x Widerstand (220)


#Schaltung:
#LED (-) kurzer Pin + rasPi GND
#LED (+) langer Pin + Widerstand 220 + rasPi Pin 26

#PIR-Sensor VCC + rasPi pin 2 5V
#PIR-Sensor GND + rasPi GND
#PIR-Sensor Out + rasPi pin 24

import RPi.GPIO as GPIO
import time, sys

GPIO.setwarnings(False)
#physische Pin-Nummerierung
GPIO.setmode(GPIO.BOARD)

# Variablen ANPASSEN
#===================
INFO = "Info: Bewegungsmelder"

print(INFO)

#PIN-Nummer definieren
LED_01_PIN = 26
PIR_01_PIN = 24

# Pin als Ausgang
GPIO.setup(LED_01_PIN, GPIO.OUT)
# Pin als Eingang
#internen Pull-down-Widerstand aktivieren
GPIO.setup(PIR_01_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def bewegung(pin):
    print("Bewegung erkannt!")
    return

# Event
# GPIO.RISING = nur bei steigender Flanke reagieren
# Überwachung 
GPIO.add_event_detect(PIR_01_PIN, GPIO.RISING)
GPIO.add_event_callback(PIR_01_PIN, bewegung)


#Programm schläft und wartet auf Taster oder Strg + C
#dadurch CPU-Auslastung minimal
try:
	while True:
		time.sleep(3)
		print("Programm schläft und wartet auf [Bewegungsmelder] oder [Strg + C]")
except KeyboardInterrupt:
	GPIO.cleanup()
	sys.exit

