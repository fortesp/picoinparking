import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(7,GPIO.OUT)
P = GPIO.PWM(7,50)
P.start(7.5)

try:
	while True:
		P.ChangeDutyCycle(7.5)	
		time.sleep(1)
		P.ChangeDutyCycle(12.5)  
                time.sleep(1)
		P.ChangeDutyCycle(2.5)  
                time.sleep(1)

except KeyboardInterrupt:
		GPIO.cleanup()
