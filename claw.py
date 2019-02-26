import time
from adafruit_servokit import ServoKit

class Claw:
	# static class elements. DO NOT CHANGE
	kit = ServoKit(channels=16)

	def __init__(self, clawID, armID):
		# object elements
		self.clawID = clawID
		self.armID = armID


	def openClaw(self):
		kit.servo[clawID].angle = 60

	def closeClaw(self):
		# TODO: Change the value to correct claw grip size
		kit.servo[clawID].angle = 0

	def rotate(self, angle):
		kit.servo[armID].angle = angle
