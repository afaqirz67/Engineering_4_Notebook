# RPI GPIO Pin Introduction
# Written by Asadullah Faqirzada
# 11.18.2021


import RPi.GPIO as GPIO  # imports RPi.GPIO library it can be refered to as GPIO
import time 		 # time library 
GPIO.setmode(GPIO.BCM)   # Uses the Boardcom pin-numbering scheme

led1 = 20		# Assigns pin 20 as led1 for better recognition
led2 = 21		# ...

GPIO.setup(led1, GPIO.OUT, initial=GPIO.LOW) # It starts with off leds	
GPIO.setup(led2, GPIO.OUT, initial=GPIO.LOW) # Both leds are off

while True:
	GPIO.setwarnings(False) # Disables warnings caused by confusion of whether the pin is being configured with something other than the default input
	print('LED1 on') 	# prints the message when led1 turns on
	GPIO.output(led1, GPIO.HIGH) # led1 turns on
	time.sleep(1.0)		     # waits for 1 sec
	print('LED1 off')	     # prints the message when it turn off
	GPIO.output(led1, GPIO.LOW)  # led1 turns off
	time.sleep(1.0)		     # waits for 1 sec
	print('LED2 on')    	     # repeats everyting in the loop function for led2
	GPIO.output(led2, GPIO.HIGH)
	time.sleep(1.0)
	print('LED2 off')
	GPIO.output(led2, GPIO.LOW)
	time.sleep(1.0)

