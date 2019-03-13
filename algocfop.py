import numpy as np
import secrets
import re
import copy
from face import Face
from cube import Cube

class AlgoCFOP:			
	# Initializer
	def __init__(self, cube, test = 0):
		self.c = cube		
		self.movelist = []
		self.movenumber = 0
		self.test = test
		self.listLength = 0

	# Function to determine if bottom two slices are complete
	def firstTwoComplete(self):
		# Simplify attributes
		down = self.c.down
		front = self.c.front
		back = self.c.back
		left = self.c.left
		right = self.c.right	

		out = True
		if (down.isComplete() == False or 
			front.ml != front.mc or front.mr != front.mc or
			front.bl != front.mc or front.br != front.mc or		
			right.ml != right.mc or right.mr != right.mc or
			right.bl != right.mc or right.br != right.mc or
			back.ml != back.mc or back.mr != back.mc or
			back.bl != back.mc or back.br != back.mc or
			left.ml != left.mc or left.mr != left.mc or
			left.bl != left.mc or left.br != left.mc):
			out = False
		return out
		
	# Function to determine if cube is completely solved
	def cubeComplete(self):
		# Simplify attributes
		up = self.c.up
		down = self.c.down
		front = self.c.front
		back = self.c.back
		left = self.c.left
		right = self.c.right
		
		out = False
		if (front.isComplete() == True and back.isComplete() == True and
			left.isComplete() == True and right.isComplete() == True and
			up.isComplete() == True and down.isComplete() == True):
			out = True
		return out
		
	# Expansion of cube turn method to include list appending
	def turn(self, dir):
		self.c.turn(dir)
		self.movelist.append(dir)
		if self.test == 1:
			print(dir + ' (turn ' + str(self.movenumber) + '):')
			self.movenumber += 1
			print(self.c)		
			input('')
		
	# Function to optimize list by removing duplicates
	def trimList(self):
		
		chars = ['X','Y','Z','F','B','U','D','L','R']
		
		for i in range(5):
			for c in chars:
				ml = ' ' + ' '.join(self.movelist) + ' '
				s = ' '
				ci = c + 'i'
				c2 = '2' + c
				# [ c c ] or [ ci ci ] -> [ 2c ]
				ml = re.sub(s + c + s + c + s, s + c2 + s, ml)
				ml = re.sub(s + ci + s + ci + s, s + c2 + s, ml)
				# [ c ci ] or [ ci c ] -> [ ]
				ml = re.sub(s + c + s + ci + s, s, ml)
				ml = re.sub(s + ci + s + c + s, s, ml)
				# [ 2c c ] or [ 2c ci ] -> [ ci ] or [ c ], respectively				
				ml = re.sub(s + c2 + s + c + s, s + ci + s, ml)
				ml = re.sub(s + c2 + s + ci + s, s + c + s, ml)
				# [ c 2c ] or [ ci 2c ] -> [ ci ] or [ c ], respectively				
				ml = re.sub(s + c + s + c2 + s, s + ci + s, ml)
				ml = re.sub(s + ci + s + c2 + s, s + c + s, ml)
				# [ 2c 2c ] -> [ ]				
				ml = re.sub(s + c2 + s + c2 + s, s, ml)
					
				ml = re.split('\s+', ml)
				out = ml[1:-1]
				self.movelist = out

	# Function to randomize a cube (20 turns)
	def randomize(self):
		# Simplify attributes and methods
		turn = self.turn
		turn = self.turn

		# Random RNG
		goodRNG = secrets.SystemRandom()
		
		# Clear existing move list
		self.movelist = []
		
		# 20 random turns
		moves = ['U','Ui','D','Di','F','Fi','B','Bi','L','Li','R','Ri',
			'2U','2D','2F','2B','2L','2R']
		for i in range(20):
			randomTurn = goodRNG.randrange(0,18)
			turn(moves[randomTurn])
					
		# Optimize the list by removing superfluous/duplicate turns
		self.trimList()
	
	# Function to get a cube to a pre-determined configuration
	def followMoves(self):	
		L = len(self.movelist)
		for i in range(L):
			self.c.turn(self.movelist[i])
	
	# Function to solve a cube				
	def solve(self):		
			
		# Make a clean copy of the cube
		cleanCopy = copy.deepcopy(self.c)
		
		# List of initial moves for initial configuration
		moves = ['','X','Xi','Z','Zi','2X']
		
		# Initial assumptions regarding list length
		minListLength = 1000
		minList = []
		
		for i in range(6):
			# Reset cube to initial configuration
			if i > 0:
				self.c = copy.deepcopy(cleanCopy)
			
			# Simplify attributes and methods
			up = self.c.up
			down = self.c.down
			front = self.c.front
			back = self.c.back
			left = self.c.left
			right = self.c.right
			turn = self.turn
			firstTwoComplete = self.firstTwoComplete
			cubeComplete = self.cubeComplete	
			
			# Clear existing move list (except for initial permutation move)
			self.movelist = []	
			if i > 0:
				self.turn(moves[i])
			
			#---------------------------------
			# While the 'daisy' isn't complete
			#---------------------------------
			while not up.allEdges(down.mc):
			# If white edge in middle slice:
				# If it's already in the front, move it up
				if front.mr == down.mc:
					if up.mr != down.mc:
						turn('R')
					else:
						if up.bc != down.mc:
							turn('Xi')
							turn('Fi')
							turn('R')
							turn('X')
						elif up.tc != down.mc:
							turn('Xi')
							turn('F')
							turn('R')
							turn('X')
						else:
							turn('Xi')
							turn('2F')
							turn('R')
							turn('X')
				elif front.ml == down.mc:
					if up.ml != down.mc:
						turn('Li')
					else:
						if up.bc != down.mc:
							turn('Xi')
							turn('F')
							turn('Li')
							turn('X')
						elif up.tc != down.mc:
							turn('Xi')
							turn('Fi')
							turn('Li')
							turn('X')
						else:
							turn('Xi')
							turn('2F')
							turn('Li')
							turn('X')
				# If it's NOT in the front, move it there
				elif right.mr == down.mc or right.ml == down.mc:
					turn('Y')
				elif left.mr == down.mc or left.ml == down.mc:
					turn('Yi')
				elif back.mr == down.mc or back.ml == down.mc:
					turn('2Y')
					
			# If white edge in top slice:
				# If it's already in the front, move it up
				elif front.tc == down.mc:
					if up.mr != down.mc:
						turn('F')
						turn('R')
					elif up.ml != down.mc:
						turn('Fi')
						turn('Li')
					elif up.tc != down.mc:
						turn('F')
						turn('Xi')
						turn('F')
						turn('R')
						turn('X')
					elif up.bc != down.mc:
						turn('F')
						turn('Xi')
						turn('Fi')
						turn('R')
						turn('X')
						
				# If it's NOT in the front, move it there
				elif right.tc == down.mc:
					turn('Y')
				elif left.tc == down.mc:
					turn('Yi')
				elif back.tc == down.mc:
					turn('2Y')
			
			# If white edge in bottom slice:
				# If it's already in the front, move it up
				elif front.bc == down.mc:
					if up.bc != down.mc:
						if up.mr != down.mc:
							turn('Fi')
							turn('R')
						elif up.ml != down.mc:
							turn('F')
							turn('Li')
						elif up.tc != down.mc:
							turn('Fi')
							turn('Xi')
							turn('F')
							turn('R')
							turn('X')
						elif up.bc != down.mc:
							turn('Fi')
							turn('Xi')
							turn('Fi')
							turn('R')
							turn('X')
					else:
						if up.mr != down.mc:
							turn('Z')
							turn('R')
							turn('Fi')
							turn('Ri')
							turn('Zi')
							turn('R')
						elif up.ml != down.mc:
							turn('Z')
							turn('Ri')
							turn('F')
							turn('R')
							turn('Zi')
							turn('Li')
						elif up.tc != down.mc:
							turn('Z')
							turn('2R')
							turn('Fi')
							turn('Ri')
							turn('Zi')
							turn('R')
				# If it's NOT in the front, move it there
				elif right.bc == down.mc:
					turn('Y')
				elif left.bc == down.mc:
					turn('Yi')
				elif back.bc == down.mc:
					turn('2Y')
			
			# If white edge on down face:
				# If it's already in the 'front', move it up
				elif down.tc == down.mc:
					if up.bc != down.mc:
						turn('2F')
					else:
						if up.mr != down.mc:
							turn('Z')
							turn('R')
							turn('2F')
							turn('Zi')
						elif up.ml != down.mc:
							turn('Z')
							turn('Ri')
							turn('2F')
							turn('Zi')
						elif up.tc != down.mc:
							turn('Z')
							turn('2R')
							turn('2F')
							turn('Zi')
				# If it's NOT in the front, move it there
				elif down.mr == down.mc:
					turn('Y')
				elif down.ml == down.mc:
					turn('Yi')
				elif down.bc == down.mc:
					turn('2Y')

			#-------------------------------------
			# While the white cross isn't complete
			#-------------------------------------
			while not down.allEdges(down.mc):
				if up.bc == down.mc and front.mc == front.tc:
					turn('2F')
				if up.ml == down.mc and left.mc == left.tc:
					turn('2L')
				if up.tc == down.mc and back.mc == back.tc:
					turn('2B')
				if up.mr == down.mc and right.mc == right.tc:
					turn('2R')
				if not down.allEdges(down.mc):
					turn('Z')
					turn('R')
					turn('Zi')
					
			#-------------------------------------------
			# While the first two layers aren't complete
			#-------------------------------------------
			while not firstTwoComplete():
				# If desired corner is in top slice get it to front spot
				# If white side of corner is facing up
				if up.tr == down.mc and back.tl == front.mc and right.tr == right.mc:
					turn('Z')
					turn('R')
					turn('Zi')
				elif up.bl == down.mc and front.tl == front.mc and left.tr == right.mc:
					turn('Z')
					turn('Ri')
					turn('Zi')
				elif up.tl == down.mc and left.tl == front.mc and back.tr == right.mc:
					turn('Z')
					turn('2R')
					turn('Zi')
					
				# If white side of corner is facing left
				elif right.tr == down.mc and up.tr == front.mc and back.tl == right.mc:
					turn('Z')
					turn('R')
					turn('Zi')			
				elif left.tr == down.mc and up.bl == front.mc and front.tl == right.mc:
					turn('Z')
					turn('Ri')
					turn('Zi')
				elif back.tr == down.mc and up.tl == front.mc and left.tl == right.mc:
					turn('Z')
					turn('2R')
					turn('Zi')
			
				# If white side of corner is facing right
				elif back.tl == down.mc and right.tr == front.mc and up.tr == right.mc:
					turn('Z')
					turn('R')
					turn('Zi')
				elif front.tl == down.mc and left.tr == front.mc and up.bl == right.mc:
					turn('Z')
					turn('Ri')
					turn('Zi')
				elif left.tl == down.mc and back.tr == front.mc and up.tl == right.mc:
					turn('Z')
					turn('2R')
					turn('Zi')
				
			# If corner is above correct spot (i.e. in top slice)
				# If white side of corner is facing up (top, 10 cases)
				elif up.br == down.mc and front.tr == right.mc and right.tl == front.mc:
					if front.mr == front.mc and right.ml == right.mc:
						if self.test == 1:
							print('Move sequence 1')
						turn('Xi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('X')
					elif front.mr == right.mc and right.ml == front.mc:
						if self.test == 1:
							print('Move sequence 2')
						turn('Xi')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('Zi')
						turn('F')
						turn('Ri')
						turn('F')
						turn('R')
						turn('X')
					elif front.tc == right.mc and up.bc == front.mc:
						if self.test == 1:
							print('Move sequence 3')
						turn('Xi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('2F')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Fi')			
						turn('R')
						turn('F')
						turn('Ri')
						turn('X')
					elif right.tc == front.mc and up.mr == right.mc:
						if self.test == 1:
							print('Move sequence 4')
						turn('Yi')
						turn('Xi')					
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('2F')			
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')					
						turn('Ri')
						turn('Fi')
						turn('R')					
						turn('X')			
					elif left.tc == right.mc and up.ml == front.mc:
						if self.test == 1:
							print('Move sequence 5')		
						turn('Xi')					
						turn('2F')
						turn('R')
						turn('F')
						turn('Ri')					
						turn('F')
						turn('R')
						turn('Fi')
						turn('Ri')					
						turn('X')					
					elif back.tc == front.mc and up.tc == right.mc:
						if self.test == 1:
							print('Move sequence 6')
						turn('Z')					
						turn('2R')
						turn('Fi')
						turn('Ri')
						turn('F')					
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')					
						turn('Zi')					
					elif back.tc == right.mc and up.tc == front.mc:
						if self.test == 1:
							print('Move sequence 7')
						turn('Xi')					
						turn('F')
						turn('R')
						turn('2F')
						turn('Ri')					
						turn('F')
						turn('R')
						turn('Fi')
						turn('Ri')					
						turn('X')					
					elif left.tc == front.mc and up.ml == right.mc:
						if self.test == 1:
							print('Move sequence 8')				
						turn('Z')					
						turn('Ri')
						turn('Fi')
						turn('2R')
						turn('F')					
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Zi')								
					elif right.tc == right.mc and up.mr == front.mc:
						if self.test == 1:
							print('Move sequence 9')
						turn('Xi')					
						turn('R')
						turn('2F')
						turn('Ri')					
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')					
						turn('X')				
					elif front.tc == front.mc and up.bc == right.mc:
						if self.test == 1:
							print('Move sequence 10')	
						turn('Z')					
						turn('Fi')
						turn('2R')
						turn('F')					
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('F')					
						turn('Zi')
						
					# If edge not in top layer
					elif front.ml == front.mc and left.mr == right.mc:
						if self.test == 1:
							print('Move sequence 01')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif front.ml == right.mc and left.mr == front.mc:
						if self.test == 1:
							print('Move sequence 02')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif back.ml == front.mc and right.mr == right.mc:
						if self.test == 1:
							print('Move sequence 03')
						turn('Z')
						turn('B')
						turn('R')
						turn('Bi')
						turn('Zi')	
					elif back.ml == right.mc and right.mr == front.mc:
						if self.test == 1:
							print('Move sequence 04')
						turn('Z')
						turn('B')
						turn('R')
						turn('Bi')
						turn('Zi')
					elif left.ml == front.mc and back.mr == right.mc:
						if self.test == 1:
							print('Move sequence 05')
						turn('Zi')
						turn('Bi')
						turn('Li')
						turn('B')
						turn('Z')				
					elif left.ml == right.mc and back.mr == front.mc:
						if self.test == 1:
							print('Move sequence 06')
						turn('Zi')
						turn('Bi')
						turn('Li')
						turn('B')
						turn('Z')	
						
					else:
						if self.test == 1:
							print('Loop 1')
						turn('Y')

				# If white side of corner is facing right (top, 10 cases)
				elif up.br == right.mc and front.tr == front.mc and right.tl == down.mc:
					if back.tc == right.mc and up.tc == front.mc:
						if self.test == 1:
							print('Move sequence 11')
						turn('Xi')					
						turn('R')
						turn('F')
						turn('Ri')					
						turn('X')				
					elif front.tc == front.mc and up.bc == right.mc:
						if self.test == 1:
							print('Move sequence 12')
						turn('Z')					
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')					
						turn('Zi')				
					elif front.mr == front.mc and right.ml == right.mc:
						if self.test == 1:
							print('Move sequence 13')
						turn('Z')					
						turn('R')
						turn('Fi')
						turn('R')
						turn('F')					
						turn('R')
						turn('Fi')
						turn('2R')
						turn('F')					
						turn('Zi')					
					elif front.mr == right.mc and right.ml == front.mc:
						if self.test == 1:
							print('Move sequence 14')
						turn('Z')					
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('F')					
						turn('X')
						turn('Ri')
						turn('F')
						turn('R')
						turn('Fi')					
						turn('Zi')				
					elif right.tc == front.mc and up.mr == right.mc:
						if self.test == 1:
							print('Move sequence 15')
						turn('Xi')					
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('F')					
						turn('Zi')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')					
						turn('X')					
					elif back.tc == front.mc and up.br == right.mc:
						if self.test == 1:
							print('Move sequence 16')
						turn('Z')					
						turn('R')
						turn('Fi')
						turn('2R')
						turn('F')					
						turn('R')
						turn('Fi')
						turn('2R')
						turn('F')					
						turn('Zi')
					elif left.tc == front.mc and up.ml == right.mc:
						if self.test == 1:
							print('Move sequence 17')
						turn('Z')					
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('F')					
						turn('R')
						turn('Fi')
						turn('2R')
						turn('F')					
						turn('Zi')				
					elif right.tc == right.mc and up.mr == front.mc:
						if self.test == 1:
							print('Move sequence 18')
						turn('Xi')					
						turn('Fi')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('F')					
						turn('R')
						turn('F')
						turn('Ri')					
						turn('X')				
					elif left.tc == right.mc and up.ml == front.mc:
						if self.test == 1:
							print('Move sequence 19')
						turn('Xi')					
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('F')					
						turn('R')
						turn('F')
						turn('Ri')
						turn('X')
					elif front.tc == right.mc and up.bc == front.mc:
						if self.test == 1:
							print('Move sequence 20')
						turn('Z')
						turn('R')
						turn('Fi')
						turn('2R')
						turn('F')
						turn('Ri')
						turn('Zi')
						turn('Xi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('X')
						
					# If edge not in top layer
					elif front.ml == front.mc and left.mr == right.mc:
						if self.test == 1:
							print('Move sequence 01')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif front.ml == right.mc and left.mr == front.mc:
						if self.test == 1:
							print('Move sequence 02')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif back.ml == front.mc and right.mr == right.mc:
						if self.test == 1:
							print('Move sequence 03')
						turn('Z')
						turn('B')
						turn('R')
						turn('Bi')
						turn('Zi')	
					elif back.ml == right.mc and right.mr == front.mc:
						if self.test == 1:
							print('Move sequence 04')
						turn('Z')
						turn('B')
						turn('R')
						turn('Bi')
						turn('Zi')
					elif left.ml == front.mc and back.mr == right.mc:
						if self.test == 1:
							print('Move sequence 05')
						turn('Zi')
						turn('Bi')
						turn('Li')
						turn('B')
						turn('Z')				
					elif left.ml == right.mc and back.mr == front.mc:
						if self.test == 1:
							print('Move sequence 06')
						turn('Zi')
						turn('Bi')
						turn('Li')
						turn('B')
						turn('Z')	
						
					else:
						if self.test == 1:
							print('Loop 2')
						turn('Y')
						
				# If white side of corner is facing front (top, 10 cases)
				elif up.br == front.mc and front.tr == down.mc and right.tl == right.mc:
					if left.tc == front.mc and up.ml == right.mc:
						if self.test == 1:
							print('Move sequence 21')
						turn('Z')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('Zi')
					elif right.tc == right.mc and up.mr == front.mc:
						if self.test == 1:
							print('Move sequence 22')
						turn('Xi')
						turn('F')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('X')
					elif front.mr == front.mc and right.ml == right.mc:
						if self.test == 1:
							print('Move sequence 23')
						turn('Xi')
						turn('Fi')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('2F')
						turn('Ri')
						turn('X')
					elif front.mr == right.mc and right.ml == front.mc:
						if self.test == 1:
							print('Move sequence 24')
						turn('Xi')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Zi')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('X')
					elif front.tc == right.mc and up.bc == front.mc:
						if self.test == 1:
							print('Move sequence 25')
						turn('Z')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('X')
						turn('Ri')
						turn('F')
						turn('R')
						turn('Fi')
						turn('Zi')
					elif left.tc == right.mc and up.ml == front.mc:
						if self.test == 1:
							print('Move sequence 26')
						turn('Xi')
						turn('Fi')
						turn('R')
						turn('2F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('2F')
						turn('Ri')
						turn('X')
					elif back.tc == right.mc and up.tc == front.mc:
						if self.test == 1:
							print('Move sequence 27')
						turn('Xi')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('2F')
						turn('Ri')
						turn('X')
					elif front.tc == front.mc and up.bc == right.mc:
						if self.test == 1:
							print('Move sequence 28')
						turn('Z')
						turn('R')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('Zi')
					elif back.tc == front.mc and up.tc == right.mc:
						if self.test == 1:
							print('Move sequence 29')
						turn('Z')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('Zi')
					elif right.tc == front.mc and up.mr == right.mc:
						if self.test == 1:
							print('Move sequence 30')
						turn('Xi')
						turn('Fi')
						turn('R')
						turn('2F')
						turn('Ri')
						turn('F')
						turn('X')
						turn('Z')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('Zi')
						
					# If edge not in top layer
					elif front.ml == front.mc and left.mr == right.mc:
						if self.test == 1:
							print('Move sequence 01')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif front.ml == right.mc and left.mr == front.mc:
						if self.test == 1:
							print('Move sequence 02')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif back.ml == front.mc and right.mr == right.mc:
						if self.test == 1:
							print('Move sequence 03')
						turn('Z')
						turn('B')
						turn('R')
						turn('Bi')
						turn('Zi')	
					elif back.ml == right.mc and right.mr == front.mc:
						if self.test == 1:
							print('Move sequence 04')
						turn('Z')
						turn('B')
						turn('R')
						turn('Bi')
						turn('Zi')
					elif left.ml == front.mc and back.mr == right.mc:
						if self.test == 1:
							print('Move sequence 05')
						turn('Zi')
						turn('Bi')
						turn('Li')
						turn('B')
						turn('Z')				
					elif left.ml == right.mc and back.mr == front.mc:
						if self.test == 1:
							print('Move sequence 06')
						turn('Zi')
						turn('Bi')
						turn('Li')
						turn('B')
						turn('Z')	
					else:
						if self.test == 1:
							print('Loop 3')	
						turn('Y')

				# If white side of corner is facing right (bottom layer, 4 cases)
				elif front.br == right.mc and down.tr == front.mc and right.bl == down.mc:
					if front.tc == front.mc and up.bc == right.mc:
						if self.test == 1:
							print('Move sequence 31')
						turn('Z')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Zi')
					elif right.tc == right.mc and up.mr == front.mc:
						if self.test == 1:
							print('Move sequence 32')
						turn('Xi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('X')
					elif front.mr == front.mc and right.ml == right.mc:
						if self.test == 1:
							print('Move sequence 33')
						turn('Xi')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('R')
						turn('2F')
						turn('Ri')
						turn('F')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('X')
					elif front.mr == right.mc and right.ml == front.mc:
						if self.test == 1:
							print('Move sequence 34')
						turn('Xi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('Zi')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('X')
					
					# If edge in incorrect spot on top
					elif back.tc == right.mc and up.tc == front.mc:
						turn('Z')
						turn('R')
						turn('Zi')
					elif front.tc == right.mc and up.bc == front.mc:
						turn('Z')
						turn('Ri')
						turn('Zi')
					elif left.tc == right.mc and up.ml == front.mc:
						turn('Z')
						turn('2R')
						turn('Zi')
					elif right.tc == front.mc and up.mr == right.mc:
						turn('Z')
						turn('R')
						turn('Zi')
					elif left.tc == front.mc and up.ml == right.mc:
						turn('Z')
						turn('Ri')
						turn('Zi')
					elif back.tc == front.mc and up.tc == right.mc:
						turn('Z')
						turn('2R')
						turn('Zi')	

					# If edge not in top layer
					elif front.ml == front.mc and left.mr == right.mc:
						if self.test == 1:
							print('Move sequence 01')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif front.ml == right.mc and left.mr == front.mc:
						if self.test == 1:
							print('Move sequence 02')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif back.ml == front.mc and right.mr == right.mc:
						if self.test == 1:
							print('Move sequence 03')
						turn('Z')
						turn('B')
						turn('R')
						turn('Bi')
						turn('Zi')	
					elif back.ml == right.mc and right.mr == front.mc:
						if self.test == 1:
							print('Move sequence 04')
						turn('Z')
						turn('B')
						turn('R')
						turn('Bi')
						turn('Zi')
					elif left.ml == front.mc and back.mr == right.mc:
						if self.test == 1:
							print('Move sequence 05')
						turn('Zi')
						turn('Bi')
						turn('Li')
						turn('B')
						turn('Z')				
					elif left.ml == right.mc and back.mr == front.mc:
						if self.test == 1:
							print('Move sequence 06')
						turn('Zi')
						turn('Bi')
						turn('Li')
						turn('B')
						turn('Z')							
					else:
						if self.test == 1:
							print('Loop 4')	
						turn('Y')
		
				# If white side of corner is facing front (bottom layer, 4 cases)
				elif front.br == down.mc and down.tr == right.mc and right.bl == front.mc:
					if right.tc == right.mc and up.mr == front.mc:
						if self.test == 1:
							print('Move sequence 35')
						turn('Xi')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('X')
					elif front.tc == front.mc and up.bc == right.mc:
						if self.test == 1:
							print('Move sequence 36')
						turn('Z')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('Zi')
					elif front.mr == front.mc and right.ml == right.mc:
						if self.test == 1:
							print('Move sequence 37')
						turn('Xi')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('2F')
						turn('Ri')
						turn('X')
					elif front.mr == right.mc and right.ml == front.mc:
						if self.test == 1:
							print('Move sequence 38')
						turn('Xi')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('Zi')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('X')
						
					# If edge in incorrect spot on top
					elif back.tc == right.mc and up.tc == front.mc:
						turn('Z')
						turn('R')
						turn('Zi')
					elif front.tc == right.mc and up.bc == front.mc:
						turn('Z')
						turn('Ri')
						turn('Zi')
					elif left.tc == right.mc and up.ml == front.mc:
						turn('Z')
						turn('2R')
						turn('Zi')
					elif right.tc == front.mc and up.mr == right.mc:
						turn('Z')
						turn('R')
						turn('Zi')
					elif left.tc == front.mc and up.ml == right.mc:
						turn('Z')
						turn('Ri')
						turn('Zi')
					elif back.tc == front.mc and up.tc == right.mc:
						turn('Z')
						turn('2R')
						turn('Zi')
						
					# If edge not in top layer
					elif front.ml == front.mc and left.mr == right.mc:
						if self.test == 1:
							print('Move sequence 01')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif front.ml == right.mc and left.mr == front.mc:
						if self.test == 1:
							print('Move sequence 02')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif back.ml == front.mc and right.mr == right.mc:
						if self.test == 1:
							print('Move sequence 03')
						turn('Z')
						turn('B')
						turn('R')
						turn('Bi')
						turn('Zi')	
					elif back.ml == right.mc and right.mr == front.mc:
						if self.test == 1:
							print('Move sequence 04')
						turn('Z')
						turn('B')
						turn('R')
						turn('Bi')
						turn('Zi')
					elif left.ml == front.mc and back.mr == right.mc:
						if self.test == 1:
							print('Move sequence 05')
						turn('Zi')
						turn('Bi')
						turn('Li')
						turn('B')
						turn('Z')				
					elif left.ml == right.mc and back.mr == front.mc:
						if self.test == 1:
							print('Move sequence 06')
						turn('Zi')
						turn('Bi')
						turn('Li')
						turn('B')
						turn('Z')	
					else:
						if self.test == 1:
							print('Loop 5')	
						turn('Y')
				
				# If white corner already correct (3 cases)
				elif front.br == front.mc and down.tr == down.mc and right.bl == right.mc:
					if front.tc == front.mc and up.bc == right.mc:
						if self.test == 1:
							print('Move sequence 39')
						turn('Xi')
						turn('F')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('X')
						turn('Z')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Zi')
					elif right.tc == right.mc and up.mr == front.mc:
						if self.test == 1:
							print('Move sequence 40')
						turn('Z')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Zi')
						turn('Xi')
						turn('F')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('X')
					elif front.mr == right.mc and right.ml == front.mc:
						if self.test == 1:
							print('Move sequence 41')
						turn('Xi')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('Zi')
						turn('F')
						turn('Ri')
						turn('2F')
						turn('R')
						turn('F')
						turn('Ri')
						turn('2F')
						turn('R')
						turn('X')
						
					# If edge in incorrect spot on top
					elif back.tc == right.mc and up.tc == front.mc:
						turn('Z')
						turn('R')
						turn('Zi')
					elif front.tc == right.mc and up.bc == front.mc:
						turn('Z')
						turn('Ri')
						turn('Zi')
					elif left.tc == right.mc and up.ml == front.mc:
						turn('Z')
						turn('2R')
						turn('Zi')
					elif right.tc == front.mc and up.mr == right.mc:
						turn('Z')
						turn('R')
						turn('Zi')
					elif left.tc == front.mc and up.ml == right.mc:
						turn('Z')
						turn('Ri')
						turn('Zi')
					elif back.tc == front.mc and up.tc == right.mc:
						turn('Z')
						turn('2R')
						turn('Zi')

					# If edge not in top layer
					elif front.ml == front.mc and left.mr == right.mc:
						if self.test == 1:
							print('Move sequence 01')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif front.ml == right.mc and left.mr == front.mc:
						if self.test == 1:
							print('Move sequence 02')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif back.ml == front.mc and right.mr == right.mc:
						if self.test == 1:
							print('Move sequence 03')
						turn('Z')
						turn('B')
						turn('R')
						turn('Bi')
						turn('Zi')	
					elif back.ml == right.mc and right.mr == front.mc:
						if self.test == 1:
							print('Move sequence 04')
						turn('Z')
						turn('B')
						turn('R')
						turn('Bi')
						turn('Zi')
					elif left.ml == front.mc and back.mr == right.mc:
						if self.test == 1:
							print('Move sequence 05')
						turn('Zi')
						turn('Bi')
						turn('Li')
						turn('B')
						turn('Z')				
					elif left.ml == right.mc and back.mr == front.mc:
						if self.test == 1:
							print('Move sequence 06')
						turn('Zi')
						turn('Bi')
						turn('Li')
						turn('B')
						turn('Z')	
						
				# If white pieces remain on the front side:
					# Toss them to the top slice
					elif front.bl == down.mc:
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('X')
					elif front.br == down.mc:
						turn('Z')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('Zi')		
						
					# Otherwise
					else:
						if self.test == 1:
							print('Loop 6')	
						turn('Y')
						
			# If white pieces remain on the front side:
				# Toss them to the top slice
				elif front.bl == down.mc:
					turn('Xi')
					turn('Li')
					turn('Fi')
					turn('L')
					turn('X')
				elif front.br == down.mc:
					turn('Z')
					turn('Fi')
					turn('Ri')
					turn('F')
					turn('Zi')	
					
			# If incorrect white corners on bottom:
				# Toss it to the top slice
				elif down.tr == down.mc and front.br != front.mc:
					if self.test == 1:
						print('Move sequence 42')
					turn('Z')
					turn('Fi')
					turn('Ri')
					turn('F')
					turn('Zi') 
		
			# Otherwise, this side is done, move to next one
				else:
					if self.test == 1:
						print('Loop outer')
					turn('Y')	
					
			#-------------------------------------
			# While the yellow side isn't complete
			#-------------------------------------
			while not up.isComplete():
			# If dot (8 cases)
				if (left.tl == up.mc and left.tc == up.mc and
					left.tr == up.mc and front.tc == up.mc and 
					back.tc == up.mc and right.tl == up.mc and
					right.tc == up.mc and right.tr == up.mc):
					if self.test == 1:
						print('OLL 1')
					turn('R')
					turn('Z')
					turn('R')
					turn('Zi')
					turn('Bi')
					turn('Xi')
					turn('R')
					turn('Z')
					turn('R')
					turn('Zi')
					turn('2X')
					turn('2R')
					turn('Xi')
					turn('Z')
					turn('Ri')
					turn('Zi')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
					
				elif (left.tl == up.mc and left.tc == up.mc and
					front.tl == up.mc and front.tc == up.mc and
					front.tr == up.mc and back.tc == up.mc and
					right.tc == up.mc and right.tr == up.mc):
					if self.test == 1:
						print('OLL 2')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
					turn('Z')
					turn('2R')
					turn('Zi')	
					turn('Ri')
					turn('F')
					turn('R')
					turn('Yi')
					turn('2R')
					turn('Z')
					turn('2R')
					turn('Zi')	
					turn('R')
					
				elif (left.tc == up.mc and left.tr == up.mc and
					front.tc == up.mc and back.tc == up.mc and
					back.tr == up.mc and right.tc == up.mc and
					right.tr == up.mc and up.br == up.mc):
					if self.test == 1:
						print('OLL 3')
					turn('Y')
					turn('Li')
					turn('2R')
					turn('B')
					turn('Ri')
					turn('B')
					turn('L')
					turn('Z')
					turn('2R')
					turn('Zi')	
					turn('Li')
					turn('B')
					turn('X')
					turn('L')
					turn('Ri')
					turn('Xi')
				
				elif (left.tl == up.mc and left.tc == up.mc and
					front.tl == up.mc and front.tc == up.mc and 
					back.tc == up.mc and right.tl == up.mc and 
					right.tc == up.mc and up.tr == up.mc):
					if self.test == 1:
						print('OLL 4')		
					turn('Xi')
					turn('Ri')
					turn('2F')
					turn('X')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
					turn('Z')
					turn('Ri')
					turn('Fi')
					turn('Ri')
					turn('F')
					turn('Ri')
					turn('X')
					turn('F')
					turn('Zi')
				
				elif (left.tc == up.mc and left.tr == up.mc and
					front.tc == up.mc and back.tl == up.mc and
					back.tc == up.mc and right.tc == up.mc and
					up.tl == up.mc and up.br == up.mc):
					if self.test == 1:
						print('OLL 5')	
					turn('Xi')
					turn('R')
					turn('F')
					turn('Ri')
					turn('F')
					turn('X')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
					turn('Z')
					turn('2R')
					turn('Zi')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
					
				elif (left.tc == up.mc and front.tc == up.mc and
					back.tc == up.mc and right.tc == up.mc and
					up.tl == up.mc and up.tr == up.mc and
					up.bl == up.mc and up.br == up.mc):
					if self.test == 1:
						print('OLL 6')
					turn('X')
					turn('L')
					turn('Ri')
					turn('Xi')
					turn('2F')
					turn('Li')
					turn('R')
					turn('Xi')
					turn('2F')
					turn('2X')
					turn('L')
					turn('Ri')
					turn('Xi')
					turn('F')
					turn('Li')
					turn('R')				
					turn('Xi')
					turn('2F')					
					turn('2X')
					turn('L')
					turn('Ri')					
					turn('Xi')
					turn('2F')
					turn('Li')
					turn('R')				

				elif (left.tc == up.mc and left.tr == up.mc and
					front.tc == up.mc and back.tc == up.mc and
					right.tl == up.mc and right.tc == up.mc and
					up.tl == up.mc and up.tr == up.mc):
					if self.test == 1:
						print('OLL 7')
					turn('Ri')
					turn('Z')
					turn('2R')
					turn('Zi')
					turn('F')
					turn('Xi')
					turn('R')
					turn('F')
					turn('Ri')
					turn('Fi')
					turn('X')
					turn('Yi')
					turn('2R')
					turn('Xi')
					turn('2F')
					turn('R')
					turn('Z')
					turn('R')
					turn('Zi')	
					turn('X')
					
				elif (left.tc == up.mc and front.tc == up.mc and
					back.tl == up.mc and back.tc == up.mc and 
					back.tr == up.mc and right.tc == up.mc and
					up.bl == up.mc and up.br == up.mc):
					if self.test == 1:
						print('OLL 8')			
					turn('F')					
					turn('Xi')
					turn('R')				
					turn('F')					
					turn('Ri')				
					turn('F')					
					turn('X')					
					turn('Yi')					
					turn('Ri')					
					turn('Z')
					turn('2R')
					turn('Zi')				
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
			
			# If line (4 cases)
				elif (left.tc == up.mc and front.tl == up.mc and
					back.tr == up.mc and right.tl == up.mc and
					right.tc == up.mc and right.tr == up.mc and
					up.tc == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 9')		
					turn('Ri')					
					turn('Z')
					turn('Ri')
					turn('Zi')					
					turn('Y')					
					turn('Li')					
					turn('Z')
					turn('R')
					turn('Zi')					
					turn('Li')					
					turn('Yi')					
					turn('L')					
					turn('F')					
					turn('Li')					
					turn('F')				
					turn('R')
			
				elif (left.tl == up.mc and left.tc == up.mc and
					left.tr == up.mc and right.tl == up.mc and
					right.tc == up.mc and right.tr  == up.mc and
					up.tc == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 10')		
					turn('Xi')
					turn('R')
					turn('Fi')
					turn('Z')
					turn('2R')
					turn('B')
					turn('Ri')
					turn('2F')
					turn('R')
					turn('Bi')
					turn('2R')
					turn('Zi')
					turn('F')
					turn('Ri')
					turn('X')
				
				elif (front.tl == up.mc and front.tc == up.mc and
					back.tr == up.mc and back.tc == up.mc and
					right.tl == up.mc and right.tr == up.mc and
					up.ml == up.mc and up.mr == up.mc):
					if self.test == 1:
						print('OLL 11')		
					turn('F')
					turn('Xi')
					turn('F')
					turn('R')
					turn('Fi')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
					turn('Ri')
					turn('X')
					turn('Fi')
				
				elif (left.tl == up.mc and left.tr == up.mc and
					front.tc == up.mc and back.tc == up.mc and
					right.tl == up.mc and right.tr == up.mc and
					up.ml == up.mc and up.mr == up.mc):
					if self.test == 1:
						print('OLL 12')	
					turn('Li')
					turn('Bi')
					turn('L')
					turn('Xi')
					turn('Fi')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
					turn('Ri')
					turn('F')
					turn('R')
					turn('X')			
					turn('Li')
					turn('B')
					turn('L')
					
			# If cross (7 cases)
				elif (front.tl == up.mc and back.tr == up.mc and
					right.tl == up.mc and right.tr == up.mc and
					up.tc == up.mc and up.bc == up.mc and
					up.ml == up.mc and up.mr == up.mc):
					if self.test == 1:
						print('OLL 12')	
					turn('Xi')
					turn('L')
					turn('Fi')
					turn('Ri')
					turn('F')
					turn('Li')
					turn('F')
					turn('R')
					turn('F')
					turn('Ri')
					turn('F')
					turn('R')
					turn('X')
				
				elif (left.tl == up.mc and left.tr == up.mc and
					right.tl == up.mc and right.tr == up.mc and
					up.tc == up.mc and up.bc == up.mc and
					up.ml == up.mc and up.mr == up.mc):					
					if self.test == 1:
						print('OLL 13')
					turn('Xi')
					turn('R')
					turn('F')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
					turn('Ri')
					turn('F')
					turn('R')
					turn('2F')
					turn('Ri')
					turn('X')
				
				elif (left.tl == up.mc and front.tl == up.mc and
					back.tl == up.mc and up.bc == up.mc and
					up.tc == up.mc and up.bc == up.mc and
					up.ml == up.mc and up.mr == up.mc):					
					if self.test == 1:
						print('OLL 14')
					turn('Xi')
					turn('Li')
					turn('F')
					turn('R')
					turn('Fi')
					turn('L')
					turn('F')
					turn('Ri')
					turn('X')
				
				elif (left.tr == up.mc and back.tr == up.mc and
					right.tr == up.mc and up.br == up.mc and
					up.tc == up.mc and up.bc == up.mc and
					up.ml == up.mc and up.mr == up.mc):					
					if self.test == 1:
						print('OLL 15')	
					turn('Xi')
					turn('Ri')
					turn('2F')
					turn('R')
					turn('F')
					turn('Ri')
					turn('F')
					turn('R')
					turn('X')
				
				elif (front.tr == up.mc and back.tl == up.mc and
					up.tl == up.mc and up.bl == up.mc and
					up.tc == up.mc and up.bc == up.mc and
					up.ml == up.mc and up.mr == up.mc):					
					if self.test == 1:
						print('OLL 16')	
					turn('Ri')
					turn('Fi')
					turn('L')
					turn('F')
					turn('R')
					turn('Fi')
					turn('Li')
					turn('F')
				
				elif (front.tl == up.mc and front.tr == up.mc and
					up.tl == up.mc and up.tr == up.mc and
					up.tc == up.mc and up.bc == up.mc and
					up.ml == up.mc and up.mr == up.mc):					
					if self.test == 1:
						print('OLL 17')	
					turn('Xi')
					turn('2R')
					turn('B')
					turn('Ri')
					turn('2F')
					turn('R')
					turn('Bi')
					turn('Ri')
					turn('2F')
					turn('Ri')
					turn('X')
				
				elif (left.tr == up.mc and back.tl == up.mc and
					up.tl == up.mc and up.br == up.mc and
					up.tc == up.mc and up.bc == up.mc and
					up.ml == up.mc and up.mr == up.mc):					
					if self.test == 1:
						print('OLL 18')	
					turn('Ri')
					turn('Fi')
					turn('Li')
					turn('F')
					turn('R')
					turn('Fi')
					turn('L')
					turn('F')

			# If 4 corners (2 cases)
				elif (back.tc == up.mc and right.tc == up.mc and
					up.ml == up.mc and up.bc == up.mc and
					up.tl == up.mc and up.tr == up.mc and
					up.bl == up.mc and up.br == up.mc):
					if self.test == 1:
						print('OLL 19')	
					turn('X')
					turn('L')
					turn('Ri')
					turn('Xi')
					turn('Fi')
					turn('Li')
					turn('R')					
					turn('Xi')
					turn('2F')
					turn('2X')	
					turn('L')
					turn('Ri')									
					turn('Xi')
					turn('Fi')
					turn('Li')
					turn('R')
					
				elif (front.tc == up.mc and back.tc == up.mc and
					up.ml == up.mc and up.mr == up.mc and					
					up.tl == up.mc and up.tr == up.mc and
					up.bl == up.mc and up.br == up.mc):
					if self.test == 1:
						print('OLL 20')		
					turn('Li')
					turn('Xi')
					turn('R')
					turn('F')
					turn('Ri')
					turn('Fi')
					turn('X')
					turn('L')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')

			# If pacman top-left (6 cases)
				elif (up.bl == up.mc and front.tr == up.mc and
					back.tr == up.mc and right.tr == up.mc and
					right.tc == up.mc and up.tc == up.mc and
					up.ml == up.mc and front.tc == up.mc):
					if self.test == 1:
						print('OLL 21')	
					turn('L')
					turn('F')
					turn('Ri')
					turn('F')
					turn('R')
					turn('2F')
					turn('Li')
					
				elif (up.tl == up.mc and right.tr == up.mc and
					front.tl == up.mc and up.br == up.mc and
					right.tc == up.mc and up.tc == up.mc and
					up.ml == up.mc and front.tc == up.mc):		
					if self.test == 1:
						print('OLL 22')	
					turn('F')
					turn('Ri')
					turn('Fi')
					turn('Xi')
					turn('R')
					turn('F')
					turn('R')
					turn('Fi')
					turn('Ri')
					turn('X')
				
				elif (left.tl == up.mc and front.tl == up.mc and
					back.tl == up.mc and up.br == up.mc and
					right.tc == up.mc and up.tc == up.mc and
					up.ml == up.mc and front.tc == up.mc):		
					if self.test == 1:
						print('OLL 23')
					turn('Ri')
					turn('Z')
					turn('Ri')
					turn('Zi')
					turn('R')
					turn('Yi')
					turn('Xi')
					turn('R')
					turn('Z')
					turn('Ri')
					turn('Zi')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Z')
					turn('R')
					turn('Zi')
					turn('Ri')
					turn('X')
				
				elif (back.tr == up.mc and back.tl == up.mc and
					up.bl == up.mc and up.br == up.mc and
					right.tc == up.mc and up.tc == up.mc and
					up.ml == up.mc and front.tc == up.mc):		
					if self.test == 1:
						print('OLL 24')				
					turn('Xi')
					turn('Fi')
					turn('R')
					turn('2F')
					turn('Ri')
					turn('Fi')
					turn('R')
					turn('Fi')
					turn('2R')
					turn('Zi')
					turn('Ri')
					turn('Fi')
					turn('R')
					turn('F')
					turn('X')
					turn('B')
					
				elif (left.tl == up.mc and left.tr == up.mc and
					front.tr == up.mc and back.tl == up.mc and
					right.tc == up.mc and up.tc == up.mc and
					up.ml == up.mc and front.tc == up.mc):		
					if self.test == 1:
						print('OLL 25')		
					turn('F')
					turn('Xi')
					turn('R')
					turn('F')
					turn('Ri')
					turn('Fi')
					turn('R')
					turn('F')
					turn('Ri')
					turn('Fi')	
					turn('X')
					turn('Fi')
				
				elif (front.tl == up.mc and front.tr == up.mc and
					back.tl == up.mc and back.tr == up.mc and
					right.tc == up.mc and up.tc == up.mc and
					up.ml == up.mc and front.tc == up.mc):		
					if self.test == 1:
						print('OLL 26')					
					turn('L')
					turn('Fi')
					turn('Li')
					turn('F')
					turn('Z')
					turn('2R')
					turn('Zi')
					turn('2L')
					turn('Yi')
					turn('L')
					turn('F')
					turn('Li')
					turn('F')
					
			# If pacman top-right (6 cases)		
				elif (back.tr == up.mc and back.tl == up.mc and
					up.bl == up.mc and up.br == up.mc and
					up.tc == up.mc and left.tc == up.mc and
					up.mr == up.mc and front.tc == up.mc):
					if self.test == 1:
						print('OLL 27')	
					turn('Xi')
					turn('Fi')
					turn('Ri')
					turn('2F')
					turn('R')
					turn('F')
					turn('Ri')
					turn('F')
					turn('2R')
					turn('Z')
					turn('R')
					turn('F')
					turn('Ri')
					turn('Fi')
					turn('X')
					turn('Fi')
				
				elif (left.tl == up.mc and  up.tr == up.mc and
					front.tl == up.mc and right.tl == up.mc and
					up.tc == up.mc and left.tc == up.mc and
					up.mr == up.mc and front.tc == up.mc):
					if self.test == 1:
						print('OLL 28')					
					turn('X')
					turn('L')
					turn('Xi')
					turn('2F')
					turn('Ri')
					turn('Fi')
					turn('R')
					turn('Fi')
					turn('Li')
				
				elif (back.tr == up.mc and up.tr == up.mc and
					up.bl == up.mc and right.tl == up.mc and
					up.tc == up.mc and left.tc == up.mc and
					up.mr == up.mc and front.tc == up.mc):
					if self.test == 1:
						print('OLL 29')	
					turn('Xi')
					turn('Ri')
					turn('2F')
					turn('Xi')
					turn('2R')
					turn('Fi')
					turn('Ri')
					turn('F')
					turn('X')
					turn('Ri')
					turn('2F')
					turn('R')
					turn('X')
					
				elif (back.tr == up.mc and right.tr == up.mc and
					front.tl == up.mc and right.tl == up.mc and
					up.tc == up.mc and left.tc == up.mc and
					up.mr == up.mc and front.tc == up.mc):
					if self.test == 1:
						print('OLL 30')	
					turn('Fi')
					turn('Xi')
					turn('Li')
					turn('Fi')
					turn('L')
					turn('F')
					turn('Li')
					turn('Fi')
					turn('L')
					turn('F')
					turn('X')
					turn('F')
					
				elif (left.tl == up.mc and back.tl == up.mc and
					left.tr == up.mc and front.tr == up.mc and 
					up.tc == up.mc and left.tc == up.mc and
					up.mr == up.mc and front.tc == up.mc):
					if self.test == 1:
						print('OLL 31')						
					turn('Ri')
					turn('F')
					turn('Ri')
					turn('Fi')
					turn('2R')
					turn('Xi')
					turn('2F')
					turn('Xi')
					turn('Fi')
					turn('R')
					turn('F')
					turn('Ri')
					turn('2X')
					
				elif (back.tr == up.mc and back.tl == up.mc and
					front.tl == up.mc and front.tr == up.mc and
					up.tc == up.mc and left.tc == up.mc and
					up.mr == up.mc and front.tc == up.mc):
					if self.test == 1:
						print('OLL 32')	
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
					turn('Z')
					turn('2R')
					turn('Zi')
					turn('2R')
					turn('Y')
					turn('Ri')
					turn('Fi')
					turn('R')
					turn('Fi')
					
			# If pacman bottom-left (4 cases)
				elif (back.tr == up.mc and up.tr == up.mc and
					left.tr == up.mc and front.tr == up.mc and
					back.tc == up.mc and up.ml == up.mc and
					right.tc == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 33')
					turn('R')
					turn('Z')
					turn('R')
					turn('Zi')
					turn('Ri')
					turn('Y')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Z')
					turn('Ri')
					turn('Zi')
					turn('Ri')
					turn('Fi')
					turn('R')
			
				elif (up.tl == up.mc and back.tl == up.mc and
					front.tl == up.mc and right.tl == up.mc and 
					back.tc == up.mc and up.ml == up.mc and
					right.tc == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 34')			
					turn('Li')
					turn('Bi')
					turn('L')
					turn('Xi')
					turn('Fi')
					turn('Ri')
					turn('F')
					turn('R')
					turn('X')
					turn('Li')
					turn('B')
					turn('L')
				
				elif (left.tl == up.mc and back.tl == up.mc and
					front.tl == up.mc and up.br == up.mc and 
					back.tc == up.mc and up.ml == up.mc and
					right.tc == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 35')	
					turn('Xi')
					turn('2F')
					turn('2X')
					turn('L')	
					turn('Xi')
					turn('2R')
					turn('Fi')
					turn('R')
					turn('Fi')
					turn('Ri')
					turn('2F')
					turn('R')
					turn('Fi')
					turn('Li')
					turn('R')
			
				elif (up.tl == up.mc and up.tr == up.mc and
					left.tr == up.mc and right.tl == up.mc and 
					back.tc == up.mc and up.ml == up.mc and
					right.tc == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 36')	
					turn('2X')
					turn('Fi')
					turn('R')
					turn('Fi')
					turn('2R')
					turn('X')
					turn('F')
					turn('R')
					turn('F')
					turn('Ri')
					turn('Fi')
					turn('R')
					turn('X')
					turn('2B')
						
			# If pacman bottom-right (4 cases)	
				elif (left.tl == up.mc and back.tl == up.mc and
					left.tr == up.mc and front.tr == up.mc and 
					back.tc == up.mc and left.tc == up.mc and
					up.mr == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 37')	
					turn('L')
					turn('Xi')
					turn('Fi')
					turn('Zi')
					turn('Ri')
					turn('2F')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
					turn('R')
					turn('2F')
					turn('R')
					turn('Z')
					turn('Fi')
					turn('Li')
					turn('X')
					
				elif (back.tr == up.mc and right.tr == up.mc and 
					up.bl == up.mc and front.tr == up.mc and 
					back.tc == up.mc and left.tc == up.mc and
					up.mr == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 38')						
					turn('Xi')
					turn('2F')
					turn('2X')
					turn('Ri')
					turn('2L')
					turn('Xi')
					turn('F')
					turn('Li')
					turn('F')
					turn('L')
					turn('2F')
					turn('Li')
					turn('F')
					turn('Li')
					turn('R')
			
				elif (up.tl == up.mc and up.tr == up.mc and 
					left.tr == up.mc and right.tl == up.mc and 
					back.tc == up.mc and left.tc == up.mc and
					up.mr == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 39')	
					turn('2R')				
					turn('Xi')
					turn('F')
					turn('X')					
					turn('Ri')				
					turn('Bi')				
					turn('R')					
					turn('Xi')
					turn('Fi')					
					turn('2R')					
					turn('F')
					turn('R')				
					turn('Xi')
					turn('F')
					turn('2X')	
					turn('Ri')					

					
				elif (back.tr == up.mc and right.tr == up.mc and
					left.tr == up.mc and up.br == up.mc and 
					back.tc == up.mc and left.tc == up.mc and
					up.mr == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 40')	
					turn('2X')
					turn('Li')
					turn('2F')
					turn('R')
					turn('F')
					turn('Ri')
					turn('F')
					turn('2X')
					turn('L')

			# If letter C (2 cases)	
				elif (left.tc == up.mc and right.tl == up.mc and
					right.tc == up.mc and right.tr == up.mc and 
					up.tl == up.mc and up.tc == up.mc and 
					up.bl == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 41')
					turn('Xi')
					turn('R')
					turn('F')
					turn('Xi')
					turn('R')
					turn('Fi')
					turn('Ri')
					turn('F')
					turn('X')
					turn('Fi')
					turn('Ri')
					turn('X')
					
				elif (left.tl == up.mc and front.tc == up.mc and 
					back.tc == up.mc and right.tr == up.mc and 
					up.ml == up.mc and up.mr == up.mc and
					up.bl == up.mc and up.br == up.mc):
					if self.test == 1:
						print('OLL 42')												
					turn('Xi')
					turn('R')
					turn('F')
					turn('Ri')
					turn('Fi')
					turn('X')
					turn('Bi')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
					turn('B')

			# If letter L (4 cases)
				elif (left.tl == up.mc and back.tl == up.mc and
					front.tl == up.mc and up.br == up.mc and 
					back.tc == up.mc and up.ml == up.mc and
					up.mr == up.mc and front.tc == up.mc):
					if self.test == 1:
						print('OLL 43')	
					turn('Ri')
					turn('F')
					turn('R')
					turn('Z')
					turn('R')
					turn('Zi')
					turn('Ri')
					turn('Fi')
					turn('R')
					turn('Y')
					turn('L')
					turn('Z')
					turn('Ri')
					turn('Zi')
					turn('Li')
				
				elif (back.tr == up.mc and right.tr == up.mc and 
					up.bl == up.mc and front.tr == up.mc and 
					back.tc == up.mc and up.ml == up.mc and
					up.mr == up.mc and front.tc == up.mc):
					if self.test == 1:
						print('OLL 44')					
					turn('L')
					turn('Fi')
					turn('Li')
					turn('Z')
					turn('Ri')
					turn('Zi')
					turn('L')
					turn('F')
					turn('Li')
					turn('Yi')
					turn('Ri')
					turn('Z')
					turn('R')
					turn('Zi')
					turn('R')

				elif (back.tr == up.mc and right.tr == up.mc and 
					left.tr == up.mc and up.br == up.mc and 
					back.tc == up.mc and up.ml == up.mc and
					up.mr == up.mc and front.tc == up.mc):
					if self.test == 1:
						print('OLL 45')
					turn('Li')
					turn('Bi')
					turn('L')
					turn('Ri')
					turn('Xi')
					turn('Fi')
					turn('R')
					turn('F')
					turn('Li')
					turn('X')
					turn('B')
					turn('L')
					
				elif (left.tl == up.mc and back.tl == up.mc and
					up.bl == up.mc and right.tl == up.mc and 
					back.tc == up.mc and up.ml == up.mc and
					up.mr == up.mc and front.tc == up.mc):
					if self.test == 1:
						print('OLL 46')	
					turn('R')
					turn('B')
					turn('Ri')
					turn('L')
					turn('Xi')
					turn('F')
					turn('Li')
					turn('Fi')
					turn('R')
					turn('X')
					turn('Bi')
					turn('Ri')

			# If letter P (4 cases)
				elif (front.tc == up.mc and right.tl == up.mc and
					right.tc == up.mc and right.tr == up.mc and
					up.tl == up.mc and up.tc == up.mc and
					up.ml == up.mc and up.bl == up.mc):
					if self.test == 1:
						print('OLL 47')
					turn('F')
					turn('Xi')
					turn('F')
					turn('R')
					turn('Fi')
					turn('Ri')
					turn('X')
					turn('Fi')
				
				elif (left.tc == up.mc and front.tl == up.mc and
					front.tc == up.mc and back.tr == up.mc and
					up.tc == up.mc and up.tr == up.mc and
					up.mr == up.mc and up.br == up.mc):
					if self.test == 1:
						print('OLL 48')
					turn('Xi')					
					turn('Ri')					
					turn('Z')
					turn('Fi')					
					turn('L')				
					turn('Zi')
					turn('F')					
					turn('R')
					turn('Fi')
					turn('Ri')
					turn('X')
					turn('Fi')
					turn('R')

				elif (front.tc == up.mc and front.tr == up.mc and
					back.tl == up.mc and right.tc == up.mc and
					up.tl == up.mc and up.tc == up.mc and
					up.ml == up.mc and up.bl == up.mc):
					if self.test == 1:
						print('OLL 49')
					turn('Xi')
					turn('L')
					turn('Zi')
					turn('F')
					turn('Ri')
					turn('Z')
					turn('Fi')
					turn('Li')
					turn('F')
					turn('L')
					turn('X')
					turn('F')
					turn('Li')

				elif (left.tl == up.mc and left.tc == up.mc and
					left.tr == up.mc and front.tc == up.mc and
					up.tc == up.mc and up.tr == up.mc and
					up.mr == up.mc and up.br == up.mc):					
					if self.test == 1:
						print('OLL 50')
					turn('Fi')
					turn('Xi')
					turn('Fi')
					turn('Li')
					turn('F')
					turn('L')
					turn('X')
					turn('F')
					
			# If letter T (2 cases)
				elif (left.tl == up.mc and left.tr == up.mc and
					front.tc == up.mc and back.tc == up.mc and
					up.ml == up.mc and up.mr == up.mc and
					up.tr == up.mc and up.br == up.mc):
					if self.test == 1:
						print('OLL 51')	
					turn('F')
					turn('Xi')
					turn('R')
					turn('F')
					turn('Ri')
					turn('Fi')
					turn('X')
					turn('Fi')
					
				elif (back.tr == up.mc and front.tl == up.mc and
					front.tc == up.mc and back.tc == up.mc and
					up.ml == up.mc and up.mr == up.mc and
					up.tr == up.mc and up.br == up.mc):
					if self.test == 1:
						print('OLL 52')
					turn('Xi')
					turn('R')
					turn('F')
					turn('Ri')
					turn('Fi')
					turn('X')
					turn('Ri')
					turn('F')
					turn('R')
					turn('Fi')
			
			# If letter W (2 cases)
				elif (left.tl == up.mc and left.tc == up.mc and
					front.tr == up.mc and back.tc == up.mc and
					up.tr == up.mc and up.mr == up.mc and
					up.bl == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 53')					
					turn('Xi')
					turn('L')
					turn('F')
					turn('Li')
					turn('F')	
					turn('L')
					turn('Fi')
					turn('Li')
					turn('Fi')
					turn('X')
					turn('Li')
					turn('B')
					turn('L')
					turn('Bi')
				
				elif (front.tl == up.mc and back.tc == up.mc and
					right.tc == up.mc and right.tr == up.mc and
					up.tl == up.mc and up.ml == up.mc and
					up.br == up.mc and up.bc == up.mc):
					if self.test == 1:
						print('OLL 54')	
					turn('Xi')
					turn('Ri')
					turn('Fi')
					turn('R')
					turn('Fi')
					turn('Ri')
					turn('F')
					turn('R')
					turn('F')
					turn('X')
					turn('R')
					turn('Bi')
					turn('Ri')
					turn('B')
					
				# If letter Z (2 cases)
				elif (left.tr == up.mc and front.tc == up.mc and
					back.tc == up.mc and back.tl == up.mc and
					up.tl == up.mc and up.ml == up.mc and
					up.mr == up.mc and up.br == up.mc):
					if self.test == 1:
						print('OLL 55')
					turn('Ri')
					turn('F')
					turn('Xi')
					turn('R')
					turn('F')
					turn('Ri')
					turn('Fi')
					turn('Z')
					turn('Li')
					turn('Zi')
					turn('F')
					turn('R')
					turn('X')
				
				elif (back.tr == up.mc and back.tc == up.mc and
					front.tc == up.mc and right.tl == up.mc and
					up.tr == up.mc and up.mr == up.mc and
					up.ml == up.mc and up.bl == up.mc):
					if self.test == 1:
						print('OLL 56')
					turn('L')
					turn('Fi')
					turn('Xi')
					turn('Li')
					turn('Fi')
					turn('L')
					turn('F')
					turn('Zi')
					turn('R')
					turn('Z')
					turn('Fi')
					turn('Li')
					turn('X')
				
				else:
					turn('Y')
					
			#-------------------------------
			# While the cube is not complete
			#-------------------------------
			while not cubeComplete():
				for j in range(4):
				# Edge only permuations
					# Ua permutation
					if (right.tc == left.mc and left.tc == front.mc and
						front.tc == right.mc and front.tr == front.mc and 
						left.tr == left.mc and right.tr == right.mc and 
						back.tr == back.mc):
						if self.test == 1:
							print('PLL Ua')	
						turn('Xi')
						turn('R')
						turn('Fi')
						turn('R')
						turn('F')
						turn('R')
						turn('F')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('Fi')
						turn('2R')
						
					# Ub permutation
					elif (right.tc == front.mc and left.tc == right.mc and
						front.tc == left.mc and front.tr == front.mc and 
						left.tr == left.mc and right.tr == right.mc and 
						back.tr == back.mc):
						if self.test == 1:
							print('PLL Ub')				
						turn('Xi')
						turn('2R')
						turn('F')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('Ri')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('Ri')
						
					# Z permutation
					elif (front.tc == right.mc and right.tc == front.mc and
						left.tc == back.mc and back.tc == left.mc and 
						front.tr == front.mc and left.tr == left.mc and 
						right.tr == right.mc and back.tr == back.mc):
						if self.test == 1:
							print('PLL Z')
						turn('Xi')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('Fi')
						turn('R')
						turn('F')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('R')
						turn('F')
						turn('2R')
						turn('Fi')
						turn('Ri')
						turn('F')
					
					# H permutation
					elif (front.tc == back.mc and back.tc == front.mc and
						left.tc == right.mc and right.tc == left.mc and
						front.tr == front.mc and left.tr == left.mc and 
						right.tr == right.mc and back.tr == back.mc):
						if self.test == 1:
								print('PLL H')					
						turn('X')
						turn('2L')
						turn('2R')
						turn('F')					
						turn('2X')
						turn('2L')
						turn('2R')
						turn('2F')					
						turn('2X')
						turn('2L')
						turn('2R')	
						turn('F')					
						turn('2X')
						turn('2L')
						turn('2R')		

				# Corner only permutations
					# Aa permutation
					elif (front.tr == back.mc and back.tr == right.mc and
						right.tr == front.mc and front.tc == front.mc and
						left.tc == left.mc and right.tc == right.mc and 
						back.tc == back.mc):
						if self.test == 1:
								print('PLL Aa')						
						turn('Ri')
						turn('F')
						turn('Ri')
						turn('2B')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('2B')
						turn('2R')
					
					# Ab permutation
					elif (left.tr == front.mc and front.tr == right.mc and
						right.tr == left.mc and front.tc == front.mc and
						left.tc == left.mc and right.tc == right.mc and 
						back.tc == back.mc):
						if self.test == 1:
								print('PLL Aa')
						turn('R')
						turn('Bi')
						turn('R')
						turn('2F')
						turn('Ri')
						turn('B')
						turn('R')
						turn('2F')
						turn('2R')
					
					# E permutation
					elif(right.tl == back.mc and right.tr == front.mc and
						left.tl == front.mc and left.tr == back.mc and
						front.tc == front.mc and left.tc == left.mc and
						right.tc == right.mc and back.tc == back.mc):
						if self.test == 1:
								print('PLL E')
						turn('R')
						turn('Bi')
						turn('Ri')
						turn('F')
						turn('R')
						turn('B')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('B')
						turn('Ri')
						turn('F')
						turn('R')
						turn('Bi')
						turn('Ri')
						turn('Fi')				
				# Corner and edge swap permutations
					# T permutation
					elif (right.tl == back.mc and right.tr == front.mc and
						left.tc == right.mc and right.tc == left.mc and
						back.tc == back.mc and front.tc == front.mc and
						back.tr == back.tc and front.tl == front.mc):
						if self.test == 1:
							print('PLL T')	
						turn('Xi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('Ri')
						turn('X')
						turn('F')
						turn('2R')
						turn('Xi')
						turn('Fi')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('X')
						turn('Fi')
					
					# F permutation
					elif (front.tl == right.mc and front.tr == left.mc and	
						left.tc == right.mc and right.tc == left.mc and 
						back.tc == back.mc and front.tc == front.mc and
						back.tl == back.mc and back.tr == back.mc):
						if self.test == 1:
							print('PLL F')	
						turn('Xi')
						turn('Ri')
						turn('2F')
						turn('Ri')
						turn('Z')
						turn('Fi')
						turn('Ri')
						turn('X')
						turn('Fi')
						turn('2R')
						turn('Xi')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('Ri')
						turn('X')
						turn('F')
						turn('R')
						turn('Xi')
						turn('Fi')
						turn('X')
						turn('F')
						
					# Ja permutation
					elif (left.tc == back.mc and back.tc == left.mc and
						left.tl == back.mc and back.tl == left.mc and 
						front.tc == front.mc and right.tc == right.mc and
						front.tl == front.mc and front.tr == front.mc):
						if self.test == 1:
							print('PLL Ja')	
						turn('Xi')
						turn('Ri')
						turn('F')
						turn('Li')
						turn('2F')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('2F')
						turn('L')
						turn('R')
						turn('Fi')
					
					# Jb permutation
					elif (front.tc == right.mc and right.tc == front.mc and
						front.tr == right.mc and right.tr == front.mc and
						back.tc == back.mc and left.tc == left.mc and
						left.tl == left.mc and left.tr == left.mc):
						if self.test == 1:
							print('PLL Jb')	
						turn('Xi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('X')
						turn('Fi')
						turn('R')
						turn('Xi')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('Ri')
						turn('X')
						turn('F')
						turn('2R')
						turn('Xi')
						turn('Fi')
						turn('Ri')
						turn('Fi')
						
					# Ra permutation
					elif (back.tl == left.mc and back.tr == right.mc and
						left.tc == front.mc and front.tc == left.mc and 
						right.tc == right.mc and back.tc == back.mc and
						front.tl == front.mc and front.tr == front.mc):
						if self.test == 1:
							print('PLL Ra')
						turn('Xi')
						turn('L')
						turn('2F')
						turn('Li')
						turn('2F')
						turn('L')
						turn('X')
						turn('Fi')
						turn('Li')
						turn('Xi')
						turn('Fi')
						turn('L')
						turn('F')
						turn('L')
						turn('X')
						turn('F')
						turn('2L')
						turn('Xi')
						turn('F')
					
					# Rb permutation
					elif (back.tl == left.mc and back.tr == right.mc and
						right.tc == front.mc and front.tc == right.mc and
						left.tc == left.mc and back.tc == back.mc and
						front.tl == front.mc and front.tr == front.mc):
						if self.test == 1:
							print('PLL Rb')
						turn('Xi')
						turn('Ri')
						turn('2F')
						turn('R')
						turn('2F')
						turn('Ri')
						turn('X')
						turn('F')
						turn('R')
						turn('Xi')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('Ri')
						turn('X')
						turn('Fi')
						turn('2R')
						turn('Xi')
						turn('Fi')
					
					# V permutation
					elif (back.tc == right.mc and right.tc == back.mc and
						left.tl == right.mc and front.tr == back.mc and
						right.tr == right.mc and front.tl == front.mc and
						left.tc == left.mc and front.tc == front.mc):
						if self.test == 1:
							print('PLL V')	
						turn('Xi')
						turn('Ri')
						turn('F')
						turn('Ri')
						turn('Z')
						turn('Fi')
						turn('Ri')
						turn('X')
						turn('Fi')
						turn('2R')
						turn('Xi')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('Ri')
						turn('X')
						turn('F')
						turn('R')
						turn('F')
						
					# Y permutation
					elif (left.tc == back.mc and back.tc == left.mc and
						front.tr == back.mc and back.tr == front.mc and 
						front.tc == front.mc and right.tc == right.mc and
						front.tl == front.mc and right.tr == right.mc):
						if self.test == 1:
							print('PLL Y')
						turn('F')
						turn('Xi')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('X')
						turn('Fi')
						turn('R')
						turn('Xi')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('X')
						turn('Ri')
						turn('F')
						turn('R')
						turn('Fi')
					
					# Na permutation
					elif (front.tc == back.mc and back.tc == front.mc and
						front.tr == back.mc and back.tr == front.mc and
						right.tc == right.mc and left.tc == left.mc and
						front.tl == front.mc and right.tr == right.mc):
						if self.test == 1:
							print('PLL Na')
						turn('Xi')
						turn('L')
						turn('Fi')
						turn('R')
						turn('2F')
						turn('Li')
						turn('F')
						turn('Ri')
						turn('L')
						turn('Fi')
						turn('R')
						turn('2F')
						turn('Li')
						turn('F')
						turn('Ri')
						turn('F')
					
					# Nb permutation
					elif (front.tc == back.mc and back.tc == front.mc and
						front.tl == back.mc and back.tl == front.mc and 
						left.tc == left.mc and right.tc == right.mc and
						front.tr == front.mc and left.tl == left.mc):
						if self.test == 1:
							print('PLL Nb')
						turn('Xi')
						turn('Ri')
						turn('F')
						turn('Li')
						turn('2F')
						turn('R')
						turn('Fi')
						turn('L')
						turn('Ri')
						turn('F')
						turn('Li')
						turn('2F')
						turn('R')
						turn('Fi')
						turn('L')
						turn('Fi')

				# Corner and edge cycle permutations				
					# Ga permutation
					elif (front.tl == left.mc and left.tl == back.mc and 
						back.tl == front.mc and left.tc == right.mc and 
						right.tc == back.mc and back.tc == left.mc and
						front.tc == front.mc and front.tr == front.mc):
						if self.test == 1:
							print('PLL Ga')		
						turn('Xi')
						turn('2R')
						turn('Z')
						turn('B')
						turn('Ri')
						turn('F')
						turn('Ri')
						turn('Fi')
						turn('R')
						turn('Zi')
						turn('Bi')
						turn('2R')
						turn('Zi')
						turn('Ri')
						turn('F')
						turn('R')
					
					# Gb permutation
					elif (front.tr == right.mc and right.tr == back.mc and 
						back.tr == front.mc and front.tc == back.mc and
						right.tc == front.mc and back.tc == right.mc and 
						left.tc == left.mc and left.tr == left.mc):
						if self.test == 1:
							print('PLL Gb')
						turn('Xi')
						turn('Li')
						turn('Fi')
						turn('L')
						turn('Zi')
						turn('2R')
						turn('Z')
						turn('B')
						turn('Ri')
						turn('F')
						turn('R')
						turn('Fi')
						turn('R')
						turn('Zi')
						turn('Bi')
						turn('2R')
					
					# Gc permutation
					elif (left.tl == front.mc and front.tl == right.mc and
					right.tl == left.mc and left.tc == right.mc and
					front.tc == left.mc and right.tc == front.mc and 
					back.tc == back.mc and back.tl == back.mc):
						if self.test == 1:
							print('PLL Gc')
						turn('Xi')
						turn('2R')
						turn('Zi')
						turn('Bi')
						turn('R')
						turn('Fi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Z')
						turn('B')
						turn('2R')
						turn('Z')
						turn('R')
						turn('Fi')
						turn('Ri')

					# Gd permutation
					elif (left.tr == back.mc and back.tr == right.mc and
						right.tr == left.mc and left.tc == front.mc and 
						front.tc == back.mc and back.tc == left.mc and 
						right.tc == right.mc and right.tl == right.mc):
						if self.test == 1:
							print('PLL Gd')				
						turn('Xi')
						turn('R')
						turn('F')
						turn('Ri')
						turn('Zi')
						turn('2R')
						turn('Zi')
						turn('Bi')
						turn('R')
						turn('Fi')
						turn('Ri')
						turn('F')
						turn('Ri')
						turn('Z')
						turn('B')
						turn('2R')
					else:
						turn('Y')
				if not cubeComplete():
					turn('Z')
					turn('Ri')
					turn('Zi')
							
			# Optimize the list by removing superfluous/duplicate turns
			self.trimList()
			
			# Get list length without counting "Y" moves:
			listLength = 0	
			for move in self.movelist:
				if move != 'Y' and move != 'Yi' and move != '2Y':
					listLength += 1
					
			if listLength < minListLength:
				minListLength = listLength
				minList = self.movelist

		self.listLength = minListLength
		self.movelist = minList
		self.followMoves()