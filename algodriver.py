import numpy as np
from face import Face
from cube import Cube
from algocfop import AlgoCFOP
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
	# algo = AlgoCFOP(cube, 1)	
	# algo.movelist = (['L', 'B', '2U', 'Li', 'U', 'Ri', 'Bi', 'Ri', 'Fi', '2D', '2U', '2L', 'D', '2L', 'D', '2L', 'Bi'])
	# algo.followMoves()
	algo.randomize()
	
	# Print initial cube
	print('Test from solved: y @ up, g @ front: ' + str(algo.movelist))
	# print('Before:\n')
	print(cube)
	
	# input('Press Enter to solve...')

	t0 = time.time()
	algo.solve()
	t1 = time.time()

	print('After:\n')
	print(cube)
	print(algo.movelist)
	print('Number of moves in list: ' + str(len(algo.movelist)))
	print('Actual number of turns by our bot: ' + str(algo.listLength))
	print('Time to generate solution: ' + str(t1-t0)[:6] +' s')
	
# Calling Test
if __name__ == '__main__': 
    Main() 
