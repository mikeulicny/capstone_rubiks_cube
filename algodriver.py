import numpy as np
from face import Face
from cube import Cube
from algobasic import AlgoBasic
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
	
	# Troubleshooting cubes
	# algo.movelist = (['Fi', '2U', 'Li', 'Di', 'Li', 'F', 'B',
		# '2U', '2F', 'D', '2F', 'Di', 'B', '2L', 'F', '2U', 'Li'])
	algo.followMoves()
	
	# Print initial cube
	print('Test from solved: y @ up, g @ front: ' + str(algo.movelist))
	# print('Before:\n')
	print(cube)
	
	input('Press Enter to solve...')

	t0 = time.time()
	algo.solve()
	t1 = time.time()
	
	print('After:\n')
	print(cube)
	print(algo.movelist)
	print('Current number of turns: ' + str(len(algo.movelist)))
	print('Solve time: ' + str(t1-t0)[:6] +' s')
	
# Calling Test
if __name__ == '__main__': 
    Main() 
