import numpy as np
from face import Face

class Cube:		
	# Initializer
	def __init__(self, up, down, front, back, left, right):
		self.up = up
		self.down = down
		self.front = front
		self.back = back
		self.left = left
		self.right = right
		
	def remapAll(self):
		self.up.remap()
		self.down.remap()
		self.front.remap()
		self.back.remap()
		self.left.remap()
		self.right.remap()
	
	def flip(self, dir):
		# 'i' stands for 'inverse' (i.e. 'counter-clockwise)
		# X-axis goes through the left and right faces (same dir as right)
		# Y-axis goes through the up and down faces (same dir as up)
		# Z-axis goes through the front and back faces (same dir as front)
		# example: 	flip('X') = flip whole cube along X-axis clockwise
		#			flip('Zi') = flip whole cube along Z-axis counter-clockwise
		
		# Define following whole-cube flips:
		# Regular (90 degree) flips
		# flip('X')
		# flip('Xi')
		# flip('Z')
		# flip('Zi')
		
		# Special composite (3 stage) flips (because of claw limitations)
		# flip('Y') = flip('Z') + flip('X') + flip('Zi')
		# flip('Yi') = flip('Z') + flip('Xi') + flip('Zi')
		
		# Special "180 degree" turns (for consistent code)
		# (The 2Y implementation is more efficient than 2 "flip('Y') calls)
		# flip('2X') = flip('X') + flip('X')
		# flip('2Y') = flip('Z') + flip('2X') + flip('Zi')
		# flip('2Z') = flip('Z') + flip('Z')		
		
		# flip('Y') and its variants 'Yi' and '2Y' would be more efficient
		# move-wise if they were instead represented by an internal re-mapping
		# of the faces (e.g. flip('Y') would actually just re-map the faces:
		# left = front, front = right, right = back, and back = left) and claws.
		# This would significantly cut down on the number of flips needed.
		
		print(dir)
	
	def turn(self, dir):
		
		# example: 	turn('F') = turn front face clockwise
		#			turn('Li') = turn left face counter-clockwise ('inverse')
		
		# Define following turns:
		# Regular (90 degree) turns
		# turn('F')
		# turn('Fi')
		# turn('B')
		# turn('Bi')
		# turn('L')
		# turn('Li')
		# turn('R')
		# turn('Ri')
		
		# Special composite (3 stage) turns (because of claw limitations)
		# turn('U')	= flip('Z') + turn('R') + flip('Zi')
		# turn('Ui') = flip('Z') + turn('Ri') + flip('Zi')
		# turn('D') = flip('Z') + turn('L') + flip('Zi')
		# turn('Di') = flip('Z') + turn('Li') + flip('Zi')
		
		# Special "180 degree" turns (for consistent code)
		# (The 2U implementation is more efficient than 2 "turn('U') calls)
		# turn('2F') = turn('F') + turn('F')
		# turn('2B') = turn('B') + turn('B') 
		# turn('2L') = turn('L') + turn('L') 
		# turn('2R') = turn('R') + turn('R')
		# turn('2U') = flip('Z') + turn('2R') + flip('Zi')
		# turn('2D') = flip('Z') + turn('2L') + flip('Zi')
		
		# Up turns could also be done more efficiently by remapping the faces,
		# however this would likely be rather complicated and doing so nuanced.
		
		print(dir)
		
		
		
		
		
		
		
		