from session import Session
from frame import Frame
import time
import re



#~ frame = Frame(clawDelay=0.3, rotateDelay90=0.5)
#~ frame.openClawsFB()
#~ input('xxx')
#~ frame.closeClawsFB()
#~ frame.openClawsLR()
#~ input('xxx')
#~ frame.closeClawsLR()

session = Session()
session.printOptions()
X = True
while X:

	X = session.prompt()

#~ moves = 'Z Fi Ri L B L Z 2Z Ri Z L Xi 2F R Fi 2X 2R B R Z 2Z 2B R B Ri L B Li B Ri Bi R Bi Ri B R B L 2B Li B X 2L Bi Li B Xi Bi Li Bi 2L B L B Li Bi Li Bi Li B Li'
#~ movelist = re.split(' ', moves)
#~ print(movelist)
#~ session.solveCube(movelist)

#~ time.sleep(1)

#~ frame.rotate90('Z', inverse=True)
#~ frame.turn90('F')
#~ frame.turn90('R', inverse=True)
#~ frame.turn90('B')
#~ frame.turn90('L', inverse=True)
#~ frame.turn90('F', inverse=True)
#~ frame.turn90('R')
#~ frame.turn90('B', inverse=True)
#~ frame.turn90('L')

#~ time.sleep(1)

#~ frame.turn180('F')
#~ frame.turn180('R')
#~ frame.turn180('B')
#~ frame.turn180('L')

#~ time.sleep(1)



#~ time.sleep(1)

#~ frame.turn90('F')
#~ frame.turn90('R')
#~ frame.turn90('B')
#~ frame.turn90('L')

#~ time.sleep(1)

#~ frame.turn90('F', inverse=True)
#~ frame.turn90('R', inverse=True)
#~ frame.turn90('B', inverse=True)
#~ frame.turn90('L', inverse=True)

#~ time.sleep(1)

#~ frame.rotate90('X')
#~ frame.rotate90('Z')

#~ frame.rotate90('X', inverse=True)
#~ frame.rotate90('Z', inverse=True)

#~ frame.rotate180('X')
#~ frame.rotate180('Z')

#~ frame.rotate180('X', inverse=True)
#~ frame.rotate180('Z', inverse=True)

#~ time.sleep(1)

#~ frame.turn90('D')
#~ frame.turn90('U')

#~ time.sleep(1)

#~ frame.turn90('D', inverse=True)
#~ frame.turn90('U', inverse=True)
