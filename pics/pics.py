import time
import picamera

effect_array = ['watercolor', 'blur', 'washedout', 'cartoon', 'hatch']
i = 0; 
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    print('running')
    #camera.image_effect = 'colorswap'
    # Camera warm-up time
    time.sleep(2)
    for x in range(5):
        camera.image_effect = effect_array[i]
        camera.capture('foo.jpg')
        print('done!')
        i+=1
        time.sleep(0.1)

