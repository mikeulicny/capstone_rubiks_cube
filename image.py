# Image Capture and Processing Class

import time
import numpy as np
import picamera
import picamera.array
from face import Face

class Image:

    '''
    The image (capture and processing) class
    This class includes the following funcionalities:
        - capturing an image with the Raspberry Pi Camera Module
        - determining the color of a specific location in an image
        - parsing an image into an array of colors (representing the Face)
        - interfacing with camera to adjust settings/effects (wb,aperature,exposure)
    '''

    def __init__(self, img=np.empty(128,128,3)):
        self.img = img
        
    def capture(self, res=128, delay=1, awb='', expsr='', eff=''):
        with picamera.PiCamera() as camera:
            with picamera.array.PiRGBArray(camera) as self.img:
                
                time.sleep(delay)
                camera.resolution = res
                camera.awb_mode = awb
                camera.exposure_mode = expsr
                camera.image_effect = eff

                camera.capture(self.img,'rgb')
        
        return self.img

    def getSample(self, x, y, average=False):
        
        img = self.img

        if average == False:
            return img[y,x,:]
        
        elif average == True:
            ctr = img[y,x,:]
            top = img[y+5,x,:]
            btm = img[y-5,x,:]
            lft = img[y,x-5,:]
            rht = img[y,x+5,:]

            samples = [ctr, top, btm, lft, rht]

            sums = np.empty(3)

            for i in sums:
                for col in samples:    
                    sums[i] = col[0] + col[1] + col[2] + col[3] + col[4]

            avgRed = sums[0] / 5
            avgGreen = sums[1] / 5
            avgBlue = sums[2] / 5

            avg = [avgRed, avgGreen, avgBlue]

            return avg

        else:
            return None            

    def findColor(self, rgb):
        
        w = np.array([175, 178, 176])
        y = np.array([157, 176, 88 ])
        r = np.array([152, 58 , 64 ])
        o = np.array([178, 113, 85 ])
        g = np.array([26 , 143, 89 ])
        b = np.array([36 , 76 , 127])

        colors = [w, y, r, o, g, b]
        dist = np.empty((6), dtype=np.float) 

        i = 0
        for col in colors:
            dist[i] = (np.sqrt((rgb[0]-col[0])**2 + 
                (rgb[1]-col[1])**2 + rgb[2]-col[2]**2))
            i+=1

        out = np.argmin(dist)
        clrs = ['w', 'y', 'r', 'o', 'g', 'b']

        return clrs[out]

    def makeFace(self, faceOpt, colorArray=np.empty((3,3),dtype=str)):
        
        findColor = self.findColor
        getSample = self.getSample

        x = 30
        y = 30
        d = 30

        if faceOpt == 'A':
            colorArray[0,0] = findColor(getSample(x,y))
            colorArray[0,1] = findColor(getSample(x+d,y))
            colorArray[0,2] = findColor(getSample(x+2*d,y))
            colorArray[1,1] = findColor(getSample(x+d,y+d))
            colorArray[2,0] = findColor(getSample(x,y+2+d))
            colorArray[2,1] = findColor(getSample(x+d,y+2*d))
            colorArray[2,2] = findColor(getSample(x+2*d,y+2*d))
            return colorArray

        elif faceOpt == 'B':
            colorArray[1,0] = findColor(getSample(x,y+d))
            colorArray[1,2] = findColor(getSample(x+2*d,y+d)) 
            f = Face(colorArray)
            return f
