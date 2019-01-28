import wiringpi
from wiringpi import (pinMode, digitalWrite, shiftOut,
                  LOW, HIGH, INPUT, OUTPUT, MSBFIRST)
import time

class LCD:

    def __init__(self):

        self.scl = 14
        self.sda = 12
        self.rs  = 1
        self.cs  = 2
        self.rst = 0

        self.size = (128, 160)

	self.reset()
	self.setup()


    def setup(self):

        wiringpi.wiringPiSetup()

        pinMode(self.scl, OUTPUT)
        pinMode(self.sda, OUTPUT)
        pinMode(self.rs, OUTPUT)
        pinMode(self.cs, OUTPUT)
        pinMode(self.rst, OUTPUT)

        self.lcd_initial()

    def sleep(self, t):
	time.sleep(t/100)        


    def LCD_CtrlWrite_IC(self, c):
        digitalWrite(self.cs, LOW)
        digitalWrite(self.rs, LOW)
        digitalWrite(self.sda, c & 128)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 64)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 32)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 16)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 8)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 4)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 2)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 1)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.cs, HIGH)


    def LCD_DataWrite_IC(self, d):
        digitalWrite(self.cs, LOW)
        digitalWrite(self.rs, HIGH)
        digitalWrite(self.sda, d & 128)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 64)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 32)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 16)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 8)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 4)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 2)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 1)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.cs, HIGH)


    def LCD_DataWrite(self, LCD_DataH, LCD_DataL):
        self.LCD_DataWrite_IC(LCD_DataH)
        self.LCD_DataWrite_IC(LCD_DataL)


    def write_command(self, c):
        digitalWrite(self.cs, LOW)
        digitalWrite(self.rs, LOW)
        digitalWrite(self.sda, c & 128)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 64)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 32)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 16)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 8)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 4)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 2)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, c & 1)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.cs, HIGH)



    def write_data(self, d):
        digitalWrite(self.cs, LOW)
        digitalWrite(self.rs, HIGH)
        digitalWrite(self.sda, d & 128)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 64)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 32)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 16)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 8)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 4)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 2)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.sda, d & 1)
        digitalWrite(self.scl, LOW)
        digitalWrite(self.scl, HIGH)
        digitalWrite(self.cs, HIGH)


    def reset(self):
        digitalWrite(self.rst, LOW)
        self.sleep(10)
        digitalWrite(self.rst, HIGH)
        self.sleep(10)
	self.blank()
	self.sleep(50)

    def blank(self):
	self.fill_display(255, 255, 255)

    def lcd_initial(self):
        digitalWrite(self.rst, LOW)
        self.sleep(10)
        digitalWrite(self.rst, HIGH)
        self.sleep(10)
        self.write_command(17)
        self.sleep(12)
        self.write_command(177)
        self.write_data(1)
        self.write_data(44)
        self.write_data(45)
        self.write_command(178)
        self.write_data(1)
        self.write_data(44)
        self.write_data(45)
        self.write_command(179)
        self.write_data(1)
        self.write_data(44)
        self.write_data(45)
        self.write_data(1)
        self.write_data(44)
        self.write_data(45)
        self.write_command(180)
        self.write_data(7)
        self.write_command(192)
        self.write_data(162)
        self.write_data(2)
        self.write_data(132)
        self.write_command(193)
        self.write_data(197)
        self.write_command(194)
        self.write_data(10)
        self.write_data(0)
        self.write_command(195)
        self.write_data(138)
        self.write_data(42)
        self.write_command(196)
        self.write_data(138)
        self.write_data(238)
        self.write_command(197)
        self.write_data(14)
        self.write_command(54)
        self.write_data(200)
        self.write_command(224)
        self.write_data(15)
        self.write_data(26)
        self.write_data(15)
        self.write_data(24)
        self.write_data(47)
        self.write_data(40)
        self.write_data(32)
        self.write_data(34)
        self.write_data(31)
        self.write_data(27)
        self.write_data(35)
        self.write_data(55)
        self.write_data(0)
        self.write_data(7)
        self.write_data(2)
        self.write_data(16)
        self.write_command(225)
        self.write_data(15)
        self.write_data(27)
        self.write_data(15)
        self.write_data(23)
        self.write_data(51)
        self.write_data(44)
        self.write_data(41)
        self.write_data(46)
        self.write_data(48)
        self.write_data(48)
        self.write_data(57)
        self.write_data(63)
        self.write_data(0)
        self.write_data(7)
        self.write_data(3)
        self.write_data(16)
        self.write_command(42)
        self.write_data(0)
        self.write_data(0)
        self.write_data(0)
        self.write_data(127)
        self.write_command(43)
        self.write_data(0)
        self.write_data(0)
        self.write_data(0)
        self.write_data(159)
        self.write_command(240)
        self.write_data(1)
        self.write_command(246)
        self.write_data(0)
        self.write_command(58)
        self.write_data(5)
        self.write_command(41)


    def _set_addr_window(x0, y0, x1, y1):
        self.write_command(CASET)
        self.write_data(0)
        self.write_data(x0 + 2)
        self.write_data(0)
        self.write_data(x1 + 2)
        self.write_command(RASET)
        self.write_data(0)
        self.write_data(y0 + 1)
        self.write_data(0)
        self.write_data(y1 + 1)


    def dsp_single_colour(self, DH, DL):
        self.write_command(44)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.LCD_DataWrite(DH, DL)


    def fill_display(self, r, g, b):
        self.write_command(44)
        for i in range(160):
            for j in range(128):
                self.send_pixel((r, g, b))


    def send_pixel(self, color):
        COLORS = dict()
        if color not in COLORS:
            COLORS[color] = (color[0] & 248 | color[1] >> 5, (color[1] & 7) << 5 | color[2] >> 3)

        digitalWrite(self.cs, False)
        digitalWrite(self.rs, True)
        shiftOut(self.sda, self.scl, MSBFIRST, COLORS[color][1])
        shiftOut(self.sda, self.scl, MSBFIRST, COLORS[color][0])
        digitalWrite(self.cs, True)


    def send_picture(self, image):
        image = image.convert("RGB")
        self.write_command(44)
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                self.send_pixel(image.getpixel((x, y)))
    
    def send_image(self, file):
	from PIL import Image
	self.send_picture(Image.open(file))


if __name__ == '__main__':
    lcd = LCD()
    lcd.write_command(44)
    from PIL import Image
    while True:
        lcd.fill_display(255, 0, 0)
        lcd.sleep(50)
        lcd.fill_display(0, 255, 0)
        lcd.send_picture(Image.open("success.bmp"))
