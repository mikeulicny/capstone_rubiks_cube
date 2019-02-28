# Image Capture and Processing

import picamera
import picamera.array
import numpy as np
import time
from cube import Cube
from face import Face

def takePic():
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as output:
 
			# Camera options for white balance, exposure, aperature, etc.
            # camera.awb_mode = ''
            # camera.exposure_mode = ''
            # camera.image_effect = ''
            
			res = 128											# resolution to 128 
			camera.resolution = (res, res)						# 128x128 pixel image
            
			# camera.start_preview()							# preview camera to set up photo
            time.sleep(1)										# sleep to let camera start up / see preview
            
			# Initialize output
			output = np.empty((res, res, 3), dtype=np.uint8)	# make empty 128x128 array
            camera.capture(output, 'rgb')						# capture picture to array as RGB image
    
	return output

def findColor(RGB):
    # This function determines the color of a given pixel by comparing it's RGB values
	# to the RGB values sampled from a standard Rubik's Cube. Comparison is done by 
	# utilizing the Euclidian Distance Formula: d = sqrt((R2-R1)^2 +(G2-G1)^2 + (G2-G1)^2)
	# R1, G1, and B1 represent the RGB values of the pixel passed into the function
	# while R2, G2, and B2 represent the RGB values of the sampled color of the cube.
	# The function returns a character value of either 'w', 'y', 'r', 'o', 'g', or 'b', 
	# corresponding to the six colors found on a Rubik's Cube.
	
	# RGB values of sampled colors from Rubik's Cube
    w = np.array([175, 178, 176])
    y = np.array([157, 176, 88 ])
    r = np.array([152, 58 , 64 ])
    o = np.array([178, 113, 85 ])
    g = np.array([26 , 143, 89 ])
    b = np.array([36 , 76 , 127])
    
    colors =[w, y, r, o, g, b]  			# array of RGB values to iterate through
    dist = np.empty((6), dtype=np.float) 	# create empty array to store distance values
    
	i = 0									# initialize counter to 0
    
	# FOR loop to calculate distance btwn each RGB value
	for col in colors:
        dist[i] = (np.sqrt((RGB[0]-col[0])**2 + 
            (RGB[1]-col[1])**2 + (RGB[2]-col[2])**2))
        i+=1
        
    out = np.argmin(dist)					# finds location of min distance in array of distances
    clrs = ['w', 'y', 'r', 'o', 'g', 'b']	# character array of color outputs
    
    return clrs [out]						# outputs character of the color determined     

def makeArray():
	# This function creates a 3x3 Numpy array that represents a face of the cube.
	# The fnctions returns an array with character values that represent 
	# the color of the cubelets in colorArray 
	
    colorArray = np.empty((3, 3), dtype=str)	# create empty 3x3 Numpy array
    img = takePic()								# call function to take picture 
    
	# Coordinates of the top left cubelet and the distance 

	X = 20	# X start value
    Y = 24	# Y start value
    d = 40	# distance to next sample point
		
	# (X, Y)		(X+d, Y)		(X+2*d, Y)
	# (X, Y+d)	    (X+d, Y+d)		(X+2*d, Y+d)
	# (X, Y+2*d)	(X+d, Y+2*d)	(X+2*d, Y+2*d)
    
    # Function calls for each cubelet
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
