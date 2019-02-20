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
	# Initializer
	def __init__(self, faceArray):
		self.tl = faceArray[0,0]
		self.tc = faceArray[0,1]
		self.tr = faceArray[0,2]
		self.ml = faceArray[1,0]
		self.mc = faceArray[1,1]
		self.mr = faceArray[1,2]
		self.bl = faceArray[2,0]
		self.bc = faceArray[2,1]
		self.br = faceArray[2,2]
		self.wholeFace = np.empty(shape=(3,3))
		self.edges = np.empty(shape=(1,4))
		self.crnrs = np.empty(shape=(1,4))
		
	def remap(self):
		self.wholeFace = np.array([[self.tl, self.tc, self.tr],
			[self.ml, self.mc, self.mr],
			[self.bl, self.bc, self.br]])
		self.edges = np.array([self.ml, self.tc, self.mr, self.bc])
		self.crnrs = np.array([self.tl, self.tr, self.br, self.bl])
	
	def allEdges(self, color):
		out = True
		for edge in self.edges:
			if edge != color:
				out = False
		return out
	
	def allCrnrs(self, color):
		out = True
		for crnr in self.crnrs:
			if crnr != color:
				out = False
		return out	
	
	def complete(self):
		out = True
		for cublet in self.wholeFace:
			if cubelet != self.mc:
				out = False
		return out
		
