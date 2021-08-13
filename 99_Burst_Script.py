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
            #Add the below line after image%02d and self.frame_num respectively to add millisecond time stamp to frame
            #_%05d
            #,round((time.time()-start)*1000)
            self.output = io.open(('99_Burst_Script/T_01/image%02d.jpg') %( self.frame_num), 'wb')
        self.output.write(buf)

with picamera.PiCamera(resolution=(2040,2040), framerate_range=(5,10)) as camera:
    #Setting up consistent images
    #AWB_mode
    #When queried, the awb_mode property returns a string representing the auto white balance setting of the camera. The possible values can be obtained from the PiCamera.AWB_MODES attribute, and are as follows:
    #
    # 'off'
    # 'auto'
    # 'sunlight'
    # 'cloudy'
    # 'shade'
    # 'tungsten'
    # 'fluorescent'
    # 'incandescent'
    # 'flash'
    # 'horizon'
    # When set, the property adjusts the camera’s auto-white-balance mode.
    # The property can be set while recordings or previews are in progress. The default value is 'auto'.
    # Check which exposure mode is needed in the setting first and apply that here.
    print('awbmode:',camera.awb_mode)
    camera.awb_mode = ('sunlight')

    #AWB gains
    #When set, this attribute adjusts the camera’s auto-white-balance gains. The property can be specified as a single value in which case both red and blue gains will be adjusted equally, or as a (red, blue) tuple. Values can be specified as an int, float or Fraction and each gain must be between 0.0 and 8.0. Typical values for the gains are between 0.9 and 1.9. The property can be set while recordings or previews are in progress.
    print('awbgain:',camera.awb_gains)
    camera.awb_gains=(1.7,1.7)

    # brightness
    # Retrieves or sets the brightness setting of the camera.
    # When queried, the brightness property returns the brightness level of the camera as an integer between 0 and 100. When set, the property adjusts the brightness of the camera. Brightness can be adjusted while previews or recordings are in progress. The default value is 50.
    print('brightness:',camera.brightness)
    camera.brightness=50

    #exposure_mode
    # Retrieves or sets the exposure mode of the camera.
    # When queried, the exposure_mode property returns a string representing the exposure setting of the camera. The possible values can be obtained from the PiCamera.EXPOSURE_MODES attribute, and are as follows:
    #'off'
    # 'auto'
    # 'night'
    # 'nightpreview'
    # 'backlight'
    # 'spotlight'
    # 'sports'
    # 'snow'
    # 'beach'
    # 'verylong'
    # 'fixedfps'
    # 'antishake'
    # 'fireworks'
    # When set, the property adjusts the camera’s exposure mode. The property can be set while recordings or previews are in progress. The default value is 'auto'.
    print('exposuremode:',camera.exposure_mode)
    camera.exposure_mode

    #color_effects
    # Retrieves or sets the current color effect applied by the camera.
    # When queried, the color_effects property either returns None which indicates that the camera is using normal color settings, or a (u, v) tuple where u and v are integer values between 0 and 255.
    # When set, the property changes the color effect applied by the camera. The property can be set while recordings or previews are in progress. For example, to make the image black and white set the value to (128, 128). The default value is None.
    print('color_effects:',camera.color_effects)
    #camera.color_effects = (0,0)

    #Shutter speed or exposure speed only read
    print('exposure speed:', camera.exposure_speed)

    #Flash settings
    #When queried, the flash_mode property returns a string representing the flash setting of the camera. The possible values can be obtained from the PiCamera.FLASH_MODES attribute, and are as follows:
    # 'off'
    # 'auto'
    # 'on'
    # 'redeye'
    # 'fillin'
    # 'torch'
    # When set, the property adjusts the camera’s flash mode. The property can be set while recordings or previews are in progress. The default value is 'off'.
    print('flash mode:',camera.flash_mode)
    camera.flash_mode='torch'

    #image denoise
    #ideally this should not be available, ie should be false
    print('image_denoise:', camera.image_denoise)
    camera.image_denoise = 'false'

    #image effect 
    #do not apply any image effect or any of the parameters
    #https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera.PiCamera.image_effect
    print('image effect',camera.image_effect)
    camera.image_effect = 'none'

    #ISO
    #Very important parameter the lower the better
    print('ISO:',camera.ISO)
    camera.iso = 100
    print('ISO(set):',camera.ISO)

    #Metering mode
    # For how to calculate gains and exposure
    # https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera.PiCamera.image_effect
    #I believe it should be spot or backlit mode
    print("Metering mode:", camera.meter_mode)
    camera.meter_mode = 'spot'
    print("Metering mode(set to):", camera.meter_mode)

    #saturation
    #For color saturation settings
    #https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera.PiCamera.saturation
    print('saturation', camera.saturation)
    camera.saturation = 0

    #sharpness
    #For sharpness of the image
    print('sharpness:',camera.sharpness)
    camera.sharpness = -25

    #For shutter speed
    #https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera.PiCamera.shutter_speed
    #Shutter speed is given in microseconds, try to keep it as low as possible.
    print('shutter speed:',camera.shutter_speed)
    camera.shutter_speed = 38000
    print('Shutter speed now:',camera.shutter_speed)


    #setting up the preview
    camera.start_preview()
    camera.preview.fullscreen = False
    camera.preview.window =(0,0,640,480)

    #Annotation time
    start = time.time()*1000    # starting a counter to begin the timer.
    print(start)

    #Annotating the program
    camera.annotate_text_size = 12
    camera.annotate_background = picamera.Color('black')
    print(round(time.time()*1000 - start,3))

    camera.annotate_text = '%4d milliseconds' % round((time.time()*1000-start),3)

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