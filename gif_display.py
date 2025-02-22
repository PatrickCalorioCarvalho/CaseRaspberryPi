
import sys
import time
from PIL import Image
import st7735


image_file = "/home/patrick/actions-runner/_work/CaseRaspberryPi/CaseRaspberryPi/background.gif"


disp = st7735.ST7735(port=0, cs=0, dc=24, backlight=None, rst=25, width=80, height=160, rotation=90,spi_speed_hz=4000000)

disp.begin()
width = disp.width
height = disp.height

image = Image.open(image_file)
frame = 0

while True:
    try:
        image.seek(frame)
        disp.display(image.resize((width, height)))
        frame += 1
        time.sleep(0.01)

    except EOFError:
        frame = 0
