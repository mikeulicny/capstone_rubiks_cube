import numpy as np
from face import Face
from cube import Cube
from algobasic import AlgoBasic
import time
import statistics as st

def Main():
	avgLength = 100
	minLength = 1000
	maxLength = 0
	minMoveList = []
	maxMoveList = []
	avgMoveList = []
	
	ITERS = 1000
	
	for i in range(ITERS):
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
		
		# Randomize cube
		algo = AlgoBasic(cube)
		algo.randomize()
		setupList = algo.movelist
		
		# Print initial cube
		# print('Test from solved: y @ up, g @ front: ' + str(algo.movelist))
		# print('Before:\n')
		# print(cube)

		algo.solve()
		print(str(round((i / ITERS) * 100, 2)) + '%')
		
		avgLength = (avgLength*(i+1) + len(algo.movelist)) // (i+2)
		if len(algo.movelist) < minLength:
			minLength = len(algo.movelist)
			minMoveList = setupList
		if len(algo.movelist) > maxLength:
			maxLength = len(algo.movelist)
			maxMoveList = setupList
			
		avgMoveList.append(len(algo.movelist))
			
	print('\nMin movecount: ' + str(minLength) + ' moves')
	print('Min list: ' +  str(minMoveList))
	print('Max movecount: ' +  str(maxLength) + ' moves')
	print('Max list: ' +  str(maxMoveList))
	print('Median number moves: ' + str(st.median(avgMoveList)))
	print('Standard deviation: ' + str(round(st.stdev(avgMoveList),2)))
	
# Calling Test
if __name__ == '__main__': 
    Main() 
