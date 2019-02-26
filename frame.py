import time
import claw
import numpy

class rubiksCube:
    """
    The interface class for the physical rubiks cube itself
    This class contains the following:
        -initializes claw positions
        -opens claws to set cube
        -provides functions for rotating and turns
    """


    def __init__(self, clawDelay=1, rotateDelay=1):
        self.__servoArray = numpy.arange(8)
        self.frontClaw = claw(clawID=__servoArray[0], armID=__servoArray[1])
        self.rightClaw = claw(clawID=__servoArray[2], armID=__servoArray[3])
        self.backClaw = claw(clawID=__servoArray[4], armID=__servoArray[5])
        self.leftClaw = claw(clawID=__servoArray[6], armID=__servoArray[7])
        self.clawDelay = clawDelay
        self.rotateDelay = rotateDelay
        # NOTE: clawDelay and rotateDelay are currently set to 1 second for debugging
        #   pursposes. These are to be changed to clawDelay = 0.35 and rotateDelay = 0.5
        #   for final runs. These numbers are rough estimates and should be fine tuned
        #   to increase speed of the cube moves


    def rotate90(self, axis, inverse = False):

        """
        rotate90(axis, inverse=0)
        rotate function remaps the faces of the cubes which remaps the labels
            for the claws
        """
        if axis != 'X' or 'Y' or 'Z':
            print("Error: rotate90 function invalid axis parameter")
            return NULL
        elif axis == 'X':
            self.frontClaw.openClaw()    # open z axis
            self.backClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                self.righClaw.rotate(180)
                self.leftClaw.rotate(0)
            else:
                self.rightClaw.rotate(0)     # rotate x axis +90 deg
                self.leftClaw.rotate(180)
            time.sleep(rotateDelay)
            self.frontClaw.closeClaw()   # close z axis
            self.backClaw.closeClaw()
            time.sleep(clawDelay)
            self.rightClaw.openClaw()    # open x axis
            self.leftClaw.openClaw()
            time.sleep(clawDelay)
            self.rightClaw.rotate(90)    # set x axis to default
            self.leftClaw.rotate(90)
            time.sleep(rotateDelay)
            self.rightClaw.close()       # close x axis
            self.leftClaw.close()
            time.sleep(clawDelay)
        elif axis == 'Z':
            self.leftClaw.openClaw()     # open x axis
            self.rightClaw.openClaw()
            time.sleep(clawDelay)
            if inverse:
                self.frontClaw.rotate(180)
                self.backClaw.rotate(0)
            else:
                self.frontClaw.rotate(0)     # rotate z axis +90 deg
                self.backClaw.rotate(180)
            time.sleep(rotateDelay)
            self.leftClaw.closeClaw()    # close x axis
            self.rightClaw.closeClaw()
            time.sleep(clawDelay)
            self.frontClaw.openClaw()    # open z axis
            self.backClaw.openClaw()
            time.sleep(clawDelay)
            self.frontClaw.rotate(90)    # set z axis to default
            self.backClaw.rotate(90)
            time.sleep(rotateDelay)
            self.frontClaw.closeClaw()   # close z axis
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
        rotate function remaps the faces of the cubes which remaps the labels
            for the claws
        """
        if axis != 'X' or 'Y' or 'Z':
            print("Error: rotate180 function invalid axis parameter")
            return NULL
        # TODO: this

    def turn90(face, inverse = False):
        """
        turn90(face, inverse=0)
        turn function does not remap any faces
        """
        if face != 'F' or 'B' or 'L' or 'R' or 'U' or 'D':
            print("Error: turn90 function invalid face parameter")
            return NULL
        # TODO: this

    def turn180(face, inverse = False):
        """
        turn180(face, inverse=0)
        turn function does not remap any faces
        """
        if face != 'F' or 'B' or 'L' or 'R' or 'U' or 'D':
            print("Error: turn180 function invalid face parameter")
            return NULL
            # TODO: this
