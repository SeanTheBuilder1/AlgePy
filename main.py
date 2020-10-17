
from sympy import solveset, symbols
import AS_def
while True:
	try:
		mode = int(input("press 1 if an\npress 2 if sum\n"))
		if mode == 1:
			value = int(input("Press 1 or 2 or 3 or 4"))
			if value == 1:
				AS_def.calcDefAn()
			elif value == 2:
				AS_def.calcDefA1()
			elif value == 3:
				AS_def.calcDefn()
			elif value == 4:
				AS_def.calcDefd()
			else:
				raise(ValueError)
				
		elif mode == 2:
			value = int(input("Press 1 or 2 or 3 or 4"))
			"""if value == 1:
				
			elif value == 2:
				
			elif value == 3:
				
			elif value == 4:
				
			else:
				raise(ValueError)"""
		else:
			raise(ValueError)
	except:
		print("Invalid Character")