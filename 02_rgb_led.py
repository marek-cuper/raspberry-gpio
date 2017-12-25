#!/usr/bin/python

# BCM 17 Blue
# BCM 18 Green
# BCM 22 Red
# -   09 Ground

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(17, GPIO.HIGH)
time.sleep(2)
GPIO.output(18, GPIO.HIGH)
time.sleep(2)
GPIO.output(22, GPIO.HIGH)
time.sleep(2)

GPIO.output(17, GPIO.LOW)
time.sleep(2)
GPIO.output(18, GPIO.LOW)
time.sleep(2)
GPIO.output(22, GPIO.LOW)

GPIO.cleanup()

D
C

A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A

