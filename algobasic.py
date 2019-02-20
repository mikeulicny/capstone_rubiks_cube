import numpy as np
from .face import Face
from .cube import Cube

class AlgoBasic:			
	# Initializer
	def __init__(self, cube):
		self.c = cube
			
	def solve(self):
		# Simplify attributes
		up = self.c.up
		down = self.c.down
		front = self.c.front
		back = self.c.back
		left = self.c.left
		right = self.c.right

		# Simplify methods
		flip = self.c.flip()
		turn = self.c.turn()
		
		# Get yellow edge on top
		if front.mc == 'y':
			flip('X')
		elif back.mc == 'y':
			flip('Xi')
		elif left.mc == 'y':
			flip('Z')
		elif right.mc == 'y':
			flip('Zi')
		elif down.mc == 'y':
			flip('X')
			flip('X')
	
		# While the 'daisy' isn't complete
		while not up.allEdges('w'):
			if front.mr == 'w':
				if up.mr != 'w':
					turn('R')
				elif up.bc !='w':
					turn('U')
					turn('R')
				elif 
				
# face.tl face.tc face.tr
# face.ml face.mc face.mr
# face.bl face.bc face.br

		








