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
		remapAll = self.c.remapAll
		
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
				
		# If white edge in top slice:
			# If it's already in the front, move it up
			elif front.tc == 'w':
				if up.mr != 'w':
					turn('F')
					turn('R')
				elif up.ml != 'w':
					turn('Fi')
					turn('Li')
				elif up.tc != 'w':
					turn('F')
					turn('U')
					turn('R')
			# If it's NOT in the front, move it there
			elif right.tc == 'w':
				flip('Y')
			elif left.tc == 'w':
				flip('Yi')
			elif back.tc == 'w':
				flip('2Y')
		
		# If white edge in bottom slice:
			# If it's already in the front, move it up
			elif front.bc == 'w':
				if up.bc != 'w':
					if up.mr != 'w':
						turn('Fi')
						turn('R')
					elif up.ml != 'w':
						turn('F')
						turn('Li')
					elif up.tc != 'w':
						turn('Fi')
						turn('U')
						turn('R')
				else:
					if up.mr != 'w':
						turn('U')
						turn('Fi')
						turn('Ui')
						turn('R')
					elif up.ml != 'w':
						turn('Ui')
						turn('F')
						turn('U')
						turn('Li')
					elif up.tc != 'w':
						turn('2U')
						turn('Fi')
						turn('Ui')
						turn('R')					
			# If it's NOT in the front, move it there
			elif right.bc == 'w':
				flip('Y')
			elif left.bc == 'w':
				flip('Yi')
			elif back.bc == 'w':
				flip('2Y')
		
		# If white edge on down face:
			# If it's already in the 'front', move it up
			elif down.bc == 'w':
				if up.bc != 'w':
					turn('2F')
				else:
					if up.mr != 'w':
						turn('U')
						turn('2F')
					elif up.ml != 'w':
						turn('Ui')
						turn('2F')
					elif up.tc != 'w':
						turn('2U')
						turn('2F')
						
			# Remap corner and edge groups after turns
				remapAll()
	
		#-------------------------------------
		# While the white cross isn't complete
		#-------------------------------------
		while not down.allEdges('w'):
			if up.bc == 'w' and front.mc == front.tc:
				turn('2F')
			if up.ml == 'w' and left.mc == left.tc:
				turn('2L')
			if up.tc == 'w' and back.mc == back.tc:
				turn('2B')
			if up.mr == 'w' and right.mc == right.tc:
				turn('2R')
			turn('U')
			# Remap corner and edge groups after turns
			remapAll()	
			
		#------------------------------------
		# While the white side isn't complete
		#------------------------------------
		while not down.isComplete():
			# TO BE WRITTEN
		
		
def Main():				
	# Test: yellow top center, green front center: R U L F B R U F U L B
	# Let's shoot for ~ 120 moves in general
	# ~100 moves for this particular cube
	# If a given turn takes 2 seconds, that's a goal of 4 minutes
	# If a given turn takes 1.5 seconds, that's a goal of 3 minutes
	# If a given turn takes 1 second, that's a goal of 2 minutes
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
	print('Test from solved: y @ up, g @ front: R U L F B R U F U L B')
	print(cube)
	input('Press enter to enter solutioning loop...')
	algo = AlgoBasic(cube)
	algo.solve()

# Calling Test
if __name__ == '__main__': 
    Main() 