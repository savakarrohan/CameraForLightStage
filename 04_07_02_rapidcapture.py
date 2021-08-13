import time
import picamera

frames = 60

with picamera.PiCamera() as camera:
    camera.resolution = (3840,2160)
    #camera.framerate = 5
    camera.start_preview(window = (100,100,400,300))
    # Give the camera some warm-up time
    time.sleep(2)
    start = time.time()
    camera.capture_sequence([
        'image%02d.jpg' % i
        for i in range(frames)
        ], use_video_port=True)
    finish = time.time()
print('Captured %d frames at %.2ffps' % (
    frames,
    frames / (finish - start)))