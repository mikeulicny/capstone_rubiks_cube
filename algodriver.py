import numpy as np
from face import Face
from cube import Cube
from algocfop import AlgoBasic
import time

def Main():
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
	# down = np.rot90(down, 1)
	# back = np.rot90(back, 3)
	# right = np.rot90(right, 3)

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
	algo = AlgoBasic(cube)
	# algo = AlgoBasic(cube, 1)	
	algo.movelist = (['Fi', 'Fi', 'B', 'Fi', '2B', 'D', 'B', 'D', 'B', 'L', '2F', 'R', 'B', 'Ui'])
	algo.followMoves()
	# algo.randomize()
	
	# Print initial cube
	print('Test from solved: y @ up, g @ front: ' + str(algo.movelist))
	# print('Before:\n')
	print(cube)
	
	# input('Press Enter to solve...')

	t0 = time.time()
	algo.solve()
	t1 = time.time()
	
	# Get list length without counting "Y" moves and multi-counting "U" moves:
	listLength = 0	
	for move in algo.movelist:
		if move == 'U' or move == 'Ui' or move == '2U':
			listLength += 3
		elif move != 'Y' and move != 'Yi' and move != '2Y':
			listLength += 1
			
	print('After:\n')
	print(cube)
	print(algo.movelist)
	print('Number of moves in list: ' + str(len(algo.movelist)))
	print('Actual number of turns by our bot: ' + str(listLength))
	print('Time to generate solution: ' + str(t1-t0)[:6] +' s')
	
# Calling Test
if __name__ == '__main__': 
    Main() 
