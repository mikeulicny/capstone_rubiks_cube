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


    def __init__(self, clawDelay=1, rotateDelay90=1):
        self.__servoArray = numpy.arange(8)
        self.frontClaw = claw(self.clawID=__servoArray[0], self.armID=__servoArray[1])
        self.rightClaw = claw(self.clawID=__servoArray[2], self.armID=__servoArray[3])
        self.backClaw = claw(self.clawID=__servoArray[4], self.armID=__servoArray[5])
        self.leftClaw = claw(self.clawID=__servoArray[6], self.armID=__servoArray[7])
        self.clawDelay = clawDelay
        self.rotateDelay90 = rotateDelay90
        self.rotateDelay180 = 2*rotateDelay90
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
        rotateDelay90 = self.rotateDelay90
        rotateDelay180 = self.rotateDelay180
        frontClaw = self.frontClaw
        backClaw = self.backClaw
        rightClaw = self.rightClaw
        leftClaw = self.leftClaw

        if axis != ('X' or 'Y' or 'Z'):
            print("Error: rotate90 function invalid axis parameter")
            return None
        if axis == 'X':
            frontClaw.openClaw()       # open z axis
            backClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                righClaw.rotate(180)   # rotate x axis -90 deg position
                leftClaw.rotate(0)     #   OR
            else:
                rightClaw.rotate(0)    # rotate x axis +90 deg position
                leftClaw.rotate(180)
            time.sleep(rotateDelay90)
            frontClaw.closeClaw()      # close z axis
            backClaw.closeClaw()
            time.sleep(clawDelay)
            rightClaw.openClaw()       # open x axis
            leftClaw.openClaw()
            time.sleep(clawDelay)
            rightClaw.rotate(90)       # set x axis to 0 deg position
            leftClaw.rotate(90)
            time.sleep(rotateDelay90)
            rightClaw.close()          # close x axis
            leftClaw.close()
            time.sleep(clawDelay)
        elif axis == 'Z':
            leftClaw.openClaw()        # open x axis
            rightClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                frontClaw.rotate(180)  # rotate z axis -90 deg position
                backClaw.rotate(0)     #   OR
            else:
                frontClaw.rotate(0)    # rotate z axis +90 deg position
                backClaw.rotate(180)
            time.sleep(rotateDelay90)
            rightClaw.closeClaw()       # close x axis
            leftClaw.closeClaw()
            time.sleep(clawDelay)
            frontClaw.openClaw()       # open z axis
            backClaw.openClaw()
            time.sleep(clawDelay)
            frontClaw.rotate(90)       # set z axis to 0 deg position
            backClaw.rotate(90)
            time.sleep(rotateDelay90)
            frontClaw.closeClaw()      # close z axis
            backClaw.closeClaw()
            time.sleep(clawDelay)
        elif axis == 'Y':
            # remap claws instead of making moves. Reduces time and moves
            #   on the physical Rubik's Cube
            if inverse:
                self.__servoArray = numpy.roll(__servoArray, -2)
            else:
                self.__servoArray = numpy.roll(__servoArray, 2)
            frontClaw.clawID = __servoArray[0]
            frontClaw.armID = __servoArray[1]
            rightClaw.clawID = __servoArray[2]
            rightClaw.armID = __servoArray[3]
            backClaw.clawID = __servoArray[4] 
            backClaw.armID = __servoArray[5]
            leftClaw.clawID = __servoArray[6]
            leftClaw.armID = __servoArray[7]
            

    def rotate180(axis, inverse = False):
        """
        rotate180(axis, inverse=0)
        rotate function will rotate the cube. If the rotation is along the "Y" axis it will instead
        remap which claw is the front, right, left, and back.
        The 180 degree rotation just pre-sets the position of the claws and then calls the rotate90 function
        """
        clawDelay = self.clawDelay
        rotateDelay90 = self.rotateDelay90
        rotateDelay180 = self.rotateDelay180
        frontClaw = self.frontClaw
        backClaw = self.backClaw
        rightClaw = self.rightClaw
        leftClaw = self.leftClaw

        if axis != ('X' or 'Y' or 'Z'):
            print("Error: rotate180 function invalid axis parameter")
            return None
        if axis == 'X':
            rightClaw.openClaw()           # open x axis
            leftClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                rightClaw.rotate(180)        # set x axis to +90 deg position
                leftClaw.rotate(0)       #   OR
            else:
                rightClaw.rotate(0)      # set x axis to -90 deg position
                leftClaw.rotate(180)
            time.sleep(rotateDelay90)
            rightClaw.closeClaw()          # close x axis
            leftClaw.closeClaw()
            time.sleep(clawDelay)
            frontClaw.openClaw()       # open z axis
            backClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                righClaw.rotate(0)   # rotate x axis -90 deg position
                leftClaw.rotate(180)     #   OR
            else:
                rightClaw.rotate(180)    # rotate x axis +90 deg position
                leftClaw.rotate(0)
            time.sleep(rotateDelay180)
            frontClaw.closeClaw()      # close z axis
            backClaw.closeClaw()
            time.sleep(clawDelay)
            rightClaw.openClaw()       # open x axis
            leftClaw.openClaw()
            time.sleep(clawDelay)
            rightClaw.rotate(90)       # set x axis to 0 deg position
            leftClaw.rotate(90)
            time.sleep(rotateDelay90)
            rightClaw.close()          # close x axis
            leftClaw.close()
            time.sleep(clawDelay)


        elif axis == 'Z':
            frontClaw.openClaw()           # open z axis
            backClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                frontClaw.rotate(180)        # set z axis to +90 deg position
                backClaw.rotate(0)       #   OR
            else:
                frontClaw.rotate(0)      # set z axis to -90 deg position
                backClaw.rotate(180)
            time.sleep(rotateDelay90)
            frontClaw.closeClaw()          # close z axis
            backClaw.closeClaw()
            leftClaw.openClaw()        # open x axis
            rightClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                frontClaw.rotate(0)  # rotate z axis -90 deg position
                backClaw.rotate(180)     #   OR
            else:
                frontClaw.rotate(180)    # rotate z axis +90 deg position
                backClaw.rotate(0)
            time.sleep(rotateDelay180)
            rightClaw.closeClaw()       # close x axis
            leftClaw.closeClaw()
            time.sleep(clawDelay)
            frontClaw.openClaw()       # open z axis
            backClaw.openClaw()
            time.sleep(clawDelay)
            frontClaw.rotate(90)       # set z axis to 0 deg position
            backClaw.rotate(90)
            time.sleep(rotateDelay90)
            frontClaw.closeClaw()      # close z axis
            backClaw.closeClaw()
            time.sleep(clawDelay)

        elif axis == 'Y':
            # remap claws instead of making moves. Reduces time and moves
            #   on the physical Rubik's Cube
            if inverse:
                self.__servoArray = numpy.roll(__servoArray, -4)
            else:
                self.__servoArray = numpy.roll(__servoArray, 4)
            frontClaw.clawID = __servoArray[0]
            frontClaw.armID = __servoArray[1]
            rightClaw.clawID = __servoArray[2]
            rightClaw.armID = __servoArray[3]
            backClaw.clawID = __servoArray[4] 
            backClaw.armID = __servoArray[5]
            leftClaw.clawID = __servoArray[6]
            leftClaw.armID = __servoArray[7]


    def turn90(face, inverse = False):
        """
        turn90(face, inverse=0)
        turn function does not remap any faces
        """
        clawDelay = self.clawDelay
        rotateDelay90 = self.rotateDelay90
        rotateDelay180 = self.rotateDelay180
        frontClaw = self.frontClaw
        backClaw = self.backClaw
        rightClaw = self.rightClaw
        leftClaw = self.leftClaw

        if face != ('F' or 'B' or 'L' or 'R' or 'U' or 'D'):
            print("Error: turn90 function invalid face parameter")
            return None
        if inverse:
            deg = 0
        else:
            deg = 180
        if face == 'F':
            frontClaw.rotate(deg)      # turn side
            time.sleep(rotateDelay90)
            frontClaw.openClaw()       # open claw
            time.sleep(clawDelay)
            frontClaw.rotate(90)       # reset claw
            time.sleep(rotateDelay90)
            frontClaw.closeClaw()      # close claw
            time.sleep(clawDelay)

        elif face == 'B':
            backClaw.rotate(deg)
            time.sleep(rotateDelay90)
            backClaw.openClaw()
            time.sleep(clawDelay)
            backClaw.rotate(90)
            time.sleep(rotateDelay90)
            backClaw.closeClaw()

        elif face == 'L':
            leftClaw.rotate(deg)
            time.sleep(rotateDelay90)
            leftClaw.openClaw()
            time.sleep(clawDelay)
            leftClaw.rotate(90)
            time.sleep(rotateDelay90)
            leftClaw.closeClaw()

        elif face == 'R':
            rightClaw.rotate(deg)
            time.sleep(rotateDelay90)
            rightClaw.openClaw()
            time.sleep(clawDelay)
            rightClaw.rotate(90)
            time.sleep(rotateDelay90)
            rightClaw.closeClaw()
            
        elif face == 'U' or 'D':
            rightClaw.openClaw()       # open x axis
            leftClaw.openClaw()
            time.sleep(clawDelay)
            rightClaw.rotate(180)      # set x axis to +90 deg position
            leftClaw.rotate(0)
            time.sleep(rotateDelay90)
            rightClaw.closeClaw()      # close x axis
            leftClaw.closeClaw()
            time.sleep(clawDelay)
            frontClaw.openClaw()       # open z axis
            backClaw.openClaw()
            time.sleep(clawDelay)
            rightClaw.rotate(90)       # rotate claws to 0 deg position
            leftClaw.rotate(90)
            time.sleep(rotateDelay90)
            frontClaw.closeClaw()      # close z axis
            backClaw.closeClaw()
            time.sleep(clawDelay)
            if face == 'U':
                frontClaw.rotate(deg)  # rotate up face
                time.sleep(rotateDelay90)
            elif face == 'D':
                backClaw.rotate(deg)   # rotate down face
                time.sleep(rotateDelay90)
            frontClaw.openClaw()       # open z axis
            backClaw.openClaw()         
            time.sleep(clawDelay)
            frontClaw.rotate(90)       # rotate z axis to 0 deg position
            backClaw.rotate(90)
            time.sleep(rotateDelay90)
            rightClaw.rotate(0)        # set cube back to original position
            leftClaw.rotate(180)
            time.sleep(rotateDelay90)
            frontClaw.closeClaw()      # close z axis
            backClaw.closeClaw()
            time.sleep(clawDelay)
            rightClaw.openClaw()       # open x axis
            leftClaw.openClaw()
            time.sleep(clawDelay)
            rightClaw.rotate(90)       # rotate x axis to 0 deg position
            leftClaw.rotate(90)
            time.sleep(rotateDelay90)
            rightClaw.closeClaw()      # close x axis
            leftClaw.closeClaw()

    def turn180(face, inverse = False):
        """
        turn180(face, inverse=0)
        turn function does not remap any faces
        """
        clawDelay = self.clawDelay
        rotateDelay90 = self.rotateDelay90
        rotateDelay180 = self.rotateDelay180
        frontClaw = self.frontClaw
        backClaw = self.backClaw
        rightClaw = self.rightClaw
        leftClaw = self.leftClaw
        
        if face != ('F' or 'B' or 'L' or 'R' or 'U' or 'D'):
            print("Error: turn180 function invalid face parameter")
            return None
        
        if inverse:
            deg = 0
        else:
            deg = 180

        if face == 'F':
            frontClaw.openClaw()        # open claw
            time.sleep(clawDelay)
            if inverse:
                frontClaw.rotate(180)   # rotate opposite direction of turn
            else:
                frontClaw.rotate(0)
            time.sleep(rotateDelay90)
            frontClaw.closeClaw()       # close claw
            time.sleep(clawDelay)
            frontClaw.rotate(deg)       # turn side 180
            time.sleep(rotateDelay180)
            frontClaw.openClaw()        # open claw
            time.sleep(clawDelay)
            frontClaw.rotate(90)        # reset claw
            time.sleep(rotateDelay90)
            frontClaw.closeClaw()       # close claw
            time.sleep(clawDelay)

        elif face == 'B':
            backClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                backClaw.rotate(180)
            else:
                backClaw.rotate(0)
            time.sleep(rotateDelay90)
            backClaw.closeClaw()
            time.sleep(clawDelay)
            backClaw.rotate(deg)
            time.sleep(rotateDelay180)
            backClaw.openClaw()
            time.sleep(clawDelay)
            backClaw.rotate(90)
            time.sleep(rotateDelay90)
            backClaw.closeClaw()
            time.sleep(clawDelay)

        elif face == 'L':
            leftClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                leftClaw.rotate(180)
            else:
                leftClaw.rotate(0)
            time.sleep(rotateDelay90)
            leftClaw.closeClaw()
            time.sleep(clawDelay)
            leftClaw.rotate(deg)
            time.sleep(rotateDelay180)
            leftClaw.openClaw()
            time.sleep(clawDelay)
            leftClaw.rotate(90)
            time.sleep(rotateDelay90)
            leftClaw.closeClaw()
            time.sleep(clawDelay)
        elif face == 'R':
            rightClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                rightClaw.rotate(180)
            else:
                rightClaw.rotate(0)
            time.sleep(rotateDelay90)
            rightClaw.closeClaw()
            time.sleep(clawDelay)
            rightClaw.rotate(deg)
            time.sleep(rotateDelay180)
            rightClaw.openClaw()
            time.sleep(clawDelay)
            rightClaw.rotate(90)
            time.sleep(rotateDelay90)
            rightClaw.closeClaw()
            time.sleep(clawDelay)
        
        elif face == ('U' or 'D'):
            frontClaw.openClaw()        # rotate x axis
            backClaw.openClaw()
            time.sleep(clawDelay)
            rightClaw.rotate(0)
            leftClaw.rotate(180)
            time.sleep(rotateDelay90)
            frontClaw.closeClaw()
            backClaw.closeClaw()
            time.sleep(clawDelay)
            rightClaw.openClaw()
            leftClaw.openClaw()
            time.sleep(clawDelay)
            rightClaw.rotate(90)
            leftClaw.rotate(90)
            time.sleep(rotateDelay90)
            rightClaw.closeClaw()
            leftClaw.closeClaw()
            time.sleep(clawDelay)
            if face == 'U':
                frontClaw.openClaw()        # turn front 180 deg
                time.sleep(clawDelay)
                if inverse:
                    frontClaw.rotate(180)
                else:
                    frontClaw.rotate(0)
                time.sleep(rotateDelay90)
                frontClaw.closeClaw()
                time.sleep(clawDelay)
                frontClaw.rotate(deg)
                time.sleep(rotateDelay180)
                frontClaw.openClaw()
                time.sleep(clawDelay)
                frontClaw.rotate(90)
                time.sleep(rotateDelay90)
                frontClaw.closeClaw()
            elif face == 'D':               # turn back 180 deg
                backClaw.openClaw()
                time.sleep(clawDelay)
                if inverse:
                    backClaw.rotate(180)
                else:
                    backClaw.rotate(0)
                time.sleep(rotateDelay90)
                backClaw.closeClaw()
                time.sleep(clawDelay)
                backClaw.rotate(deg)
                time.sleep(rotateDelay180)
                backClaw.openClaw()
                time.sleep(clawDelay)
                backClaw.rotate(90)
                time.sleep(rotateDelay90)
                backClaw.closeClaw()
            rightClaw.openClaw()
            leftClaw.openClaw()
            time.sleep(clawDelay)
            rightClaw.rotate(0)
            leftClaw.rotate(180)
            time.sleep(rotateDelay90)
            rightClaw.closeClaw()
            leftClaw.closeClaw()
            time.sleep(clawDelay)
            frontClaw.openClaw()
            backClaw.openClaw()
            time.sleep(clawDelay)
            rightClaw.rotate(90)
            leftClaw.rotate(90)
            time.sleep(rotateDelay90)
            frontClaw.closeClaw()
            backClaw.closeClaw()
            time.sleep(clawDelay)
        
