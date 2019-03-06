import numpy as np
import random
from face import Face
from cube import Cube

class AlgoBasic:			
	# Initializer
	def __init__(self, cube):
		self.c = cube		
		self.movelist = []
		self.movenumber = 0
		
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
		if (front.ml == front.mc == front.mr and left.ml == left.mc == left.mr and 
			right.ml == right.mc == right.mr and back.ml == back.mc == back.mr):
			out = True
		return out

	# Function to determine if top corners are correctly oriented
	def topCrnrsComplete(self):
		# Simplify attributes
		front = self.c.front
		back = self.c.back
		left = self.c.left
		right = self.c.right

		out = False
		if (front.tl == front.mc and left.tl == left.mc and
			back.tl == back.mc and right.tl == right.tr):
			out = True
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
		# print(dir + ' (turn ' + str(self.movenumber) + '):')
		# self.movenumber += 1
		# print(self.c)
		# input('')
	
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
					elif ml[i] == ml[j] and ml[i][0] != '2':
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
					elif ml[i][0] == '2' and ml[i] == ml[j]:
						ml[i] = 'RM'
						ml[j] = 'RM'
				except:
					pass	
		# New movelist without values marked 'RM'
		self.movelist = [move for move in ml.tolist() if move != 'RM']
	
	# Function to randomize a cube (20 turns)
	def randomize(self):
		# Simplify attributes and methods
		turn = self.turn
		turn = self.turn
		
		# Clear existing move list
		self.movelist = []
		
		# 20 random turns
		for i in range(20):
			randomTurn = random.randint(9,26)
			if randomTurn == 9:
				turn('U')				
			elif randomTurn == 10:					
				turn('Ui')					
			elif randomTurn == 11:					
				turn('D')				
			elif randomTurn == 12:					
				turn('Di')
			elif randomTurn == 13:					
				turn('F')				
			elif randomTurn == 14:					
				turn('Fi')
			elif randomTurn == 15:					
				turn('B')				
			elif randomTurn == 16:					
				turn('Bi')
			elif randomTurn == 17:					
				turn('L')				
			elif randomTurn == 18:					
				turn('Li')
			elif randomTurn == 19:					
				turn('R')	
			elif randomTurn == 20:					
				turn('Ri')	
			elif randomTurn == 21:					
				turn('2U')
			elif randomTurn == 22:					
				turn('2D')
			elif randomTurn == 23:					
				turn('2F')	
			elif randomTurn == 24:					
				turn('2B')	
			elif randomTurn == 25:					
				turn('2L')		
			elif randomTurn == 26:					
				turn('2R')	
					
		# Optimize the list by removing superfluous/duplicate turns
		self.trimList()
	
	# Function to get a cube to a pre-determined configuration
	def followMoves(self):	
		L = len(self.movelist)
		for i in range(L):
			self.c.turn(self.movelist[i])
		
	# Function to solve a cube				
	def solve(self):
		# Simplify attributes and methods
		up = self.c.up
		down = self.c.down
		front = self.c.front
		back = self.c.back
		left = self.c.left
		right = self.c.right
		turn = self.turn
		turn = self.turn
		downSliceComplete = self.downSliceComplete
		midSliceComplete = self.midSliceComplete
		topCrnrsComplete = self.topCrnrsComplete
		cubeComplete = self.cubeComplete
		
		# Clear existing move list
		self.movelist = []		
		
		#-----------------------
		# Get yellow edge on top
		#-----------------------
		if front.mc == 'y':
			turn('X')
		elif back.mc == 'y':
			turn('Xi')
		elif left.mc == 'y':
			turn('Z')
		elif right.mc == 'y':
			turn('Zi')
		elif down.mc == 'y':
			turn('2X')
			
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
					elif up.tc != 'w':
						turn('Ui')
						turn('Li')
					else:
						turn('2U')
						turn('Li')
			# If it's NOT in the front, move it there
			elif right.mr == 'w' or right.ml == 'w':
				turn('Y')
			elif left.mr == 'w' or left.ml == 'w':
				turn('Yi')
			elif back.mr == 'w' or back.ml == 'w':
				turn('2Y')
				
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
				elif up.bc != 'w':
					turn('F')
					turn('Ui')
					turn('R')
					
			# If it's NOT in the front, move it there
			elif right.tc == 'w':
				turn('Y')
			elif left.tc == 'w':
				turn('Yi')
			elif back.tc == 'w':
				turn('2Y')
		
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
					elif up.bc != 'w':
						turn('Fi')
						turn('Ui')
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
				turn('Y')
			elif left.bc == 'w':
				turn('Yi')
			elif back.bc == 'w':
				turn('2Y')
		
		# If white edge on down face:
			# If it's already in the 'front', move it up
			elif down.tc == 'w':
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
			# If it's NOT in the front, move it there
			elif down.mr == 'w':
				turn('Y')
			elif down.ml == 'w':
				turn('Yi')
			elif down.bc == 'w':
				turn('2Y')

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
				turn('Y')

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

		# If desired piece in top slice but turnped:
			# Keep turnping to avoid tons of wasted turns
			elif up.mr != 'y' and right.tc != 'y':
				turn('Y')
			elif up.ml != 'y' and left.tc != 'y':
				turn('Y')
			elif up.tc != 'y' and back.tc != 'y':
				turn('Y')
				
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
				turn('Y')		

		#-------------------------------------------
		# While the top (yellow) cross isn't complete
		#-------------------------------------------
		while not up.allEdges('y'):
			# If only the center of the cross is yellow
			if up.tc != 'y' and up.ml != 'y' and up.mr != 'y' and up.bc != 'y':
				turn('F')
				turn('R')
				turn('U')
				turn('Ri')
				turn('Ui')
				turn('Fi')
			
			# If there's a yellow line 
			elif up.tc == 'y' and up.bc == 'y':
				turn('Y')
			elif up.ml == 'y' and up.mr == 'y':
				turn('F')
				turn('R')
				turn('U')
				turn('Ri')
				turn('Ui')
				turn('Fi')

			# If there's a yellow triangle
			elif up.ml == 'y' and up.bc == 'y':
				turn('Y')
			elif up.tc == 'y' and up.mr == 'y':
				turn('Yi')
			elif up.mr == 'y' and up.bc == 'y':
				turn('2Y')
			elif up.tc == 'y' and up.ml == 'y':
				turn('F')
				turn('U')
				turn('R')
				turn('Ui')
				turn('Ri')
				turn('Fi')					
		#-------------------------------------
		# While the yellow side isn't complete
		#-------------------------------------
		while not up.isComplete():
			# If no corners are yellow
			if up.tl != 'y' and up.tr != 'y' and up.bl != 'y' and up.br != 'y':
				if left.tr == 'y':						
					turn('R')
					turn('U')
					turn('Ri')
					turn('U')
					turn('R')
					turn('2U')
					turn('Ri')
				elif front.tr == 'y':		
					turn('Y')
				elif back.tr == 'y':
					turn('Yi')
				elif right.tr == 'y':
					turn('2Y')
			
			# If exactly one corner is yellow
			elif up.tl != 'y' and up.tr != 'y' and up.bl == 'y' and up.br != 'y':
					turn('R')
					turn('U')
					turn('Ri')
					turn('U')
					turn('R')
					turn('2U')
					turn('Ri')
			elif up.tl != 'y' and up.tr != 'y' and up.bl != 'y' and up.br == 'y':
				turn('Y')
			elif up.tl == 'y' and up.tr != 'y' and up.bl != 'y' and up.br != 'y':
				turn('Yi')
			elif up.tl != 'y' and up.tr == 'y' and up.bl != 'y' and up.br != 'y':
				turn('2Y')
				
			# If any two corners are yellow
			else:
				if front.tl == 'y':
					turn('R')
					turn('U')
					turn('Ri')
					turn('U')
					turn('R')
					turn('2U')
					turn('Ri')
				elif right.tl == 'y':
					turn('Y')
				elif left.tl == 'y':
					turn('Yi')
				elif back.tl == 'y':
					turn('2Y')
		
		#---------------------------------------
		# While the top corners are not complete
		#---------------------------------------
		while not topCrnrsComplete():
			# If back corners are correct
			if back.tl == back.tr == back.mc:
				turn('Ri')
				turn('F')
				turn('Ri')
				turn('2B')
				turn('R')
				turn('Fi')
				turn('Ri')
				turn('2B')
				turn('2R')
				turn('Ui')
		
			# If there are two correct corners (i.e. same as back)
			elif right.tl == right.tr == back.mc:
				turn('Ui')
			elif left.tl == left.tr == back.mc:
				turn('U')		
			elif front.tl == front.tr == back.mc:
				turn('2U')
				
			# If there is any pair of correct corners
			elif (right.tl == right.tr or front.tl == front.tr or
				left.tl == left.tr or front.tl == front.tr):
				turn('Y')
			
			# If there are no correct corners
			else:
				turn('Ri')
				turn('F')
				turn('Ri')
				turn('2B')
				turn('R')
				turn('Fi')
				turn('Ri')
				turn('2B')
				turn('2R')
				turn('Ui')

		#-------------------------------				
		# While the cube is not complete
		#-------------------------------
		while not cubeComplete():
			# If no top edges in correct position
			if (front.tc != front.mc and left.tc != left.mc and
				right.tc != right.mc and back.tc != back.mc):
				turn('2F')
				turn('U')
				turn('L')
				turn('Ri')
				turn('2F')
				turn('Li')
				turn('R')
				turn('U')
				turn('2F')
			
			# If one edge in correct position, get it to back
			elif left.tc == left.tl:
				turn('Y')
			elif right.tc == right.tl:
				turn('Yi')
			elif front.tc == front.tl:
				turn('2Y')
				
			# If remaining three need to be rotated clockwise
			elif front.tc == left.mc:
				turn('2F')
				turn('U')
				turn('L')
				turn('Ri')
				turn('2F')
				turn('Li')
				turn('R')
				turn('U')
				turn('2F')				
			
			# If remaining three need to be rotated counter-clockwise
			elif front.tc == right.mc:
				turn('2F')
				turn('Ui')
				turn('L')
				turn('Ri')
				turn('2F')
				turn('Li')
				turn('R')
				turn('Ui')
				turn('2F')				
			
		# Optimize the list by removing superfluous/duplicate turns
		self.trimList()