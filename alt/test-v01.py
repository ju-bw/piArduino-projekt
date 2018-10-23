#!/usr/bin/python3
# coding: utf-8
# python3 test.py

#https://bw1.eu/
#2017-09-16 13:02

import time, sys

# Variablen ANPASSEN
#===================
info = "Info: Python Test"

max = 3

print(info)

#Schleife 3x range(bis)
for i in range(max):
	print(i, "x ", "LED an", sep="")
	time.sleep(1)
	print(i, "x ", "LED aus", sep="")
	time.sleep(1)

print()

#Schleife 3x range(von,bis,schritt)
for i in range(1,4,1):
	print(i, "x ", "LED an", sep="")
	time.sleep(1)
	print(i, "x ", "LED aus", sep="")
	time.sleep(1)

print()
