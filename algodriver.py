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
	# algo.movelist = (['Fi', 'Li', '2U', 'Ri', '2D', 'F', '2D', 
		# '2B', 'Ri', 'Ui', 'D', 'Fi', 'Ri', 'Bi', '2F', 'Li', '2B'])
	# algo.followMoves()
	
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
