#--------------------------------------------------------------
# ECE 4600 Capstone - Winter 2019
# Wayne State University
# Project: Rubik's Cube Solving Robot
# Primary author: Joseph Breitner
# Additional team members: Michael Ulicny, Joseph VanBuhler
#
# This class is the user-interface. It is intended to call 
# our other functions and classes to allow easy interaction 
# between user and robot. 
# 
# A simple command line interface is utilized to control the
# robot. The following commands are available:
#   <1>: Opens the claws to allow user to insert cube 
#   <2>: Closes the claws to load in the cube
#   <3>: "Captures" the cube and creates digital representation
#   <4>: Generates the algorithm and move list required to solve
#   <5>: Executes the move list to solve the cube
#   <6>: Generates a random configuration and randomizes cube
#   <7>: Quits the session and ends the program
#--------------------------------------------------------------

from frame import Frame
from algocfop import AlgoCFOP
from cube import Cube
from face import Face
from image import Image
import time
import numpy as np

# Session class
class Session:

    def __init__(self):
    # Initialize Frame, Cube, and Algorithm
        self.frame = Frame(clawDelay=0.5, rotateDelay90=0.5)
        self.cube = None
        self.algo = None

    def printOptions(self):
    # Prints options for user-interface
        print('Press <1> to open the claws')
        print('Press <2> to close the claws')
        print('Press <3> to capture cube')
        print('Press <4> to generate algorithm')
        print('Press <5> to solve the cube')
        print('Press <6> to randomize cube')
        print('Press <7> to exit session')
        print('\n')
    
    def prompt(self):
    # Prompts user for input
        
        option = input('Please select an option from the list above and hit enter: ')

        # <1> : open the claws
        if option == '1':
            self.frame.openClaws()
            print('Claws opened\n')
            return True
        
        # <2> : close the claws
        elif option == '2':
            self.frame.closeClaws()
            print('Claws closed\n')
            return True

        # <3> : map the cube
        elif option == '3':
            images = self.frame.mapCube()   # list of image arrays of each face 
            self.makeCube(images)           # creates software representation
            print('Your cube...')
            print(self.cube)
            return True
        
        # <4> : generate the algorithm
        elif option == '4':
            
            # if there is no cube data in this session yet
            if self.cube == None:
                print('No cube')
                return True     # exit and re-prompt

            # call algorithm 
            self.algo = AlgoCFOP(self.cube) # pass the cube 
            self.algo.solve()               # solve the cube
            length = len(self.algo.movelist)    # return length of move list
            print('Algorithm generated with ', length, ' moves')    # display length of move list
            print('\nThe move list: ')
            self.algo.printList()
            return True
        
        # <5> : begins solving the physical cube
        elif option == '5':

            # if there is no cube data in this session yet
            if self.cube == None:
                print('No cube')
                return True     # exit and re-prompt

            # Ask for single step
            tempStep = input('Single-step through solution? (n/y): ')
            if tempStep == 'n' or tempStep == 'N':
                singleStep = False
            elif tempStep == 'y' or tempStep == 'Y':
                singleStep = True

            # pass move list to list parser
            self.solveCube(singleStep)
            print('Cube solved')
            print(self.algo.cube, '\n')
            return True

        # <6> : generate random config and execute moves
        elif option == '6':

            # if there is no cube data in this session yet
            if self.cube == None:
                print('No cube')
                return True     # exit and re-prompt
            
            # call algorithm to generate random configuration
            self.algo = AlgoCFOP(self.cube)
            self.algo.randomize()       # random move list generator
            self.solveCube(self.algo.movelist)  # execute moves on physical cube
            print('Cube randomized')
            return True

        # <7> : end session
        elif option == '7':
            print('Session ended')
            return False
        
        # other inputs
        else:
            print('ERROR: Invalid entry')
            return True

    def makeCube(self, images):
    # calls necessary functions to create software representaion of the cube
    # handles errors by allowing user to verify camera capture and manually
    # configuration if there are any errors in the mapping of the cube

        inputOK = False
        retry = False
        while inputOK == False: 
            if retry == True:  

                # Input current cube state
                print('Please enter the cube configuration for each side as prompted.')
                upColors =      input('    Up layer colors:    ')
                frontColors =   input('    Front layer colors: ')
                downColors =    input('    Down layer colors:  ')
                rightColors =   input('    Right layer colors: ')
                backColors =    input('    Back layer colors:  ')
                leftColors =    input('    Left layer colors:  ')
                colorSides = [upColors, frontColors, downColors, rightColors, backColors, leftColors]

                # Create numpy arrays
                up = np.empty([3,3], dtype=np.str)
                front = np.empty([3,3], dtype=np.str)
                down = np.empty([3,3], dtype=np.str)
                right = np.empty([3,3], dtype=np.str)
                back = np.empty([3,3], dtype=np.str)
                left = np.empty([3,3], dtype=np.str)

                # create list of Faces
                faces = [up, front, down, right, back, left]

                # Fill numpy arrays
                for i in range(6):
                    for j in range(3):
                        for k in range(3):
                            faces[i][j][k] = colorSides[i][3*j + k]
		
                # Instantiate faces
                up = Face(up)
                down = Face(down)
                front = Face(front)
                back = Face(back)
                left = Face(left)
                right = Face(right)

                # Instantiate cube
                self.cube = Cube(up, down, front, back, left, right)
            
            elif retry == False:

                # Create faces and rotate to proper orientation
                front = self.makeFace(images[0])
                back = self.makeFace(images[1])
                right = np.rot90(self.makeFace(images[2]),1)
                left = np.rot90(self.makeFace(images[3]),3)
                down = self.makeFace(images[4])
                up = self.makeFace(images[5])
                
                # create list of color arrays
                colorArrays = [up,front,down,right,back,left]

                # instantiate faces
                frontFace = Face(front)
                backFace = Face(back)
                rightFace = Face(right)
                leftFace = Face(left)
                downFace = Face(down)
                upFace = Face(up)
        
                # instnatiate cube
                self.cube = Cube(upFace, downFace, frontFace, backFace, leftFace, rightFace)
        
            # Print cube for inspection
            print('\nCube configuration as entered:\n')
            print(self.cube)
    
            # Print text-copyable list of configurations
            print('\nCurrent cube configuration as text inputs:')
            textColors = ''
            for face in colorArrays:
                for color in face:
                    textColors += str(color)
                textColors += '\n'
            textColors = ''.join(x for x in textColors if (
                x.isalpha() or x == '\n'))
            print(textColors)
    
            # Prompt for correction
            failcol = {'r':'red', 'o':'orange', 'y':'yellow',
                'g':'green', 'b':'blue', 'w':'white'}

            # if the checksum fails, prompt for correction
            if self.cube.checkSumGood == False:
                print('Too many ' + failcol[self.cube.failedColor] + 's! ' + 
                'Impossible cube configuration.')
                inputOK = False
                retry = True
                
            # if the checksum is correct    
            elif self.cube.checkSumGood == True:
                print('Checksum passes; there are nine of each color.')
                status = input('Is this cube correct? (Y/N): ')
                if status == 'n' or status == 'N':
                    inputOK = False
                    retry = True
                    print('')
                else:
                    inputOK = True

            return self.cube

    # Function to solve the cube with the claws
    def solveCube(self, singleStep = True):
        
        # Alias for simplifying code
        movelist = self.algo.movelist
        
		# Flag to indicate whether current iteration is an inverse one
        isInverse = False
        
		# Runtime indicator flag
        goodToGo = True
        
		# Initial range parameter
        liststart = 0
        tempindex = 0
        
		# Sets of moves
        turns = 'F B U D R L'
        iturns = 'Fi Bi Ui Di Ri Li'
        dturns = '2F 2B 2U 2D 2R 2L'
        rots = 'X Z'
        irots = 'Xi Yi Zi'
        drots = '2X 2Y 2Z'
        
		# Entering main loop of claw solving
        while goodToGo == True:
            try:
                for i in range(liststart, len(movelist)):
                    tempindex = i

					# Print move number and move
                    if not isInverse:
                        print('Move ' + str(i) + ': ' + str(movelist[i]))	
                    else:
                        print('Move ' + str(len(movelist) - i - 1) + ': ' 
							+ str(movelist[i]))
                    
					# Parse list
                    if movelist[i] in turns:
                        self.frame.turn90(movelist[i])
                    elif movelist[i] in iturns:
                        self.frame.turn90(movelist[i][0], inverse=True)
                    elif movelist[i] in dturns:
                        self.frame.turn180(movelist[i][1])
                    elif movelist[i] in rots:
                        self.frame.rotate90(movelist[i])
                    elif movelist[i] in irots:
                        self.frame.rotate90(movelist[i][0], inverse=True)
                    elif movelist[i] in drots:
                        self.frame.rotate180(movelist[i][1])					
                    
					# Loop terminator statement
                    if tempindex == (len(movelist) - 1):
                        goodToGo = False
                    
					# If single stepping
                    if singleStep:
                        input('')
                    
			# On a CTRL+C press:
            except KeyboardInterrupt:
                goodToGo = False
                print('-----------\nUSER PAUSE\n-----------')
                print('Type 0 - 20 and press Enter to repeat last n moves.')
                print('Press "i" to proceed backwards through the list')
                print('Press "s" to enable single-step through the solution.')
                print('(Pressing Enter will proceed to the next step)')
                print('Press "m" to exit single-stepping mode')
                extCommand = input('Option: ')
                if extCommand in '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20':
                    goodToGo = True
					# Set new list start to next movelist
                    liststart = tempindex - int(extCommand) + 1
                elif extCommand == 'i':
                    isInverse = not isInverse
                    templist = self.algo.inverseList()
                    movelist = templist
                    goodToGo = True
					# Set new list start to next movelist
                    liststart = len(movelist) - (tempindex + 1)
                elif extCommand == 's':
                    singleStep = True
                    liststart = tempindex + 1
                    goodToGo = True
                elif extCommand == 'm':
                    singleStep = False
                    liststart = tempindex + 1
                    goodToGo = True
                print('-----------\nUSER RESUME\n-----------')      
    
    def getSample(self, img, x, y):
    # function to pick a sample from the image array
    # accepts the image array and the X, Y location
        return img[y,x,:]
      

    def findColor(self, rgb):
    # determines color of a given RGB sample by calculating the 
    # Euclidian distance from a set of Rubik's Cube RGB colors.
    #   Eucldian distnace formula:
    #       d = sqrt((r1-r2)^2 + (g1-g2)^2 (b1-b2)^2)
    # The smallest distance corresponds to the color which the sample
    # is closest to. The function then returns the color as a character:
    #   'w' for white
    #   'y' for yellow
    #   'r' for red
    #   'o' for orange
    #   'g' for green
    #   'b' for blue

        # Rubik's Cube Colors
        w=np.array([255,255,255])
        y=np.array([255,128,0])
        r=np.array([255,0,0])
        o=np.array([255,255,0])
        g=np.array([0,128,0])
        b=np.array([0,0,128])

        # create list of colors
        colors = [w, y, r, o, g, b]

        # create list of distances
        dist = np.empty((6), dtype=np.float) 

        # calculate Euclidian distance
        i = 0
        for col in colors:
            dist[i] = (np.sqrt(((rgb[0]-col[0])**2) + ((rgb[1]-col[1])**2) + ((rgb[2]-col[2])**2)))
            i+=1

        # determine character output and return
        out = np.argmin(dist)
        clrs = ['w', 'y', 'r', 'o', 'g', 'b']
        return clrs[out]

    def makeFace(self, img):
    # make face array 
        
        # initialize numpy array
        colorArray=np.empty((3,3),dtype=str)
        
        # initialize functions
        findColor = self.findColor
        getSample = self.getSample

        # hard-coded pixel locations 
        x = 55
        y = 50
        d = 75

        # Create color arrays:
        colorArray[0,0] = findColor(getSample(img,x,y))
        colorArray[0,1] = findColor(getSample(img,x+d,y))
        colorArray[0,2] = findColor(getSample(img,x+2*d,y))
        colorArray[1,0] = findColor(getSample(img,x,y+d))
        colorArray[1,1] = findColor(getSample(img,x+d,y+d))
        colorArray[1,2] = findColor(getSample(img,x+2*d,y+d))
        colorArray[2,0] = findColor(getSample(img,x,y+2+d))
        colorArray[2,1] = findColor(getSample(img,x+d,y+2*d))
        colorArray[2,2] = findColor(getSample(img,x+2*d,y+2*d))
        
        return colorArray

        
                
