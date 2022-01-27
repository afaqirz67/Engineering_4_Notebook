from picamera import PiCamera
import time
camera = PiCamera()
camera.resolution = (1280, 720)
#camera.vflip = True
#camera.contrast = 10
#camera.image_effect = "watercolor"
time.sleep(2)
camera.start_preview()
frame = 1
while True:
    try:
	button.wait_for_press()
	camera.capture("/home/pi/Documents/Engineering_4_Notebook/copypasta.py/img.jpg") 
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break
