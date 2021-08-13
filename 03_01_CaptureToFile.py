from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (2048, 1080)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('02_Aug_PiB/PiB_08_02.jpg')