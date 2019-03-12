import numpy as np
from face import Face
from cube import Cube
from algocfop import AlgoCFOP
import statistics as st

def Main():

	avgLength = 100
	minLength = 1000
	maxLength = 0
	minMoveList = []
	maxMoveList = []
	avgMoveList = []
	
	ITERS = 10000
	
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
		algo = AlgoCFOP(cube)
		algo.randomize()
		setupList = algo.movelist

		# Solve random cube
		print(str(setupList))
		algo.solve()
		prcnt = round((i / ITERS) * 100, 2)
		print(str(prcnt) + '%', end = '\r')
		
		# Get list length without counting "Y" moves and multi-counting "U" moves:
		listLength = 0	
		for move in algo.movelist:
			if move == 'U' or move == 'Ui' or move == '2U':
				listLength += 3
			elif move != 'Y' and move != 'Yi' and move != '2Y':
				listLength += 1
		
		if listLength < minLength:
			minLength = listLength
			minMoveList = setupList
		if listLength > maxLength:
			maxLength = listLength
			maxMoveList = setupList
			
		avgMoveList.append(listLength)
		
	print('\nNumber of turns our bot takes (algocfop):')
	print('Min movecount: ' + str(minLength) + ' moves')
	print('Min list: ' +  str(minMoveList))
	print('Max movecount: ' +  str(maxLength) + ' moves')
	print('Max list: ' +  str(maxMoveList))
	print('Median number moves: ' + str(st.median(avgMoveList)))
	print('Standard deviation: ' + str(round(st.stdev(avgMoveList),2)))		
	
# Calling Test
if __name__ == '__main__': 
    Main() 
