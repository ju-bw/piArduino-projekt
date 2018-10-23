#!/usr/bin/python3
# coding: utf-8
# python3 pwm.py

#https://bw1.eu/
#2017-09-16 13:02


#Duty-Cycle = prozentualer Anteil der High-Phase

# Parameter | Duty-Cycle in Prozent
# 0         |   0%
# 64        |  25%
# 128       |  50%
# 192       |  75%
# 255       | 100%

# Dämon-Programm im Hintergrund starten
# $ sudo pigpiod

#Generierung von PWM-Signalen
import pigpio
import time

# Variablen ANPASSEN
#===================
info = "Info: PWM - LEDs dimmen"

#PIN-Nummer definieren
#BCM 7 (physischer Pin 26)
LED_01_PIN = 7

pi = pigpio.pi()
#Pin als Ausgang

pi.set_mode(LED_01_PIN, pigpio.OUTPUT) 

# wert von 0 bis 255
dc = 0

#100 Hertz (Hz)
#Frequenzen von 10 bis 8000 Hz möglich
pi.set_PWM_frequency(LED_01_PIN,100)
print(pi.get_PWM_frequency(LED_01_PIN), "Hz")

#Helligkeit der LED
for dc in range(256):
	print(dc)
	pi.set_PWM_dutycycle(LED_01_PIN,dc)
	dc=dc+1
	time.sleep(.1)



time.sleep(3)
pi.write(LED_01_PIN,0)
pi.stop()

print()
