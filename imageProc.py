# Image Capture and Processing
# -----------------------------
# February 18, 2019

import picamera
import picamera.array
import numpy as np
import matplotlib.pyplot as plt
import time
from cube import Cube
from face import Face

def takePic():
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as output:
            res = 128
            #camera.awb_mode = 'incandescent'
            #camera.exposure_mode = 'verylong'
            #camera.image_effect = 'colorpoint'
            camera.resolution = (res, res)
            camera.start_preview()
            time.sleep(2)
            output = np.empty((res, res, 3), dtype=np.uint8)
            camera.capture(output, 'rgb')
    return output

def findColor(RGB):
    
    w = np.array([175, 178, 176])
    y = np.array([157, 176, 88 ])
    r = np.array([152, 58 , 64 ])
    o = np.array([178, 113, 85 ])
    g = np.array([26 , 143, 89 ])
    b = np.array([36 , 76 , 127])
    
    colors =[w, y, r, o, g, b]
    dist = np.empty((6), dtype=np.float)
    i = 0
    for col in colors:
        dist[i] = (np.sqrt((RGB[0]-col[0])**2 + 
            (RGB[1]-col[1])**2 + (RGB[2]-col[2])**2))
        i+=1
        
    out = np.argmin(dist)
    clrs = ['w', 'y', 'r', 'o', 'g', 'b']
    
    return clrs [out]       

def makeFace():

    colorArray = np.empty((3, 3), dtype=str)
    img = takePic()
    X = 20
    Y = 24
    d = 40
    
    # (Y, X, [R G B])
    
    # First Row
    colorArray[0,0] = findColor(img[Y,X,:])
    colorArray[0,1] = findColor(img[Y,X+d,:])
    colorArray[0,2] = findColor(img[Y,X+2*d,:])
    
    # Second Row
    colorArray[1,0] = findColor(img[Y+d,X,:])
    colorArray[1,1] = findColor(img[Y+d,X+d,:])
    colorArray[1,2] = findColor(img[Y+d,X+2*d,:])
    
    # Third Row
    colorArray[2,0] = findColor(img[Y+2*d,X,:])
    colorArray[2,1] = findColor(img[Y+2*d,X+d,:])
    colorArray[2,2] = findColor(img[Y+2*d,X+2*d,:])
    
    return colorArray

input('Press enter to capture Upper Face...')
upperFace = makeFace()
up = Face(upperFace)
print('\nUpper Face\n')
print(upperFace)
print('\n')

input('Press enter to capture Front Face...')
frontFace = makeFace()
front = Face(frontFace)
print('\nFront Face\n')
print(frontFace)
print('\n')

input('Press enter to capture Left Face...')
leftFace = makeFace()
leftFace = np.rot90(leftFace,3)
left = Face(leftFace)
print('\nLeft Face\n')
print(leftFace)
print('\n')
input('Press enter...')

downFace = makeFace()
downFace = np.rot90(downFace,3)
down = Face(downFace)
print('\nDown Face\n')
print(downFace)
print('\n')

input('Press enter to capture Back Face...')
backFace = makeFace()
backFace = np.rot90(backFace,1)
back = Face(backFace)
print('\nBack Face\n')
print(backFace)
print('\n')

input('Press enter to capture Right Face...')
rightFace = makeFace()
right = Face(rightFace)
print('\nRight Face\n')
print(rightFace)
print('\n')

input('Press enter to print The Cube...')
theCube = Cube(up,down,front,back,left,right)
print('\nThe Cube\n')
print(theCube)
print('\n')
input('Press enter to exit...')
