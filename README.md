# picoinparking
Car Parking System simulator
## A Raspberry Pi project 


This is a simulation of a car parking payment system that requires the crypto currency 
e.g. Bitcoin, as payment method. 
The system will detect that the vehicle is close to the payment device using a Sensor component, and then it presents a QR code image referred to a Bitcoin public address and total due, using a LCD component, so that the user can read the total due and scan the code to conveniently pay with a Smartphone. The system will then check whether the payment it’s confirmed, and if yes, rotate a servo to simulate opening of a parking gate. However due to some unpredictable issues, some adaptations to the initial solution have been made.
  
## Components
The hardware components used are the following.
- Raspberry Pi Zero W with header
- Ultra sound sensor
- Micro USB cable
- LCD TFT 1.8 res. 128x160, 262K colors.
- Servo 1.6Kg
- Micro SD card


## Assembly

1.	Raspberry Pi Setup.
       - Connect Micro USB cable to Pi in Data port.
       - Format Micro SD card.
       - Extract Raspbian Stretch Lite into Micro SD.
       - Change boot.txt configuration to allow SSH connection.
       - Connect Pi to a computer, using Data port to setup wifi.
2.	Connect components to Raspberry Pi pin-out header using Jumper cables.
3.	Match the pinout with the pinout configuration of  the code.
4.	Upload Python code using SSH to the Pi.
5.	Run the code (main.py).



## File structure
The following file structure is used to make it work.
- arialbd.ttf  - Font file to show the total due on the LCD screen
- lcd.py  - Class exclusive for LCD component
- qrlcd.py – Imports lcd.py. Class to deal with the QR together with LCD class
- servo.py – Class exclusive for Servo component.
- ultrasonic.py – Class exclusive for Sensor component.
- main.py – Imports the majority of the classes. File with all the main logic pertaining to sequence of actions and payment system.
- success.bmp – Image to be shown after successful payment.
