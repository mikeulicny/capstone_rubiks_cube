# On any given face mapping is as follows:

# 6 faces:
# up, front, left, back, right, down

# topLeft 		topCenter 		topRight
# middleLeft	middleCenter	middleRight
# bottomLeft	bottomCenter	bottomRight

# face.tl face.tc face.tr
# face.ml face.mc face.mr
# face.bl face.bc face.br

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
	
	# Sub-arrays:
	wholeFace = np.array([[tl, tc, tr],[ml, mc, mr],[bl, bc, br]])
	edges = np.array([ml, tc, mr, bc])
	crnrs = np.array([tl, tr, br, bl])
	
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
				
	# def remap(self):	
		# wholeFace = ([[tl, tc, tr],[ml, mc, mr],[bl, bc, br]])
		# edges = np.array([ml, tc, mr, bc])
		# crnrs = np.array([tl, tr, br, bl])
		
