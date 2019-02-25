# On any given face mapping is as follows:

# 6 faces:
# up, front, left, back, right, down

# topLeft 		topCenter 		topRight
# middleLeft	middleCenter	middleRight
# bottomLeft	bottomCenter	bottomRight

# face.tl face.tc face.tr
# face.ml face.mc face.mr
# face.bl face.bc face.br

import numpy as np

class Face:
	# Initializer (either from faceArray or uninitialized)
	def __init__(self, faceArray = np.empty([3,3])):
		self.tl = faceArray[0,0]
		self.tc = faceArray[0,1]
		self.tr = faceArray[0,2]
		self.ml = faceArray[1,0]
		self.mc = faceArray[1,1]
		self.mr = faceArray[1,2]
		self.bl = faceArray[2,0]
		self.bc = faceArray[2,1]
		self.br = faceArray[2,2]

	# Checks if all edges are a color
	def allEdges(self, color):
		out = True
		if (self.ml != color or self.tc != color or
			self.mr != color or self.bc != color):
			out = False
		return out

	# Checks if all corners are a color		
	def allCrnrs(self, color):
		out = True
		if (self.tl != color or self.tr != color or
			self.bl != color or self.br != color):
			out = False
		return out	
	
	# Checks if face is all same color
	def isComplete(self):
		out = True
		if (self.tl != self.mc or self.tc != self.mc or self.tr != self.mc or
			self.ml != self.mc or self.mr != mc or
			self.bl != self.mc or self.bc != self.mc or self.br != self.mc):
			out = False
		return out

	# Rotates face clockwise
	def cw(self):
		temp = Face()
		self.tl, self.bl = self.bl, self.tl
		self.tc, self.ml = self.ml, self.tc
		self.tr, self.bl = self.bl, self.tr
		self.ml, self.bc = self.bc, self.ml
		self.bl, self.br = self.br, self.bl
		self.bc, self.mr = self.mr, self.bc
		temp.fill(self)
		return temp

	# Rotates face counter-clockwise		
	def ccw(self):
		temp = Face()
		self.tl, self.tr = self.tr, self.tl
		self.tc, self.mr = self.mr, self.tc
		self.tr, self.br = self.br, self.tr
		self.ml, self.mr = self.mr, self.ml
		self.bl, self.br = self.br, self.bl
		self.bc, self.mr = self.mr, self.bc
		temp.fill(self)
		return temp
	
	# Rotates face 180 degrees
	def c180(self):
		temp = Face()
		self.tl, self.br = self.br, self.tl
		self.tc, self.bc = self.bc, self.tc
		self.tr, self.bl = self.bl, self.tr
		self.ml, self.mr = self.mr, self.ml
		temp.fill(self)
		return temp
		
	# Fills face with values from another face	
	def fill(self, otherFace):
		self.tl = otherFace.tl
		self.tc = otherFace.tc
		self.tr = otherFace.tr
		self.ml = otherFace.ml
		self.mc = otherFace.mc
		self.mr = otherFace.mr
		self.bl = otherFace.bl
		self.bc = otherFace.bc
		self.br = otherFace.br
		return self
	
	# Fills one side of face with values from another face
	def fillEdge(self, edge, otherFace):
		if edge == 't':
			self.tl = otherFace.tl
			self.tc = otherFace.tc
			self.tr = otherFace.tr
		elif edge =='b':
			self.bl = otherFace.bl
			self.bc = otherFace.bc
			self.br = otherFace.br
		elif edge =='l':
			self.tl = otherFace.tl
			self.ml = otherFace.ml
			self.bl = otherFace.bl
		elif edge =='r':
			self.tr = otherFace.tr
			self.mr = otherFace.mr
			self.br = otherFace.br
		return self
