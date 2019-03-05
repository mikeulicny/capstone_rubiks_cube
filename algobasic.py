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
		self.movelist = []
	
	# Function to determine if down slice is complete
	def downSliceComplete(self):
		# Simplify attributes
		down = self.c.down
		front = self.c.front
		back = self.c.back
		left = self.c.left
		right = self.c.right	
		
		out = True
		if (down.isComplete() == False or front.bc != front.br or 
			left.bc != left.br or back.bc != back.br or 
			right.bc != right.br):
			out = False	
		return out

	# Function to determine if middle layer is complete
	def midSliceComplete(self):
		# Simplify attributes
		front = self.c.front
		back = self.c.back
		left = self.c.left
		right = self.c.right
		
		out = False
		if (front.ml == front.mc == front.mr and 
			left.ml == left.mc == left.mr and 
			right.ml == right.mc == right.mr and
			back.ml == back.mc == back.mr):
			out = True
		return out
		
	# Expansion of cube flip method to include list appending
	def flip(self, dir):
		self.c.flip(dir)
		self.movelist.append(dir)
		
	# Expansion of cube turn method to include appending		
	def turn(self, dir):
		self.c.turn(dir)
		self.movelist.append(dir)
	
	# Function to optimize list by removing duplicates
	def trimList(self):
		ml = np.array(self.movelist)
		# 5 passes over the list should catch most un-optimized move combos
		for k in range (5):
			for i in range (0, len(ml)):
				j = i + 1
				try:
					if ml[i] == 'RM' or ml[j] == 'RM':
						continue
					# [X , X] -> [2X]
					elif ml[i] == ml[j] and ml[0] != '2':
						ml[j] = 'RM'
						ml[i] = '2' + ml[i][0] 
					# [X, Xi] or [Xi, X] -> RM both
					elif ml[i][0] == ml[j][0] and len(ml[i]) != len(ml[j]):
						ml[i] = 'RM'
						ml[j] = 'RM'
					# [X, 2X] or [Xi, 2X] -> [Xi] or [X], respectively
					elif len(ml[j]) == 2 and ml[i][0] == ml[j][1]:
						if len(ml[i]) == 1:
							ml[i] = ml[i] + 'i'
							ml[j] = 'RM'
						else:
							ml[i] = ml[i][0]
							ml[j] = 'RM'
					# [2X, X] or [2X, Xi] -> [Xi] or [X], respectively
					elif len(ml[i]) == 2 and ml[i][1] == ml[j][0]:
						if len(ml[j]) == 1:
							ml[i] = ml[j] + 'i'
							ml[j] = 'RM'
						else:
							ml[i] = ml[j][0]
							ml[j] = 'RM'
				except:
					pass	
		# New movelist without values marked 'RM'
		self.movelist = [move for move in ml.tolist() if move != 'RM']
	
	def solve(self):
		# Simplify attributes and methods
		up = self.c.up
		down = self.c.down
		front = self.c.front
		back = self.c.back
		left = self.c.left
		right = self.c.right
		flip = self.flip
		turn = self.turn
		downSliceComplete = self.downSliceComplete
		midSliceComplete = self.midSliceComplete
		
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
			if not down.allEdges('w'):
				turn('U')
				
		#------------------------------------
		# While the white side isn't complete
		#------------------------------------
		while not downSliceComplete():
		# If desired piece in 'good' position:
			if front.tl == 'w' and up.bl == front.mc:
				turn('Ui')
				turn('Li')
				turn('U')
				turn('L')
			elif front.tr == 'w' and up.br == front.mc:
				turn('Fi')
				turn('Ui')
				turn('F')
			elif up.bl == 'w' and front.tl == left.mc:
				turn('Li')
				turn('2U')
				turn('L')
				turn('U')
				turn('Li')
				turn('Ui')
				turn('L')
		# If desired piece in top slice at all:
			# Get it to the front
			elif right.tr == 'w' and up.tr == front.mc:
				turn('U')
			elif left.tr == 'w' and up.bl == front.mc:
				turn('Ui')
			elif back.tr == 'w' and up.tl == front.mc:
				turn('2U')
				
			elif right.tl == 'w' and up.br == front.mc:
				turn('U')
			elif left.tl == 'w' and up.tl == front.mc:
				turn('Ui')
			elif back.tl == 'w' and up.tr == front.mc:
				turn('2U')
			
			elif up.br == 'w' and front.tr == front.mc:
				turn('U')
			elif up.tl == 'w' and back.tr == front.mc:
				turn('Ui')
			elif up.tr == 'w' and right.tr == front.mc:
				turn('2U')
		
		# If white pieces remain on the front side:
			# Toss them to the top slice
			elif front.bl == 'w':
				turn('Li')
				turn('Ui')
				turn('L')
			elif front.br == 'w':
				turn('Fi')
				turn('Ui')
				turn('F')
		
		# If incorrect white piece on bottom:
			# Toss it to the top slice
			elif down.tl == 'w' and front.bl != front.mc:
				turn('Li')
				turn('Ui')
				turn('L')	
			elif down.tr == 'w' and front.br != front.mc:
				turn('Fi')
				turn('Ui')
				turn('F')
		
		# Otherwise this side is done, make next side front
			elif not downSliceComplete():
				flip('Y')

		#--------------------------------------
		# While the center slice isn't complete
		#--------------------------------------
		while not midSliceComplete():
		# If piece to drop in the front, drop it down
			if front.tc == front.mc and up.bc == left.mc:
				turn('Ui')
				turn('Li')
				turn('U')
				turn('L')
				turn('U')
				turn('F')
				turn('Ui')
				turn('Fi')
			elif front.tc == front.mc and up.bc == right.mc:
				turn('U')
				turn('R')
				turn('Ui')
				turn('Ri')
				turn('Ui')
				turn('Fi')
				turn('U')
				turn('F')

		# If desired piece in top slice at all:
			# Get it to the front
			elif right.tc == front.mc and up.mr != 'y':
				turn('U')
			elif left.tc == front.mc and up.ml != 'y':
				turn('Ui')
			elif back.tc == front.mc and up.tc != 'y':
				turn('2U')

		# If desired piece in top slice but flipped:
			# Keep flipping to avoid tons of wasted turns
			elif up.mr != 'y' and right.tc != 'y':
				flip('Y')
			elif up.ml != 'y' and left.tc != 'y':
				flip('Y')
			elif up.tc != 'y' and back.tc != 'y':
				flip('Y')
				
		# If incorrect piece is currently dropped, get it out
			elif front.mc != front.ml:
				turn('Ui')
				turn('Li')
				turn('U')
				turn('L')
				turn('U')
				turn('F')
				turn('Ui')
				turn('Fi')			
			elif front.mc != front.mr:
				turn('U')
				turn('R')
				turn('Ui')
				turn('Ri')
				turn('Ui')
				turn('Fi')
				turn('U')
				turn('F')					
		
		# Otherwise this side is 'done', make next side front
			elif not midSliceComplete():
				flip('Y')		

		#-------------------------------------------
		# While the top (yellow) cross isn't complete
		#-------------------------------------------
		while not up.allEdges('y'):
		
		
		
		# Optimize the list by removing superfluous/duplicate turns
		self.trimList()
	
