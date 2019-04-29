#--------------------------------------------------------------
# ECE 4600 Capstone - Winter 2019
# Wayne State University
# Project: Rubik's Cube Solving Robot
# Primary author: Joseph Breitner
# Additional team members: Michael Ulicny, Joseph VanBuhler
#
# This is the main program to run the Rubik's Cube Solving
# Robot. When opened it creates a new Session and prompts the
# user in a while loop until the session is ended. Then the 
# program is terminated.
#--------------------------------------------------------------

from session import Session

# Start new session
session = Session()	

# While loop to keep session open 
X = True				
while X:
	session.printOptions()	# print session options
	X = session.prompt()	# test to resume / end session

