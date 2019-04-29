from session import Session

session = Session()

X = True
while X:
	session.printOptions()
	X = session.prompt()