def Main():				
	# Test: yellow top center, green front center: R U L F B R U F U L B
	# Let's shoot for ~ 120 moves in general
	# ~100 moves for this particular cube
	# If a given turn takes 2 seconds, that's a goal of 4 minutes
	# If a given turn takes 1.5 seconds, that's a goal of 3 minutes
	# If a given turn takes 1 second, that's a goal of 2 minutes

	# X Z X Z X Z
	# 1st image: Up (correct orientation)
	# 2nd image: Front (correct orientation)
	# 3rd image: Left (correct orientation)
	# 4th image: Down (needs to be rotated 90 degrees counter-clockwise)
	# 5th image: Back (needs to be rotated 90 degrees clockwise)
	# 6th image: Right (needs to be rotated 90 degrees clockwise)
	'''
	# Test cube 1:
	print('Test from solved: y @ up, g @ front: R U L F B R U F U L B')
	up = np.array([['o', 'b', 'b'],
		['r', 'y', 'b'],
		['o', 'o', 'b']])	
	front = np.array([['b', 'y', 'r'],
		['w', 'g', 'g'],
		['y', 'b', 'r']])
	left = np.array([['w', 'y', 'w'],
		['g', 'r', 'g'],
		['w', 'o', 'g']])
	down = np.array([['b', 'w', 'o'],
		['r', 'w', 'o'],
		['w', 'b', 'g']])
	back = np.array([['g', 'y', 'r'],
		['y', 'b', 'g'],
		['o', 'w', 'g']])
	right = np.array([['y', 'r', 'r'],
		['r', 'o', 'w'],
		['y', 'o', 'y']])
	'''
	# Test cube 2:
	print('Test from solved: o @ up, b @ front: U Li B R Fi L U B Fi Ui D')
	up = np.array([['r', 'y', 'g'],
		['g', 'o', 'r'],
		['b', 'y', 'o']])	
	front = np.array([['o', 'r', 'y'],
		['y', 'b', 'r'],
		['w', 'o', 'w']])
	left = np.array([['y', 'o', 'y'],
		['w', 'w', 'b'],
		['w', 'g', 'o']])
	down = np.array([['b', 'w', 'g'],
		['g', 'r', 'y'],
		['b', 'w', 'b']])
	back = np.array([['g', 'o', 'r'],
		['g', 'g', 'r'],
		['w', 'o', 'r']])
	right = np.array([['r', 'b', 'y'],
		['b', 'y', 'b'],
		['g', 'w', 'o']])	
	
	# Rotate arrays
	down = np.rot90(down, 1)
	back = np.rot90(back, 3)
	right = np.rot90(right, 3)

	# Instantiate faces
	up = Face(up)
	down = Face(down)
	front = Face(front)
	back = Face(back)
	left = Face(left)
	right = Face(right)

	# Instantiate cube
	cube = Cube(up, down, front, back, left, right)
	
	# input('Press Enter to solve...')
	algo = AlgoBasic(cube)
	algo.solve()

	print('After:\n')
	print(cube)
	print(algo.movelist)
	print('Current number of turns: ' + str(len(algo.movelist)))
	
# Calling Test
if __name__ == '__main__': 
    Main() 