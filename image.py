#--------------------------------------------------------------
# ECE 4600 Capstone - Winter 2019
# Wayne State University
# Project: Rubik's Cube Solving Robot
# Primary author: Joseph Breitner
# Additional team members: Michael Ulicny, Joseph VanBuhler
#
# Image capture class: 
# includes and calls functions to capture images 
#--------------------------------------------------------------

import time
import numpy as np
import picamera
import picamera.array
from face import Face

class Image:
# image class

    def __init__(self):
        pass
        
    def capture(self, res=256, delay=0.5):
    # captures image default size 256x256

        with picamera.PiCamera() as camera:
            with picamera.array.PiRGBArray(camera) as self.img:
                # delay for camera to warm up and focus (default = 0.5s)
                time.sleep(delay)
                camera.resolution = (res, res)

                # initialize numpy array
                self.img = np.empty((res,res,3), dtype=np.uint8)

                # capture image as RGB array
                camera.capture(self.img,'rgb')
        
        return self.img
