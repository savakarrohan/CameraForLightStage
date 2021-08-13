import picamera
import datetime as dt

camera = picamera.PiCamera(resolution=(1280, 720), framerate=60)
camera.start_preview(window = (100,100,400,300))
camera.annotate_background = picamera.Color('black')
camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
camera.start_recording('video_03/timestamped.h264')
start = dt.datetime.now()
while (dt.datetime.now() - start).seconds < 30:
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.wait_recording(0.8)
camera.stop_recording()
camera.stop_preview()