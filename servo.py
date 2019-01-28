import RPi.GPIO as GPIO
import time


class Servo():


	def __init__(self):
		self.setup()

	def setup(self):
		GPIO.setmode(GPIO.BCM) 
		GPIO.setup(26, GPIO.OUT)
		self.p = GPIO.PWM(26, 50)
		self.p.start(7.5)

	def move(self, angle):
		duty = (angle/18.0) + 2.5
		self.p.ChangeDutyCycle(duty)
		print("direction =", angle, "-> duty =", duty)
		time.sleep(0.5) 



if __name__ == '__main__':
	servo = Servo()
	servo.move(0)
	servo.move(90)
	servo.move(180)

	GPIO.cleanup()	
