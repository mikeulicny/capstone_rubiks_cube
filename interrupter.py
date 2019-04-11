import time

# Here's an example list (dummy class for reference)
class AlgoCFOP:
	def __init__(self, movelist):
		self.movelist = movelist
		
algo = AlgoCFOP(['B', 'L', 'Fi', 'Di', 'Ui', '2B', '2U', '2L', 'B', '2D', '2L', 'U', 'Li', 'Fi', 'R', 'L'])

# Runtime indicator flag
goodToGo = True

# Initial range parameter
liststart = 0
tempindex = 0

# Entering main loop of claw solving
while goodToGo == True:
	try:
		for i in range(liststart, len(algo.movelist)):
			tempindex = i
			
			# ####################################################
			# HAVE CLAW MOVE OCCUR HERE
			print('Move ' + str(i) + ': ' + str(algo.movelist[i]))
			time.sleep(0.5)
			# ####################################################
			
			# Loop terminator statement
			if tempindex == (len(algo.movelist) - 1):
				goodToGo = False

	# On a CTRL+C press:
	except KeyboardInterrupt:
		goodToGo = False
		print('-----------\nUSER PAUSE\n-----------')
		print('Type 0 and press Enter to resume.')
		extCommand = input('Type 1 - 10 and press Enter to repeat last n moves: ')
		if extCommand == '0':
			goodToGo = True
			# Set new list start to next movelist
			liststart = tempindex + 1
		elif extCommand in '1 2 3 4 5 6 7 8 9 10':
			goodToGo = True
			# Set new list start to next movelist
			liststart = tempindex - int(extCommand) + 1
		print('-----------\nUSER RESUME\n-----------')

input('Press Enter to exit program.')