from picamera import PiCamera
import time
from gpiozero import Button

button = Button(17)
camera = PiCamera()
camera.resolution = (1280, 720)
#camera.vflip = True
#camera.contrast = 10
#camera.image_effect = "watercolor"
time.sleep(2)
camera.start_preview()
frame = 1
print('code working')
while True:
    try:
        button.wait_for_press()
        camera.capture(f"/home/pi/Documents/Engineering_4_Notebook/pastafile/{frame}.jpg") 
        print('working..')
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break
