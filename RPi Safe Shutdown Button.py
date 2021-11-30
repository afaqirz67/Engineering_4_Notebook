# RPi Safe shutdown Button
# Writen by Asadullah Faqirzada
# 11.30.2021

import time 
import RPI.GPIO as GPIO

reset_shutdown_pin = 26
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(reset_shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP
#GPIO.setup(reset_shutdown_pin, GPIO.IN)

def restart():
	print("restarting Pi")	
	command = "/usr/bin/sudo /sbin/shutdown -r now"
	import subprocess	
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
	print(output)

def shutdown():
	print("shutting down")
	command = "/usr/bin/sudo /sbin/shutdown -h now"
    	import subprocess
    	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    	output = process.communicate()[0]
    	print(output)

while True:
    #short delay, otherwise this code will take up a lot of the Pi's processing power
    time.sleep(0.5)

    # For troubleshooting, uncomment this line to output button status on command line
    #print('GPIO state is = ", GPIO.input(reset_shutdown_pin))
    if GPIO.input(reset_shutdown_pin) == False:
        counter = 0

        while GPIO.input(reset_shutdown_pin) == False:
            #For troubleshooting, uncomment this line to view the counter. If it reaches a value above 4, we will restart.     
            #print(counter)
            counter += 1
            time.sleep(0.5)

            # long button press
            if counter > 4:
                shut_down()

        #if short button press, restart!
        restart()
