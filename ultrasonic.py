import RPi.GPIO as GPIO
import time

                    
class Ultrasonic:


	def __init__(self):

		self.trig = 5
		self.echo = 6

		self.setup()

	def setup(self):

		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.trig, GPIO.OUT)
		GPIO.setup(self.echo, GPIO.IN)
		GPIO.output(self.trig, False)

	def calculateDistance(self):

		pulse_start = 0
		pulse_end   = 0

		time.sleep(0.01)
		GPIO.output(self.trig, True)
    		time.sleep(0.01)
    		GPIO.output(self.trig, False)

    		while GPIO.input(self.echo)==0:
      			pulse_start = time.time()

    		while GPIO.input(self.echo)==1:
      			pulse_end = time.time()

    		pulse_duration = pulse_end - pulse_start

    		distance = pulse_duration * 17150

    		distance = round(distance, 2)

		return distance



if __name__ == '__main__':
	us = Ultrasonic()

	while True:
        	try:
		    distance = us.calculateDistance()
		    print(distance)
            
	        except Exception, exc:
			print(exc)
                
	GPIO.cleanup()
