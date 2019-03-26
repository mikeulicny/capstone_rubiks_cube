from adafruit_servokit import ServoKit

class Claw:

	def __init__(self, clawID, armID):
		# object elements
		self.clawID = clawID
		self.armID = armID
		self.kit = ServoKit(channels=16)
		# self.position

		# initialize claw to 90 deg (0 deg position)
		self.rotate(90)


	def openClaw(self):
		self.kit.servo[self.clawID].angle = 60

	def closeClaw(self):

		self.kit.servo[self.clawID].angle = 14

	def rotate(self, angle):
		self.kit.servo[self.armID].angle = angle

		# to be used to optimize movements
		# self.position = angle
