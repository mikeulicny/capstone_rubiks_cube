from frame import Frame
from algocfop import AlgoCFOP
from cube import Cube
from image import Image
import time
import numpy as np

class Session:

    def __init__(self):
        self.frame = Frame()
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
        frame = self.frame
        cube = self.cube
        algo = self.algo
        
        option = input('Please select an option from the list above and hit enter: ')

        if option == '1':
            frame.openClaws()
            return True
        
        elif option == '2':
            frame.closeClaws()
            return True

        elif option == '3':
            cube = self.makeCube()
            print('Your cube...')
            cube.__str__()
            return True
        
        elif option == '4':
            if cube == None:
                print('No cube')
                return True
            algo = AlgoCFOP(cube)
            algo.solve()
            length = len(algo.movelist)
            print('Algorithm generated with ', length, ' moves')
            return True
        
        elif option == '5':
            if cube == None:
                print('No cube')
                return True
            self.solveCube(algo.movelist)
            print('Cube solved')
            return True

        elif option == '6':
            if cube == None:
                print('No cube')
                return True
            algo = AlgoCFOP(cube)
            algo.randomize()
            self.solveCube(algo.movelist)
            print('Cube randomized')
            return True

        elif option == '7':
            cube = self.makeCube()
            algo = AlgoCFOP(cube)
            algo.solve()
            self.solveCube(algo.movelist)
            print('Cube solved')
            return True

        elif option == '8':
            print('Session ended')
            return False
        
        else:
            print('ERROR: Invalid entry')
            return True
    
    def makeCube(self):
        frame = self.frame
        cube = self.cube
        img1 = Image()
        img2 = Image()
        faces = np.empty(6)

        flip = 'X'
        for i in faces:
            frame.openClawsFB()
            img1 = img1.capture()
            colorArray = img1.makeFace('A')     
            frame.closeClawsFB()
            
            frame.openClawsLR()
            img2 = img2.capture()
            f = img2.makeFace('B', colorArray)
            frame.closeClawsLR()
            faces[i] = f

            if flip == 'X':
                frame.rotate90(flip, inverse=True)
                flip = 'Z'
            elif flip == 'Z':
                frame.rotate90(flip)
                flip == 'X' 

        faces[2] = np.rot90(faces[2], 3)
        faces[3] = np.rot90(faces[3], 3)
        faces[4] = np.rot90(faces[4], 1)
        cube = Cube(faces[0],faces[1],faces[2],faces[3],faces[4],faces[5])

        return cube

    def solveCube(self, movelist):
        frame = self.frame

        for i in movelist:
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
