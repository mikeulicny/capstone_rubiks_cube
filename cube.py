import numpy as np
from face import Face

class Cube:		
	# Initializer	
	def __init__(self, up, down, front, back, left, right):
		self.up = up
		self.down = down
		self.front = front
		self.back = back
		self.left = left
		self.right = right
	
	# Default print function (it's gross but compact)
	def __str__(self):
		u = self.up
		d = self.down
		f = self.front
		b = self.back
		l = self.left
		r = self.right
		s = ' '
		g = s*8
		output=(g+'┏━━━━━━━┓\n'+
			g+'┃ '+u.tl+s+u.tc+s+u.tr+' ┃\n'+ 
			g+'┃ '+u.ml+s+u.mc+s+u.mr+' ┃\n'+
			g+'┃ '+u.bl+s+u.bc+s+u.br+' ┃\n'+
			'┏━━━━━━━╋━━━━━━━╋━━━━━━━┳━━━━━━━┓\n'+
			'┃ '+l.tl+s+l.tc+s+l.tr+' ┃ '+f.tl+s+f.tc+s+f.tr+s+
			'┃ '+r.tl+s+r.tc+s+r.tr+' ┃ '+b.tl+s+b.tc+s+b.tr+' ┃\n'+
			'┃ '+l.ml+s+l.mc+s+l.mr+' ┃ '+f.ml+s+f.mc+s+f.mr+s+
			'┃ '+r.ml+s+r.mc+s+r.mr+' ┃ '+b.ml+s+b.mc+s+b.mr+' ┃\n'+
			'┃ '+l.bl+s+l.bc+s+l.br+' ┃ '+f.bl+s+f.bc+s+f.br+s+
			'┃ '+r.bl+s+r.bc+s+r.br+' ┃ '+b.bl+s+b.bc+s+b.br+' ┃\n'+
			'┗━━━━━━━╋━━━━━━━╋━━━━━━━┻━━━━━━━┛\n'+
			g+'┃ '+d.tl+s+d.tc+s+d.tr+' ┃\n'+
			g+'┃ '+d.ml+s+d.mc+s+d.mr+' ┃\n'+
			g+'┃ '+d.bl+s+d.bc+s+d.br+' ┃\n'+
			g+'┗━━━━━━━┛\n')
		return output

	def flip(self, dir):
	
		# Simplify attributes
		up = self.up
		down = self.down
		front = self.front
		back = self.back
		left = self.left
		right = self.right
		
		# Create temp face for storage
		temp = Face()	
		
		# flip('X')
		if dir == 'X':
			right.fill(right.cw())
			left.fill(left.ccw())
			temp.fill(back.c180())
			back.fill(up.c180())
			up.fill(front)
			front.fill(down)
			down.fill(temp)
		
		# flip('Xi')
		elif dir == 'Xi':
			left.fill(left.cw())
			right.fill(right.ccw())
			temp.fill(back.c180())
			back.fill(down.c180())
			down.fill(front)
			front.fill(up)
			up.fill(temp)
				
		# flip('Z')
		elif dir == 'Z':
			front.fill(front.cw())
			back.fill(back.ccw())
			temp.fill(up.cw())
			up.fill(left.cw())
			left.fill(down.cw())
			down.fill(right.cw())
			right.fill(temp)
			
		# flip('Zi')
		elif dir == 'Zi':
			back.fill(back.cw())
			front.fill(front.ccw())
			temp.fill(up.ccw())
			up.fill(right.ccw())
			right.fill(down.ccw())
			down.fill(left.ccw())
			left.fill(temp)			
		
		# flip('Y')
		elif dir == 'Y':
			up.fill(up.cw())
			down.fill(down.ccw())
			temp.fill(back)
			back.fill(left)
			left.fill(front)
			front.fill(right)
			right.fill(temp)
			
		# flip('Yi')
		elif dir == 'Yi':
			down.fill(down.cw())
			up.fill(up.ccw())
			temp.fill(back)
			back.fill(right)
			right.fill(front)
			front.fill(left)
			left.fill(temp)
		
		# flip('2X')
		elif dir == '2X':
			right.fill(right.c180())
			left.fill(left.c180())
			temp.fill(back.c180())
			back.fill(front.c180())
			front.fill(temp)
			temp.fill(up)
			up.fill(down)
			down.fill(temp)
			
		# flip('2Y')
		elif dir == '2Y':
			up.fill(up.c180())
			down.fill(down.c180())
			temp.fill(back)
			back.fill(front)
			front.fill(temp)
			temp.fill(left)
			left.fill(right)
			right.fill(temp)
		
		# flip('2Z')
		elif dir == '2Z':
			front.fill(front.c180())
			back.fill(back.c180())
			temp.fill(up.c180())
			up.fill(down.c180())
			down.fill(temp)
			temp.fill(right.c180())
			right.fill(left.c180())
			left.fill(temp)
		
		# Endmatter
		print('Flip ' + dir)
		del temp
		return self
		
		# ------------------------------------------------------------------------
		# COMMENTS:		
		# Special composite (3 stage) flips (because of claw limitations)
		# flip('Y') = flip('Z') + flip('X') + flip('Zi')
		# flip('Yi') = flip('Z') + flip('Xi') + flip('Zi')
		
		# Special "180 degree" turns (for consistent code)
		# (The 2Y implementation is more efficient than 2 "flip('Y') calls)
		# flip('2X') = flip('X') + flip('X')
		# flip('2Y') = flip('Z') + flip('2X') + flip('Zi')
		# flip('2Z') = flip('Z') + flip('Z')		
		
		# flip('Y') and its variants 'Yi' and '2Y' would be more efficient
		# move-wise if they were instead represented by an internal re-mapping
		# of the faces (e.g. flip('Y') would actually just re-map the faces:
		# left = front, front = right, right = back, and back = left) and claws.
		# This would significantly cut down on the number of flips needed,
		# because 'Y' moves wouldn't actually turn the cube.
		# ------------------------------------------------------------------------

	def turn(self, dir):
		
		# Simplify attributes
		up = self.up
		down = self.down
		front = self.front
		back = self.back
		left = self.left
		right = self.right	
		
		# Create temp face for storage
		temp = Face()	
		
		# turn('F')
		if dir == 'F':
			front.fill(front.cw())
			temp.fillEdge('l', up.cw())
			up.fillEdge('b', left.cw())
			left.fillEdge('r', down.cw())
			down.fillEdge('t', right.cw())
			right.fillEdge('l', temp)
		
		# turn('Fi')
		elif dir == 'Fi':
			front.fill(front.ccw())
			temp.fillEdge('r', up.ccw())
			up.fillEdge('b', right.ccw())
			right.fillEdge('l', down.ccw())
			down.fillEdge('t', left.ccw())
			left.fillEdge('r', temp)
			
		# turn('B')
		elif dir == 'B':
			back.fill(back.cw())
			temp.fillEdge('l', up.ccw())
			up.fillEdge('t', right.ccw())
			right.fillEdge('r', down.ccw())
			down.fillEdge('b', left.ccw())
			left.fillEdge('l', temp)
			
		# turn('Bi')
		elif dir == 'Bi':
			back.fill(back.ccw())
			temp.fillEdge('r', up.cw())
			up.fillEdge('t', left.cw())
			left.fillEdge('l', down.cw())
			down.fillEdge('b', right.cw())
			right.fillEdge('r', temp)
			
		# turn('L')
		elif dir == 'L':
			left.fill(left.cw())
			temp.fillEdge('l', up)
			up.fillEdge('l', back.c180())
			back.fillEdge('r', down.c180())
			down.fillEdge('l', front)
			front.fillEdge('l', temp)

		# turn('Li')
		elif dir == 'Li':
			left.fill(left.ccw())
			temp.fillEdge('r', up.c180())
			up.fillEdge('l', front)
			front.fillEdge('l', down)
			down.fillEdge('l', back.c180())
			back.fillEdge('r', temp)
		
		# turn('R')
		elif dir == 'R':
			right.fill(right.cw())
			temp.fillEdge('l', up.c180())
			up.fillEdge('r', front)
			front.fillEdge('r', down)
			down.fillEdge('r', back.c180())
			back.fillEdge('l', temp)
		
		# turn('Ri')
		elif dir == 'Ri':
			right.fill(right.ccw())
			temp.fillEdge('r', up)
			up.fillEdge('r', back.c180())
			back.fillEdge('l', down.c180())
			down.fillEdge('r', front)
			front.fillEdge('r', temp)

		# turn('U')
		elif dir == 'U':
			up.fill(up.cw())
			temp.fillEdge('t', front)
			front.fillEdge('t', right)
			right.fillEdge('t', back)
			back.fillEdge('t', left)
			left.fillEdge('t', temp)
		
		# turn('Ui')
		elif dir == 'Ui':
			up.fill(up.ccw())
			temp.fillEdge('t', front)
			front.fillEdge('t', left)
			left.fillEdge('t', back)
			back.fillEdge('t', right)
			right.fillEdge('t', temp)
			
		# turn('D')
		elif dir == 'D':
			down.fill(down.cw())
			temp.fillEdge('b', front)
			front.fillEdge('b', left)
			left.fillEdge('b', back)
			back.fillEdge('b', right)
			right.fillEdge('b', temp)
			
		# turn('Di')
		elif dir == 'Di':
			down.fill(down.ccw())
			temp.fillEdge('b', front)
			front.fillEdge('b', right)
			right.fillEdge('b', back)
			back.fillEdge('b', left)
			left.fillEdge('b', temp)			
		
		# turn('2F')
		elif dir == '2F':
			front.fill(front.c180())
			temp.fillEdge('t', up.c180())
			up.fillEdge('b', down.c180())
			down.fillEdge('t', temp)
			temp.fillEdge('l', left.c180())
			left.fillEdge('r', right.c180())
			right.fillEdge('l', temp)
			
		# turn('2B')
		elif dir == '2B':
			back.fill(back.c180())
			temp.fillEdge('b', up.c180())
			up.fillEdge('t', down.c180())
			down.fillEdge('b', temp)
			temp.fillEdge('r', left.c180())
			left.fillEdge('l', right.c180())
			right.fillEdge('r', temp)
			
		# turn('2L')
		elif dir == '2L':
			left.fill(left.c180())
			temp.fillEdge('l', up)
			up.fillEdge('l', down)
			down.fillEdge('l', temp)
			temp.fillEdge('r', front.c180())
			front.fillEdge('l', back.c180())
			back.fillEdge('r', temp)
			
		# turn('2R')
		elif dir == '2R':
			right.fill(right.c180())
			temp.fillEdge('r', up)
			up.fillEdge('r', down)
			down.fillEdge('r', temp)
			temp.fillEdge('l', front.c180())
			front.fillEdge('r', back.c180())
			back.fillEdge('l', temp)
			
		# turn('2U')
		elif dir == '2U':
			up.fill(up.c180())
			temp.fillEdge('t', front)
			front.fillEdge('t', back)
			back.fillEdge('t', temp)
			temp.fillEdge('t', left)
			left.fillEdge('t', right)
			right.fillEdge('t', left)
			
		# turn('2D')
		elif dir == '2D':
			down.fill(down.c180())
			temp.fillEdge('b', front)
			front.fillEdge('b', back)
			back.fillEdge('b', temp)
			temp.fillEdge('b', left)
			left.fillEdge('b', right)
			right.fillEdge('b', left)		
		
		print('Turn ' + dir)
		del temp
		return self
		
		# ------------------------------------------------------------------------
		# COMMENTS:
		# example: 	turn('F') = turn front face clockwise
		#			turn('Li') = turn left face counter-clockwise ('inverse')
		
		# Special composite (3 stage) turns (because of claw limitations)
		# turn('U')	= flip('Z') + turn('R') + flip('Zi')
		# turn('Ui') = flip('Z') + turn('Ri') + flip('Zi')
		# turn('D') = flip('Z') + turn('L') + flip('Zi')
		# turn('Di') = flip('Z') + turn('Li') + flip('Zi')
		
		# Special "180 degree" turns (for consistent code)
		# (The 2U implementation is more efficient than 2 "turn('U') calls)
		# turn('2F') = turn('F') + turn('F')
		# turn('2B') = turn('B') + turn('B') 
		# turn('2L') = turn('L') + turn('L') 
		# turn('2R') = turn('R') + turn('R')
		# turn('2U') = flip('Z') + turn('2R') + flip('Zi')
		# turn('2D') = flip('Z') + turn('2L') + flip('Zi')
		
		# Up turns could also be done more efficiently by remapping the faces,
		# however this would likely be rather complicated and doing so nuanced.
		# ------------------------------------------------------------------------		

		
		
		
		
		
		
		
		