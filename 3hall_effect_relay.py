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
    if (hallswitch1 == False and hallswitch2 == False and hallswitch3 == False):
        print ("first check all hallswitches: triggered")
        time.sleep(1)
        if (hallswitch1 == False and hallswitch2 == False and hallswitch3 == False):
            print ("final check all hallswitches: triggered")
            print ("turning off relay/maglock")
            GPIO.output(RelaySwitch, GPIO.HIGH)
            time.sleep(120)
            #make time longer about 2 min?
            print ("2 minutes finished, check again")
    else:
        if hallswitch1 == True:
            print ("hallswtich1 untriggered")
            GPIO.output(RelaySwitch, GPIO.LOW)
        if hallswitch2 == True:
            print ("hallswitch2 Untriggered")
            GPIO.output(RelaySwitch, GPIO.LOW)
        if hallswitch3 == True:
            print ("hallswitch3 Untriggered")   
            GPIO.output(RelaySwitch, GPIO.LOW)
        time.sleep(1)
