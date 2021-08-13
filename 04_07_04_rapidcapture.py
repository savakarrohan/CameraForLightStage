import io
import time
import picamera
import datetime as dt

class SplitFrames(object):
    def __init__(self):
        self.frame_num = 0
        self.output = None

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # Start of new frame; close the old one (if any) and
            # open a new output
            if self.output:
                self.output.close()
            self.frame_num += 1
            self.output = io.open('images_04_07_04/image%02d.jpg' % self.frame_num, 'wb')
        self.output.write(buf)

with picamera.PiCamera(resolution=(2040,2040), framerate=30) as camera:
    #setting up the preview
    camera.start_preview()
    camera.preview.fullscreen = False
    camera.preview.window =(0,0,640,480)

    #Annotating the program
    camera.annotate_background = picamera.Color('black')
    camera.annotate_text = 'Its Working'

    #Annotation time
    start = dt.datetime.now()
    # Give the camera some warm-up time
    time.sleep(2)
    output = SplitFrames()
    start = time.time()
    camera.start_recording(output, format='mjpeg')
    camera.wait_recording(3)
    camera.stop_recording()
    finish = time.time()

#Print the FPS of the capture
print('Captured %d frames at %.2ffps' % (
    output.frame_num,
    output.frame_num / (finish - start)))

#In order to prevent a crash of the program, unnecessary but just a safety measure
camera.stop_preview()