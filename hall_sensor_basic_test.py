#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

HallPin = 11
finished = 0
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location

#channel = GPIO.wait_for_edge(HallPin, GPIO.RISING, timeout=60000)
GPIO.setup(HallPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    
# Set BtnPin's mode is input, and pull up to high level(3.3V)


#we're using this as a button instead of a rising/falling call 
while (finished == 0):
	hallswitch1 = GPIO.input(HallPin)
	if hallswitch1 == False:
		print ('hallswtich1 = False')
		time.sleep(1)
	if hallswitch1 == True:
		print ('hallswitch1 = True')
		time.sleep(1)

#Imbedded if statements and then do a final check one second later to make sure that it's not a weird error?

#do a final check where the door locks again 10 seconds after all 3 statues are removed.