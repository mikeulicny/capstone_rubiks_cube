from .face import Face

class Cube:		
	# Initializer
	def __init__(self, up, down, front, back, left, right):
		self.up = up
		self.down = down
		self.front = front
		self.back = back
		self.left = left
		self.right = right	
		
	def flip(self, faceAndDir):
	
		# 'i' stands for 'inverse' (i.e. 'counter-clockwise)
		
		# Define following flips:
		# flip('X')		# cube along X-axis clockwise
		# flip('Xi')	# cube along X-axis counter-clockwise
		# flip('Y')		# cube along Y-axis clockwise
		# flip('Yi')	# cube along Y-axis counter-clockwise
		# flip('Z')		# cube along Z-axis clockwise
		# flip('Zi')	# cube along Z-axis counter-clockwise
	
	def turn(self, faceAndDir):
		# Define following turns:
		# turn('U')		# up face clockwise
		# turn('Ui')	# up face counter-clockwise
		# turn('D')		# down face clockwise
		# turn('Di')	# down face counter-clockwise
		# turn('F')		# front face clockwise
		# turn('Fi')	# front face counter-clockwise
		# turn('B')		# back face clockwise
		# turn('Bi')	# back face counter-clockwise
		# turn('L')		# left face clockwise
		# turn('Li')	# left face counter-clockwise
		# turn('R')		# right face clockwise
		# turn('Ri')	# right face counter-clockwise