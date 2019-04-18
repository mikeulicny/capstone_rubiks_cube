import numpy as np
from face import Face
from colorama import init, Back
init()

class Cube:
	# Initializer	
	def __init__(self, up, down, front, back, left, right):
		self.up = up
		self.down = down
		self.front = front
		self.back = back
		self.left = left
		self.right = right
		self.__getCheckSum()

	# Returns colorama 'object' based on cube color
	def toColor(self, cubelet):
		if cubelet == 'r':
			return Back.RED + '  ' + Back.RESET
		elif cubelet == 'g':
			return Back.GREEN + '  ' + Back.RESET
		elif cubelet == 'b':
			return Back.BLUE + '  ' + Back.RESET
		elif cubelet == 'y':
			return Back.YELLOW + '  ' + Back.RESET
		elif cubelet == 'w':
			return Back.WHITE + '  ' + Back.RESET		
		elif cubelet == 'o':
			return Back.MAGENTA + '  ' + Back.RESET

	# Internal function to generate checksum variable
	def __getCheckSum(self):
		faces = [self.up, self.down, self.front,
			self.back, self.left, self.right]		
		output = True
		
		colorSums = {'r':0, 'g':0, 'b':0, 'y':0, 'o':0, 'w':0}
		
		for face in faces:
			templist = [face.tl, face.tc, face.tr,
				face.ml, face.mc, face.mr, 
				face.bl, face.bc, face.br]
			for cubelet in templist:
				if cubelet == 'r':
					colorSums['r'] += 1
				elif cubelet == 'g':
					colorSums['g'] += 1
				elif cubelet == 'b':
					colorSums['b'] += 1		
				elif cubelet == 'y':
					colorSums['y'] += 1	
				elif cubelet == 'o':
					colorSums['o'] += 1	
				elif cubelet == 'w':
					colorSums['w'] += 1	
		for value in colorSums.values():
			if value != 9:
				output = False
		self.checkSumGood = output

	# Default print function (it's gross but compact)
	def __str__(self):
		u = self.up
		d = self.down
		f = self.front
		b = self.back
		l = self.left
		r = self.right
		toColor = self.toColor
		
		u1 = toColor(u.tl)
		u2 = toColor(u.tc)
		u3 = toColor(u.tr)
		u4 = toColor(u.ml)
		u5 = toColor(u.mc)
		u6 = toColor(u.mr)
		u7 = toColor(u.bl)
		u8 = toColor(u.bc)
		u9 = toColor(u.br)

		l1 = toColor(l.tl)
		l2 = toColor(l.tc)
		l3 = toColor(l.tr)
		l4 = toColor(l.ml)
		l5 = toColor(l.mc)
		l6 = toColor(l.mr)
		l7 = toColor(l.bl)
		l8 = toColor(l.bc)
		l9 = toColor(l.br)

		f1 = toColor(f.tl)
		f2 = toColor(f.tc)
		f3 = toColor(f.tr)
		f4 = toColor(f.ml)
		f5 = toColor(f.mc)
		f6 = toColor(f.mr)
		f7 = toColor(f.bl)
		f8 = toColor(f.bc)
		f9 = toColor(f.br)

		r1 = toColor(r.tl)
		r2 = toColor(r.tc)
		r3 = toColor(r.tr)
		r4 = toColor(r.ml)
		r5 = toColor(r.mc)
		r6 = toColor(r.mr)
		r7 = toColor(r.bl)
		r8 = toColor(r.bc)
		r9 = toColor(r.br)

		b1 = toColor(b.tl)
		b2 = toColor(b.tc)
		b3 = toColor(b.tr)
		b4 = toColor(b.ml)
		b5 = toColor(b.mc)
		b6 = toColor(b.mr)
		b7 = toColor(b.bl)
		b8 = toColor(b.bc)
		b9 = toColor(b.br)

		d1 = toColor(d.tl)
		d2 = toColor(d.tc)
		d3 = toColor(d.tr)
		d4 = toColor(d.ml)
		d5 = toColor(d.mc)
		d6 = toColor(d.mr)
		d7 = toColor(d.bl)
		d8 = toColor(d.bc)
		d9 = toColor(d.br)

		output = ('         ┏━━━━━━━━┓\n'+
			'         ┃ '+u1+u2+u3+' ┃\n'+ 
			'         ┃ '+u4+u5+u6+' ┃\n'+
			'         ┃ '+u7+u8+u9+' ┃\n'+
			'┏━━━━━━━━╋━━━━━━━━╋━━━━━━━━┳━━━━━━━━┓\n'+
			'┃ '+l1+l2+l3+' ┃ '+f1+f2+f3+' ┃ '+r1+r2+r3+' ┃ '+b1+b2+b3+' ┃\n'+
			'┃ '+l4+l5+l6+' ┃ '+f4+f5+f6+' ┃ '+r4+r5+r6+' ┃ '+b4+b5+b6+' ┃\n'+
			'┃ '+l7+l8+l9+' ┃ '+f7+f8+f9+' ┃ '+r7+r8+r9+' ┃ '+b7+b8+b9+' ┃\n'+
			'┗━━━━━━━━╋━━━━━━━━╋━━━━━━━━┻━━━━━━━━┛\n'+
			'         ┃ '+d1+d2+d3+' ┃\n'+ 
			'         ┃ '+d4+d5+d6+' ┃\n'+
			'         ┃ '+d7+d8+d9+' ┃\n'+
			'         ┗━━━━━━━━┛\n')
		return output	
				
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
		
		# turn('X')
		if dir == 'X':
			right.fill(right.cw())
			left.fill(left.ccw())
			temp.fill(back.c180())
			back.fill(up.c180())
			up.fill(front)
			front.fill(down)
			down.fill(temp)
		
		# turn('Xi')
		elif dir == 'Xi':
			left.fill(left.cw())
			right.fill(right.ccw())
			temp.fill(back.c180())
			back.fill(down.c180())
			down.fill(front)
			front.fill(up)
			up.fill(temp)
				
		# turn('Z')
		elif dir == 'Z':
			front.fill(front.cw())
			back.fill(back.ccw())
			temp.fill(up.cw())
			up.fill(left.cw())
			left.fill(down.cw())
			down.fill(right.cw())
			right.fill(temp)
			
		# turn('Zi')
		elif dir == 'Zi':
			back.fill(back.cw())
			front.fill(front.ccw())
			temp.fill(up.ccw())
			up.fill(right.ccw())
			right.fill(down.ccw())
			down.fill(left.ccw())
			left.fill(temp)			
		
		# turn('Y')
		elif dir == 'Y':
			up.fill(up.cw())
			down.fill(down.ccw())
			temp.fill(back)
			back.fill(left)
			left.fill(front)
			front.fill(right)
			right.fill(temp)
			
		# turn('Yi')
		elif dir == 'Yi':
			down.fill(down.cw())
			up.fill(up.ccw())
			temp.fill(back)
			back.fill(right)
			right.fill(front)
			front.fill(left)
			left.fill(temp)
		
		# turn('2X')
		elif dir == '2X':
			right.fill(right.c180())
			left.fill(left.c180())
			temp.fill(back.c180())
			back.fill(front.c180())
			front.fill(temp)
			temp.fill(up)
			up.fill(down)
			down.fill(temp)
			
		# turn('2Y')
		elif dir == '2Y':
			up.fill(up.c180())
			down.fill(down.c180())
			temp.fill(back)
			back.fill(front)
			front.fill(temp)
			temp.fill(left)
			left.fill(right)
			right.fill(temp)
		
		# turn('2Z')
		elif dir == '2Z':
			front.fill(front.c180())
			back.fill(back.c180())
			temp.fill(up.c180())
			up.fill(down.c180())
			down.fill(temp)
			temp.fill(right.c180())
			right.fill(left.c180())
			left.fill(temp)
		# turn('F')
		elif dir == 'F':
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
			right.fillEdge('t', temp)
			
		# turn('2D')
		elif dir == '2D':
			down.fill(down.c180())
			temp.fillEdge('b', front)
			front.fillEdge('b', back)
			back.fillEdge('b', temp)
			temp.fillEdge('b', left)
			left.fillEdge('b', right)
			right.fillEdge('b', temp)		
		
		# Endmatter
		# print('turn ' + dir)
		# print(self)
		# input('Press Enter to continue...')
		del temp
		return self