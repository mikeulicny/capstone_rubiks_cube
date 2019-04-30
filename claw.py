from adafruit_servokit import ServoKit

class Claw:

	def __init__(self, clawID, armID):
		# object elements
		self.clawID = clawID
		self.armID = armID
		self.kit = ServoKit(channels=16)		
		
		'''MIN/MAX PWM FOR CLAWS'''
		self.kit.servo[0].set_pulse_width_range(700, 2300)	# FRONT
		self.kit.servo[2].set_pulse_width_range(700, 2300)	# RIGHT
		self.kit.servo[4].set_pulse_width_range(700, 2300)	# BACK
		self.kit.servo[6].set_pulse_width_range(700, 2300)	# LEFT
		
		'''MIN?MAX PWM FOR ARMS'''
		self.kit.servo[1].set_pulse_width_range(600, 2330)	# FRONT
		self.kit.servo[3].set_pulse_width_range(800, 2550)	# RIGHT
		self.kit.servo[5].set_pulse_width_range(775, 2550)	# BACK
		self.kit.servo[7].set_pulse_width_range(600, 2500)	# LEFT
		
		# self.position

		# initialize claw to 90 deg (0 deg position)
		self.rotate(90)


	def openClaw(self):
		if self.clawID == 0:
			angle = 70	
		if self.clawID == 2:
			angle = 65
		if self.clawID == 4:
			angle = 75
		if self.clawID == 6:
			angle = 75
		
		self.kit.servo[self.clawID].angle = angle


	def closeClaw(self):
		if self.clawID == 0:
			angle = 22
		if self.clawID == 2:
			angle = 22
		if self.clawID == 4:
			angle = 22
		if self.clawID == 6:
			angle = 22

		self.kit.servo[self.clawID].angle = angle

	def rotate(self, angle, overturn=True):
		# if overturn=True
			# use default turn value. This is for claw turns on the cube
		if overturn == False:
			# use "perfect" angles. This is for setting the claws to grip the cube
			if self.armID == 1:
				if angle == 0:
					angle = 15
				elif angle == 180:
					angle = 178
			
			elif self.armID == 3:
				if angle == 0:
					angle = 2
				elif angle == 180:
					angle = 165
			
			elif self.armID == 5:
				if angle == 0:
					angle = 3
				elif angle == 180:
					angle = 172
			
			elif self.armID == 15:
				if angle == 0:
					angle = 10
				elif angle == 180:
					angle = 178


		if self.armID == 1 and angle == 90:
			angle = 89
		if self.armID == 3 and angle == 90:
			angle = 74
		if self.armID == 5 and angle == 90:
			angle = 85
		if self.armID == 7 and angle == 90:
			angle = 92
		
		self.kit.servo[self.armID].angle = angle

		# to be used to optimize movements
		# self.position = angle
