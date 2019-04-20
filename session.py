from frame import Frame
from algocfop import AlgoCFOP
from cube import Cube
from face import Face
from image import Image
import time
import numpy as np
import matplotlib.pyplot as plt

class Session:

    def __init__(self):
        self.frame = Frame(clawDelay=0.3, rotateDelay90=0.5)
        self.cube = None
        self.algo = None

    def printOptions(self):
        print('Press <1> to open the claws')
        print('Press <2> to close the claws')
        print('Press <3> to capture cube')
        print('Press <4> to generate algorithm')
        print('Press <5> to solve the cube')
        print('Press <6> to randomize cube')
        print('Press <7> to Auto-Solve')
        print('Press <8> to exit session')
        print('\n')
    
    def prompt(self):
        
        option = input('Please select an option from the list above and hit enter: ')

        if option == '1':
            self.frame.openClaws()
            return True
        
        elif option == '2':
            self.frame.closeClaws()
            return True

        elif option == '3':
            images = self.frame.mapCube()
            self.makeCube(images)
            
            #~ self.cube = self.makeCube()
            #~ plt.imshow(images[0])
            #~ plt.show()
            #~ plt.close()
            #~ plt.imshow(images[1])
            #~ plt.show()
            #~ plt.close()
            #~ plt.imshow(images[2])
            #~ plt.show()
            #~ plt.close()
            #~ plt.imshow(images[3])
            #~ plt.show()
            #~ plt.close()
            #~ plt.imshow(images[4])
            #~ plt.show()
            #~ plt.close()
            #~ plt.imshow(images[5])
            #~ plt.show()
            #~ plt.close()
            
            print(self.cube)
            
            return True
        
        elif option == '4':
            if self.cube == None:
                print('No cube')
                return True
            self.algo = AlgoCFOP(cube)
            self.algo.solve()
            length = len(self.algo.movelist)
            print('Algorithm generated with ', length, ' moves')
            return True
        
        elif option == '5':
            if self.cube == None:
                print('No cube')
                return True
            self.solveCube(algo.movelist)
            print('Cube solved')
            return True

        elif option == '6':
            if self.cube == None:
                print('No cube')
                return True
            self.algo = AlgoCFOP(cube)
            self.algo.randomize()
            self.solveCube(algo.movelist)
            print('Cube randomized')
            return True

        elif option == '7':
            self.cube = self.makeCube()
            self.algo = AlgoCFOP(cube)
            self.algo.solve()
            self.solveCube(algo.movelist)
            print('Cube solved')
            return True

        elif option == '8':
            print('Session ended')
            return False
        
        else:
            print('ERROR: Invalid entry')
            return True
    
    def makeCube(self, images):
        
            frontFace = Face(np.rot90(self.makeFace(images[0]),2))
            backFace = Face(self.makeFace(images[1]))
            rightFace = Face(np.rot90(self.makeFace(images[2]),3))
            leftFace = Face(np.rot90(self.makeFace(images[3]),1))
            downFace = Face(np.rot90(self.makeFace(images[4]),2))
            upFace = Face(np.rot90(self.makeFace(images[5]),2))
                        
            self.cube = Cube(upFace, downFace, frontFace, backFace, leftFace, rightFace)
        
        #~ inputStage = True
        #~ while inputStage == True:            
            
            #~ # Input current cube state
            #~ upColors = input('Up layer colors: ')
            #~ frontColors = input('Front layer colors: ')
            #~ downColors = input('Down layer colors: ')
            #~ rightColors = input('Right layer colors: ')
            #~ backColors = input('Back layer colors: ')
            #~ leftColors = input('Left layer colors: ')
            #~ colorSides = [upColors, frontColors, downColors, rightColors, backColors, leftColors]

            #~ # Create numpy arrays
            #~ up = np.empty([3,3], dtype=np.str)
            #~ front = np.empty([3,3], dtype=np.str)
            #~ down = np.empty([3,3], dtype=np.str)
            #~ right = np.empty([3,3], dtype=np.str)
            #~ back = np.empty([3,3], dtype=np.str)
            #~ left = np.empty([3,3], dtype=np.str)
            #~ faces = [up, front, down, right, back, left]
     
            #~ # Fill numpy arrays
            #~ for i in range(6):
                #~ for j in range(3):
                    #~ for k in range(3):
                        #~ faces[i][j][k] = colorSides[i][3*j + k]
                        
            #~ # Instantiate faces
            #~ up = Face(up)
            #~ down = Face(down)
            #~ front = Face(front)
            #~ back = Face(back)
            #~ left = Face(left)
            #~ right = Face(right)

            #~ # Instantiate cube
            #~ cube = Cube(up, down, front, back, left, right)
            #~ print(cube)
            #~ status = input('Is this correct? (y,n): ')
            #~ if status == 'n' or status == 'N':
                #~ inputStage = True
                #~ print('')
            #~ else:
                #~ inputStage = False

            return self.cube

    def solveCube(self, movelist):
        frame = self.frame

        for i in range(len(movelist)):
            if movelist[i] == 'X':
                frame.rotate90('X')
            elif movelist[i] == 'Xi':
                frame.rotate90('X', inverse=True)
            elif movelist[i] == 'Z':
                frame.rotate90('Z')
            elif movelist[i] == 'Zi':
                frame.rotate90('Z', inverse=True)
            elif movelist[i] == 'Y':
                frame.rotate90('Y')
            elif movelist[i] == 'Yi':
                frame.rotate90('Y', inverse=True)
            elif movelist[i] == '2X':
                frame.rotate180('X')
            elif movelist[i] == '2Y':
                frame.rotate180('Y')
            elif movelist[i] == '2Z':
                frame.rotate180('Z')
            elif movelist[i] == 'F':
                frame.turn90('F')
            elif movelist[i] == 'Fi':
                frame.turn90('F', inverse=True)
            elif movelist[i] == 'B':
                frame.turn90('B')
            elif movelist[i] == 'Bi':
                frame.turn90('B', inverse=True)
            elif movelist[i] == 'L':
                frame.turn90('L')
            elif movelist[i] == 'Li':
                frame.turn90('L', inverse=True)
            elif movelist[i] == 'R':
                frame.turn90('R')
            elif movelist[i] == 'Ri':
                frame.turn90('R', inverse=True)
            elif movelist[i] == 'U':
                frame.turn90('U')
            elif movelist[i] == 'Ui':
                frame.turn90('U', inverse=True)
            elif movelist[i] == 'D':
                frame.turn90('D')
            elif movelist[i] == 'Di':
                frame.turn90('D', inverse=True)
            elif movelist[i] == '2F':
                frame.turn180('F')
            elif movelist[i] == '2B':
                frame.turn180('B')
            elif movelist[i] == '2L':
                frame.turn180('L')
            elif movelist[i] == '2R':
                frame.turn180('R')
            elif movelist[i] == '2U':
                frame.turn180('U')
            elif movelist[i] == '2D':
                frame.turn180('D')
            else:
                pass

        return
        
        
        
    def getSample(self, img, x, y, average=False):

        if average == False:
            return img[y,x,:]
        
        elif average == True:
            ctr = img[y,x,:]
            top = img[y+5,x,:]
            btm = img[y-5,x,:]
            lft = img[y,x-5,:]
            rht = img[y,x+5,:]

            samples = [ctr, top, btm, lft, rht]

            sums = np.empty(5)

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
        
        w=np.array([189,171,154])
        y=np.array([163,128,62])
        r=np.array([113,42,49])
        o=np.array([106,77,68])
        g=np.array([49,80,63])
        b=np.array([31,47,83])

        colors = [w, y, r, o, g, b]
        dist = np.empty((6), dtype=np.float) 

        i = 0
        for col in colors:
            print(((rgb[0]-col[0])**2) + ((rgb[1]-col[1])**2) + ((rgb[2]-col[2])**2))
            
            dist[i] = (np.sqrt(((rgb[0]-col[0])**2) + ((rgb[1]-col[1])**2) + ((rgb[2]-col[2])**2)))
            
            i+=1

        out = np.argmin(dist)
        clrs = ['w', 'y', 'r', 'o', 'g', 'b']

        return clrs[out]

    def makeFace(self, img):
        
        colorArray=np.empty((3,3),dtype=str)
        findColor = self.findColor
        getSample = self.getSample

        x = 28
        y = 38
        d = 30

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
