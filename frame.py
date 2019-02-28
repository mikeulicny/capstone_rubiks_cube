import time
from claw import Claw
import numpy

class Frame:

    """
    The interface class for the physical rubiks cube itself
    This class contains the following:
        -initializes claw positions
        -opens claws to set cube
        -provides functions for rotating and turns
    Class functions
        .rotate90(axis, inverse=False)
        .rotate180(axis, inverse=False)
        .turn90(face, inverse=False)
        .turn180(face, inverse=False)
    """


    def __init__(self, clawDelay=1, rotateDelay=1):
        self.__servoArray = numpy.arange(8)
        self.frontClaw = claw(self.clawID=__servoArray[0], self.armID=__servoArray[1])
        self.rightClaw = claw(self.clawID=__servoArray[2], self.armID=__servoArray[3])
        self.backClaw = claw(self.clawID=__servoArray[4], self.armID=__servoArray[5])
        self.leftClaw = claw(self.clawID=__servoArray[6], self.armID=__servoArray[7])
        self.clawDelay = clawDelay
        self.rotateDelay = rotateDelay
        # NOTE: clawDelay and rotateDelay are currently set to 1 second for debugging
        #   pursposes. These are to be changed to clawDelay = 0.35 and rotateDelay = 0.5
        #   for final runs. These numbers are rough estimates and should be fine tuned
        #   to increase speed of the cube moves


    def rotate90(self, axis, inverse = False):
        """
        rotate90(axis, inverse=0)
        rotate function will rotate the cube. If the rotation is along the "Y" axis it will instead
        remap which claw is the front, right, left, and back
        """
        clawDelay = self.clawDelay
        rotateDelay=self.rotateDelay
        if axis != ('X' or 'Y' or 'Z'):
            print("Error: rotate90 function invalid axis parameter")
            return None
        if axis == 'X':
            self.frontClaw.openClaw()       # open z axis
            self.backClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                self.righClaw.rotate(180)   # rotate x axis -90 deg position
                self.leftClaw.rotate(0)     #   OR
            else:
                self.rightClaw.rotate(0)    # rotate x axis +90 deg position
                self.leftClaw.rotate(180)
            time.sleep(rotateDelay)
            # TODO: get position of servo to determine delay. (0 deg smaller delay, 180 deg larger delay)
            self.frontClaw.closeClaw()      # close z axis
            self.backClaw.closeClaw()
            time.sleep(clawDelay)
            self.rightClaw.openClaw()       # open x axis
            self.leftClaw.openClaw()
            time.sleep(clawDelay)
            self.rightClaw.rotate(90)       # set x axis to 0 deg position
            self.leftClaw.rotate(90)
            time.sleep(rotateDelay)
            self.rightClaw.close()          # close x axis
            self.leftClaw.close()
            time.sleep(clawDelay)
        elif axis == 'Z':
            self.leftClaw.openClaw()        # open x axis
            self.rightClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                self.frontClaw.rotate(180)  # rotate z axis -90 deg position
                self.backClaw.rotate(0)     #   OR
            else:
                self.frontClaw.rotate(0)    # rotate z axis +90 deg position
                self.backClaw.rotate(180)
            time.sleep(rotateDelay)
            self.rightClaw.closeClaw()       # close x axis
            self.leftClaw.closeClaw()
            time.sleep(clawDelay)
            self.frontClaw.openClaw()       # open z axis
            self.backClaw.openClaw()
            time.sleep(clawDelay)
            self.frontClaw.rotate(90)       # set z axis to 0 deg position
            self.backClaw.rotate(90)
            time.sleep(rotateDelay)
            self.frontClaw.closeClaw()      # close z axis
            self.backClaw.closeClaw()
            time.sleep(clawDelay)
        elif axis == 'Y':
            # remap claws instead of making moves. Reduces time and moves
            #   on the physical Rubik's Cube
            if inverse:
                self.__servoArray = numpy.roll(__servoArray, -2)
            else:
                self.__servoArray = numpy.roll(__servoArray, 2)
            self.frontClaw.clawID = __servoArray[0]
            self.frontClaw.armID = __servoArray[1]
            self.rightClaw.clawID = __servoArray[2]
            self.rightClaw.armID = __servoArray[3]
            self.backClaw.clawID = __servoArray[4] 
            self.backClaw.armID = __servoArray[5]
            self.leftClaw.clawID = __servoArray[6]
            self.leftClaw.armID = __servoArray[7]
            

    def rotate180(axis, inverse = False):
        """
        rotate180(axis, inverse=0)
        rotate function will rotate the cube. If the rotation is along the "Y" axis it will instead
        remap which claw is the front, right, left, and back.
        The 180 degree rotation just pre-sets the position of the claws and then calls the rotate90 function
        """
        clawDelay = self.clawDelay
        rotateDelay=self.rotateDelay

        if axis != ('X' or 'Y' or 'Z'):
            print("Error: rotate180 function invalid axis parameter")
            return None
        if axis == 'X':
            self.rightClaw.openClaw()           # open x axis
            self.leftClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                self.rightClaw.rotate(180)        # set x axis to +90 deg position
                self.leftClaw.rotate(0)       #   OR
            else:
                self.rightClaw.rotate(0)      # set x axis to -90 deg position
                self.leftClaw.rotate(180)
            time.sleep(rotateDelay)
            self.rightClaw.closeClaw()          # close x axis
            self.leftClaw.closeClaw()
            time.sleep(clawDelay)
            self.rotate90('X', inverse=inverse) # This will complete 180 deg rotation

        elif axis == 'Z':
            self.frontClaw.openClaw()           # open z axis
            self.backClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                self.frontClaw.rotate(180)        # set z axis to +90 deg position
                self.backClaw.rotate(0)       #   OR
            else:
                self.frontClaw.rotate(0)      # set z axis to -90 deg position
                self.backClaw.rotate(180)
            time.sleep(rotateDelay)
            self.frontClaw.closeClaw()          # close z axis
            self.backClaw.closeClaw()
            self.rotate90('Z', inverse=inverse) # This will complete 180 deg rotation

        elif axis == 'Y':
            # remap claws instead of making moves. Reduces time and moves
            #   on the physical Rubik's Cube
            if inverse:
                self.__servoArray = numpy.roll(__servoArray, -4)
            else:
                self.__servoArray = numpy.roll(__servoArray, 4)
            self.frontClaw.clawID = __servoArray[0]
            self.frontClaw.armID = __servoArray[1]
            self.rightClaw.clawID = __servoArray[2]
            self.rightClaw.armID = __servoArray[3]
            self.backClaw.clawID = __servoArray[4] 
            self.backClaw.armID = __servoArray[5]
            self.leftClaw.clawID = __servoArray[6]
            self.leftClaw.armID = __servoArray[7]


    def turn90(face, inverse = False):
        """
        turn90(face, inverse=0)
        turn function does not remap any faces
        """
        clawDelay = self.clawDelay
        rotateDelay=self.rotateDelay

        if face != ('F' or 'B' or 'L' or 'R' or 'U' or 'D'):
            print("Error: turn90 function invalid face parameter")
            return None
        if inverse:
            deg = 0
        else:
            deg = 180
        if face == 'F':
            self.frontClaw.rotate(deg)      # turn side
            time.sleep(rotateDelay)
            self.frontClaw.openClaw()       # open claw
            time.sleep(clawDelay)
            self.frontClaw.rotate(90)       # reset claw
            time.sleep(rotateDelay)
            self.frontClaw.closeClaw()      # close claw
            time.sleep(clawDelay)

        elif face == 'B':
            self.backClaw.rotate(deg)
            time.sleep(rotateDelay)
            self.backClaw.openClaw()
            time.sleep(clawDelay)
            self.backClaw.rotate(90)
            time.sleep(rotateDelay)
            self.backClaw.closeClaw()

        elif face == 'L':
            self.leftClaw.rotate(deg)
            time.sleep(rotateDelay)
            self.leftClaw.openClaw()
            time.sleep(clawDelay)
            self.leftClaw.rotate(90)
            time.sleep(rotateDelay)
            self.leftClaw.closeClaw()

        elif face == 'R':
            self.rightClaw.rotate(deg)
            time.sleep(rotateDelay)
            self.rightClaw.openClaw()
            time.sleep(clawDelay)
            self.rightClaw.rotate(90)
            time.sleep(rotateDelay)
            self.rightClaw.closeClaw()
            
        elif face == 'U' or 'D':
            self.rightClaw.openClaw()       # open x axis
            self.leftClaw.openClaw()
            time.sleep(clawDelay)
            self.rightClaw.rotate(180)      # set x axis to +90 deg position
            self.leftClaw.rotate(0)
            time.sleep(rotateDelay)
            self.rightClaw.closeClaw()      # close x axis
            self.leftClaw.closeClaw()
            time.sleep(clawDelay)
            self.frontClaw.openClaw()       # open z axis
            self.backClaw.openClaw()
            time.sleep(clawDelay)
            self.rightClaw.rotate(90)       # rotate claws to 0 deg position
            self.leftClaw.rotate(90)
            time.sleep(rotateDelay)
            self.frontClaw.closeClaw()      # close z axis
            self.backClaw.closeClaw()
            time.sleep(clawDelay)
            if face == 'U':
                self.frontClaw.rotate(deg)  # rotate up face
                time.sleep(rotateDelay)
            elif face == 'D':
                self.backClaw.rotate(deg)   # rotate down face
                time.sleep(rotateDelay)
            self.frontClaw.openClaw()       # open z axis
            self.backClaw.openClaw()         
            time.sleep(clawDelay)
            self.frontClaw.rotate(90)       # rotate z axis to 0 deg position
            self.backClaw.rotate(90)
            time.sleep(rotateDelay)
            self.rightClaw.rotate(0)        # set cube back to original position
            self.leftClaw.rotate(180)
            time.sleep(rotateDelay)
            self.frontClaw.closeClaw()      # close z axis
            self.backClaw.closeClaw()
            time.sleep(clawDelay)
            self.rightClaw.openClaw()       # open x axis
            self.leftClaw.openClaw()
            time.sleep(clawDelay)
            self.rightClaw.rotate(90)       # rotate x axis to 0 deg position
            self.leftClaw.rotate(90)
            time.sleep(rotateDelay)
            self.rightClaw.closeClaw()      # close x axis
            self.leftClaw.closeClaw()

    def turn180(face, inverse = False):
        """
        turn180(face, inverse=0)
        turn function does not remap any faces
        """
        clawDelay = self.clawDelay
        rotateDelay=self.rotateDelay
        
        if face != ('F' or 'B' or 'L' or 'R' or 'U' or 'D'):
            print("Error: turn180 function invalid face parameter")
            return None
        elif face == 'F':
            pass
        elif face == 'B':
            pass
        elif face == 'L':
            pass
        elif face == 'R':
            pass
        
