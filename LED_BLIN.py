import Rpi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

led1 = 20
led2 = 21

GPIO.setup(led1, GPIO.OUT, initial=GPIO.LOW)	
GPIO.setup(led2, GPIO.OUT, intial=GPIO.LOW)

while True:

	print 'LED1 on'
	GPIO.output(led1, GPIO.HIGH)
	time.sleep(1.0)
	print 'LED1 off'
	GPIO.output(led1, GPIO.LOW)

	print 'LED2 on'
	GPIO.output(led2, GPIO.HIGH)
	time.sleep(1.0)
	GPIO.output(led2, GPIO.LOW)
	time.sleep(1.0)

