# coding=utf-8
import time
import datetime
import json
import servo, ultrasonic, qrlcd
import urllib2


address = "mhWPFDUxFrp6vgoeMNV8YER1wBJ6n438eD"
URL = "https://api.blockcypher.com/v1/btc/test3/addrs/" + address + "/full?limit=50"
PRICE = 1000
MINCONFIRMATIONS=0


def totimestamp(d):
	return time.mktime(datetime.datetime.strptime(d.split(".")[0], "%Y-%m-%dT%H:%M:%S").timetuple())

def fetchData():
	src = None
	data = ""
	try:
		src = urlopen(URL)
	        data = src.read()
	except (ValueError, RuntimeError, TypeError, NameError, urllib2.HTTPError):
		return False
	finally:
        	if src:
	            src.close()
	return json.loads(data)


us = ultrasonic.Ultrasonic()
servo = servo.Servo()

qrlcd = qrlcd.QRLCD()
qrlcd.blank()

print("System initialized.")
while True:
	payed = False
	distance = us.calculateDistance()
	if(distance < 4):
		print("Object detected.\nSending image to LCD.")
		st = time.time()
		qrlcd.send(address, str(float(PRICE)/100000) + " BTC")
		while not payed:
			print("Fetching data from API.")
			data = fetchData()
			if(data):
				amount = data['txs'][0]['outputs'][0]['value']
				confirmations = data['txs'][0]['confirmations']
				transactiontime = totimestamp(data['txs'][0]['received'])

				if(transactiontime > st and amount >= PRICE and confirmations >= MINCONFIRMATIONS): 
					payed = True
					qrlcd.send_image("success.bmp")
					time.sleep(1)
					qrlcd.blank()
					print("Payment successful!")

				time.sleep(3)
				if(int(time.time()-st) > 120): 
					print("Timeout.")
					break
			else: 
				print("No data from API.")
				break
	time.sleep(0.1)



