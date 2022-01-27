import time
import picamera

effect_array = ['watercolor', 'blur', 'washedout', 'cartoon', 'hatch']
pic_array = ['v.jpg', 'v2.jpg', 'v3.jpg' ,'v4.jpg' ,'v5.jpg']
x= 1;
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
        camera.capture(pic_array[x])
        print('done!')
        i+=1
        x+=1
        time.sleep(0.1)

