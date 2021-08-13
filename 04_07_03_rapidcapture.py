import time
import picamera

frames = 8

def filenames():
    frame = 0
    while frame < frames:
        yield 'images_03/image%02d.jpg' % frame
        frame += 1

with picamera.PiCamera(resolution= (2040,2040)) as camera:
    camera.start_preview()
    camera.preview.fullscreen = False
    camera.preview.window=(0,0,640,480)
    # Give the camera some warm-up time
    time.sleep(2)
    start = time.time()
    camera.capture_sequence(filenames(), use_video_port=True)
    finish = time.time()
print('Captured %d frames at %.2ffps' % (
    frames,
    frames / (finish - start)))