#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

#Sam, I expect that you will change this drastically to fit with the GUI. Go right ahead, this is a starter file - Adam

HallPin1 = 2 #Physical pin 3
HallPin2 = 3 #Physical pin 5
HallPin3 = 4 #Physical pin 7
finished = 0
RelaySwitch = 14 #BCM of output for relay
GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by BCM location

#the line directly under this was the code that was recommended with the Hall Effect Sensors
#channel = GPIO.wait_for_edge(HallPin, GPIO.RISING, timeout=60000)
#but we're using this as a button instead of a rising/falling call 

GPIO.setup(HallPin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)    
#Set mode as input, and pull up to high level(3.3V)
GPIO.setup(HallPin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)    
GPIO.setup(HallPin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(RelaySwitch, GPIO.OUT)
GPIO.output(RelaySwitch, GPIO.LOW) #set to low, relay should be set on Normally Open
 
while (finished == 0):
	hallswitch1 = GPIO.input(HallPin1)
	hallswitch2 = GPIO.input(HallPin2)
	hallswitch3 = GPIO.input(HallPin3)
	if (hallswitch1 == True and hallswitch2 == True and hallswitch3 == True):
		print "first check all hallswitches = True"
		time.sleep(1)
		if (hallswitch1 == True and hallswitch2 == True and hallswitch3 == True):
		print "final check all hallswitches = True"
		GPIO.output(RelaySwitch, GPIO.HIGH)
		time.sleep(120)
		print "2 minutes finished, check again"
	else
		if hallswitch1 == False:
			print "hallswtich1 = False"
			GPIO.output(RelaySwitch, GPIO.LOW)
		if hallswitch2 == False:
			print "hallswitch2 = False"
			GPIO.output(RelaySwitch, GPIO.LOW)
		if hallswitch3 == False:
			print "hallswitch3 = False"	
			GPIO.output(RelaySwitch, GPIO.LOW)
		time.sleep(1)
