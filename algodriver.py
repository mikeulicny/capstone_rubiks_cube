#--------------------------------------------------------------
# ECE 4600 Capstone - Winter 2019
# Wayne State University
# Project: Rubik's Cube Solving Robot
# Primary author: Joseph VanBuhler
# Additional team members: Michael Ulicny, Joseph Breitner
#
# This program is a short driver program used in
# troubleshooting the Face, Cube, and algorithm classes.
# It is also useful as a demonstration of the capabilities of 
# the Face, Cube, and algorithm classes as a whole.
#--------------------------------------------------------------

# Resolving dependencies
import numpy as np
from face import Face
from cube import Cube
from algocfop import AlgoCFOP
import statistics as st
import time

# Completion flag
done = False

while done == False:

	# User prompt
	print('Please select an option and press Enter:')
	print('    1: Solve cube from random configuration')
	print('    2: Solve cube from stored move configuration')
	print('    3: Solve from manual entry of cube configuration')
	print('    4: Solve N cubes and display statistical info')
	print('    5: Exit')
	controlValue = input('    Option: ')
	print('--------------------------------------------------------------\n')

	# 1: Solve cube from random configuration
	if controlValue == '1':
		# Initial solved cube:
		up = np.array([['y', 'y', 'y'],
			['y', 'y', 'y'],
			['y', 'y', 'y']])	
		front = np.array([['g', 'g', 'g'],
			['g', 'g', 'g'],
			['g', 'g', 'g']])
		left = np.array([['r', 'r', 'r'],
			['r', 'r', 'r'],
			['r', 'r', 'r']])
		down = np.array([['w', 'w', 'w'],
			['w', 'w', 'w'],
			['w', 'w', 'w']])
		back = np.array([['b', 'b', 'b'],
			['b', 'b', 'b'],
			['b', 'b', 'b']])
		right = np.array([['o', 'o', 'o'],
			['o', 'o', 'o'],
			['o', 'o', 'o']])
			
		# Instantiate faces
		up = Face(up)
		down = Face(down)
		front = Face(front)
		back = Face(back)
		left = Face(left)
		right = Face(right)

		# Instantiate cube
		cube = Cube(up, down, front, back, left, right)

		# Cube setup
		algo = AlgoCFOP(cube)
		algo.randomize()
		
		# Print initial cube
		print('Test from random scramble (y on top, g on front):')
		algo.printList()

	# 2: Solve cube from stored move configuration
	elif controlValue == '2':
		# Initial solved cube:
		up = np.array([['y', 'y', 'y'],
			['y', 'y', 'y'],
			['y', 'y', 'y']])	
		front = np.array([['g', 'g', 'g'],
			['g', 'g', 'g'],
			['g', 'g', 'g']])
		left = np.array([['r', 'r', 'r'],
			['r', 'r', 'r'],
			['r', 'r', 'r']])
		down = np.array([['w', 'w', 'w'],
			['w', 'w', 'w'],
			['w', 'w', 'w']])
		back = np.array([['b', 'b', 'b'],
			['b', 'b', 'b'],
			['b', 'b', 'b']])
		right = np.array([['o', 'o', 'o'],
			['o', 'o', 'o'],
			['o', 'o', 'o']])

		# Instantiate faces
		up = Face(up)
		down = Face(down)
		front = Face(front)
		back = Face(back)
		left = Face(left)
		right = Face(right)

		# Instantiate cube
		cube = Cube(up, down, front, back, left, right)

		# Cube setup
		algo = AlgoCFOP(cube)
		algo.movelist = ['U', '2R', 'F', 'B', 'R', '2B', 'R', '2U', 'L', '2B', 'R', 'Ui', 'Di', '2R', 'F', 'Ri', 'L', '2B', '2U', '2F']
		algo.followMoves()	

		# Print initial cube
		print('Test from internal movelist (y on top, g on front):')
		algo.printList()


	# 3: Solve from manual entry of cube configuration	
	elif controlValue == '3':
		# Input flag
		inputOK = False
		
		while inputOK == False:
			# Input current cube state
			print('Please enter the cube configuration for each side as prompted.')
			upColors = input('    Up layer colors:    ')
			frontColors = input('    Front layer colors: ')
			downColors = input('    Down layer colors:  ')
			rightColors = input('    Right layer colors: ')
			backColors = input('    Back layer colors:  ')
			leftColors = input('    Left layer colors:  ')
			colorSides = [upColors, frontColors, downColors, rightColors, backColors, leftColors]

			# Create numpy arrays
			up = np.empty([3,3], dtype=np.str)
			front = np.empty([3,3], dtype=np.str)
			down = np.empty([3,3], dtype=np.str)
			right = np.empty([3,3], dtype=np.str)
			back = np.empty([3,3], dtype=np.str)
			left = np.empty([3,3], dtype=np.str)
			faces = [up, front, down, right, back, left]

			# Fill numpy arrays
			for i in range(6):
				for j in range(3):
					for k in range(3):
						faces[i][j][k] = colorSides[i][3*j + k]
		
			# Instantiate faces
			up = Face(up)
			down = Face(down)
			front = Face(front)
			back = Face(back)
			left = Face(left)
			right = Face(right)

			# Instantiate cube
			cube = Cube(up, down, front, back, left, right)	

			# Cube setup
			algo = AlgoCFOP(cube)		
			
			# Print cube for inspection
			print('\nCube configuration as entered:\n')
			print(cube)
		
			# Prompt for correction
			status = input('Is this correct? (Y/N): ')
			if status == 'n' or status == 'N':
				inputOK = False
				print('')
			else:
				inputOK = True
		
		# Print initial cube
		print('Test from manual entry of cube: ')
		algo.printList()

	# 4: Solve N cubes and display statistical info
	elif controlValue == '4':
		# Input number of iterations
		iters = input('Please enter number of cubes to solve: ')

		avgLength = 100
		minLength = 1000
		maxLength = 0
		minMoveList = []
		maxMoveList = []
		avgMoveList = []
	
		# Initial solved cube:
		up = np.array([['y', 'y', 'y'],
			['y', 'y', 'y'],
			['y', 'y', 'y']])	
		front = np.array([['g', 'g', 'g'],
			['g', 'g', 'g'],
			['g', 'g', 'g']])
		left = np.array([['r', 'r', 'r'],
			['r', 'r', 'r'],
			['r', 'r', 'r']])
		down = np.array([['w', 'w', 'w'],
			['w', 'w', 'w'],
			['w', 'w', 'w']])
		back = np.array([['b', 'b', 'b'],
			['b', 'b', 'b'],
			['b', 'b', 'b']])
		right = np.array([['o', 'o', 'o'],
			['o', 'o', 'o'],
			['o', 'o', 'o']])
				
		# Instantiate faces
		up = Face(up)
		down = Face(down)
		front = Face(front)
		back = Face(back)
		left = Face(left)
		right = Face(right)

		# Instantiate cube
		cube = Cube(up, down, front, back, left, right)

		for i in range(int(iters)):
			# Cube setup
			algo = AlgoCFOP(cube)
			algo.randomize()
			setupList = algo.movelist
			
			# Solve random cube
			algo.solve()
			prcnt = round((i / int(iters)) * 100, 2)
			print(str(prcnt) + '%', end = '\r')

			# Determine min and max list lengths
			if algo.listLength < minLength:
				minLength = algo.listLength
				minMoveList = setupList
			if algo.listLength > maxLength:
				maxLength = algo.listLength
				maxMoveList = setupList
			
			# Add list l
			avgMoveList.append(algo.listLength)
			
			del algo
		
		print('100.0%', end = '\r')
		print('\nInformation per ' + str(iters) + ' cubes:')
		print('    Min movecount: ' + str(minLength) + ' moves')
		print('    Min list: ' +  str(minMoveList))
		print('    Max movecount: ' +  str(maxLength) + ' moves')
		print('    Max list: ' +  str(maxMoveList))
		print('    Median number moves: ' + str(st.median(avgMoveList)))
		print('    Standard deviation: ' + str(round(st.stdev(avgMoveList),2)))
		print('\n--------------------------------------------------------------\n')

	# 5: Exit
	else:
		done = True
		break
	
	if controlValue != '4':
		# Print input cube
		print('\nBefore:\n')
		print(algo.cube)

		# Solve cube
		t0 = time.time()
		algo.solve()
		t1 = time.time()

		# Print output (solved) cube
		print('After:\n')
		print(algo.cube)

		# Print solution list
		print('Solution move list:')
		algo.printList()
		print('\nActual number of turns by our bot: ' + str(algo.listLength))
		print('Time to generate solution: ' + str(t1-t0)[:6] +' s')
		print('\n--------------------------------------------------------------\n')