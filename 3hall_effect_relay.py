#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

#Sam, I expect that you will change this drastically to fit with the GUI. Go right ahead, this is a starter file - Adam

HallPin1 = 11 #will change to correct pin number
HallPin2 = 13 #will change to correct pin number
HallPin3 = 12 #will change to correct pin number
finished = 0
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

#the line directly under this was the code that was recommended with the Hall Effect Sensors
#channel = GPIO.wait_for_edge(HallPin, GPIO.RISING, timeout=60000)
#but we're using this as a button instead of a rising/falling call 

GPIO.setup(HallPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)    
GPIO.setup(HallPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)    
GPIO.setup(HallPin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)    
#Set BtnPin's mode is input, and pull up to high level(3.3V)

