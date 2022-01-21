import time
import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont




# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

lsm303 = Adafruit_LSM303.LSM303()
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)


# Initialize library.
disp.begin()
# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
shape_width = 20
padding = 2
bottom = height-padding

# Load default font.
font = ImageFont.load_default()

while True:
    accel, mag = lsm303.read()
    mag_x, mag_y, mag_z = mag
    accel_x, accel_y, accel_z = accel
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((5, 2), f" X: {round(accel_x/102.34)} ",  font=font, fill=55)
    draw.text((5, 22), f" Y: {round(accel_y/102.34)}", font=font, fill=55)
    draw.text((5, 22), f" Z: {round(accel_z/102.34)}", font=font, fill=55)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Display image.
    disp.image(image)
    disp.display()
    # Wait half a second and repeat.
    time.sleep(000.5)


disp.image(image)
disp.display()
