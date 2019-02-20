# face.tl face.tc face.tr
# face.ml face.mc face.mr
# face.bl face.bc face.br

import numpy as np
from face import Face
from cube import Cube

class AlgoBasic:			
	# Initializer
	def __init__(self, cube):
		self.c = cube
		
	def solve(self):
		# Simplify attributes and methods
		up = self.c.up
		down = self.c.down
		front = self.c.front
		back = self.c.back
		left = self.c.left
		right = self.c.right
		flip = self.c.flip
		turn = self.c.turn
		
		#-----------------------
		# Get yellow edge on top
		#-----------------------
		if front.mc == 'y':
			flip('X')
		elif back.mc == 'y':
			flip('Xi')
		elif left.mc == 'y':
			flip('Z')
		elif right.mc == 'y':
			flip('Zi')
		elif down.mc == 'y':
			flip('2X')
	
		#---------------------------------
		# While the 'daisy' isn't complete
		#---------------------------------
		while not up.allEdges('w'):
		# If white edge in middle slice:
			# If it's already in the front, move it up
			if front.mr == 'w':
				if up.mr != 'w':
					turn('R')
				else:
					if up.bc != 'w':
						turn('Ui')
						turn('R')
					elif up.tc != 'w':
						turn('U')
						turn('R')
					else:
						turn('2U')
						turn('R')
			elif front.ml == 'w':
				if up.ml != 'w':
					turn('Li')
				else:
					if up.bc != 'w':
						turn('U')
						turn('Li')
					elif u.tc != 'w':
						turn('Ui')
						turn('Li')
					else:
						turn('2U')
						turn('Li')
			# If it's NOT in the front, move it there
			elif right.mr == 'w' or right.ml == 'w':
				flip('Y')
			elif left.mr == 'w' or left.ml == 'w':
				flip('Yi')
			elif back.mr == 'w' or back.ml == 'w':
				flip('2Y')


def Main():				
	# Test: yellow top, green front: R U L F B R U F U L B
	up = np.array([['o', 'b', 'b'],
		['r', 'y', 'b'],
		['o', 'o', 'b']])	
	front = np.array([['b', 'y', 'r'],
		['w', 'g', 'g'],
		['y', 'b', 'r']])
	left = np.array([['w', 'g', 'w'],
		['o', 'r', 'y'],
		['g', 'g', 'w']])
	down = np.array([['w', 'r', 'b'],
		['b', 'w', 'w'],
		['g', 'o', 'o']])
	back = np.array([['r', 'g', 'g'],
		['y', 'b', 'w'],
		['g', 'y', 'o']])
	right = np.array([['y', 'r', 'r'],
		['r', 'o', 'w'],
		['y', 'o', 'y']])

	up = Face(up)
	down = Face(down)
	front = Face(front)
	back = Face(back)
	left = Face(left)
	right = Face(right)

	cube = Cube(up, down, front, back, left, right)
	algo = AlgoBasic(cube)
	algo.solve()

# Calling Test
if __name__ == '__main__': 
    Main() 