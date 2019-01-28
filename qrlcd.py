import lcd
from PIL import Image, ImageDraw, ImageFont
import qrcode

class QRLCD(lcd.LCD):

    def __init__(self):

        self.font = "arialbd.ttf"
        self.fontsize = 16

        lcd.LCD.__init__(self)


    def send(self, data, text):
	self.sleep(50)

        qr = qrcode.QRCode(
            version=4,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=1,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((self.size[0], self.size[0]), Image.NEAREST)

        img2 = Image.new(img.mode, self.size, 255)
        img2.paste(img, (0, 0, self.size[0], self.size[0]))

        draw = ImageDraw.Draw(img2)
        f = ImageFont.truetype(self.font, self.fontsize)

        draw.text((10, self.size[0] + 6), text, fill=0, font=f)

        self.write_command(44)
        self.send_picture(img2)



if __name__ == '__main__':
    qrlcd = QRLCD()
    qrlcd.send('msEG4yPUHyDC9zAjTxHqT8wtzAcG6UUAHt', '0.1 BTC')
