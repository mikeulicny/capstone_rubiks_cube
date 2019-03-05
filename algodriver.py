import numpy as np
from face import Face
from cube import Cube
from algobasic import AlgoBasic
import time

def Main():				
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
	'''
	
	# Test cube 3:
	print('Test from solved: w @ up, r @ front: L B U Fi Ri L F Ri 2B')
	up = np.array([['b', 'g', 'b'],
		['o', 'w', 'y'],
		['b', 'r', 'g']])	
	front = np.array([['o', 'w', 'y'],
		['w', 'r', 'o'],
		['b', 'b', 'w']])
	left = np.array([['w', 'w', 'y'],
		['y', 'g', 'g'],
		['r', 'w', 'r']])
	down = np.array([['g', 'b', 'y'],
		['o', 'y', 'o'],
		['y', 'r', 'o']])
	back = np.array([['o', 'r', 'w'],
		['y', 'o', 'g'],
		['r', 'r', 'g']])
	right = np.array([['w', 'g', 'o'],
		['b', 'b', 'b'],
		['r', 'y', 'g']])	

	
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
	
	# Print initial cube
	print('Before:\n')
	print(cube)
	
	# input('Press Enter to solve...')
	algo = AlgoBasic(cube)
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