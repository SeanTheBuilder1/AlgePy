from sympy import solveset, symbols
import AS_def
import AS_sum
import GS_def
import GS_sum
while True:
	try:
		mode = int(input("Press 1 to use aritmetic sequence definition formula\nPress 2 to use sum of arithmetic sequence formula\nPress 3 to use geometric sequence definition formula\nPress 4 to use sum of geometric sequence formula\n"))
		if mode == 1:
			value = int(input("Press 1 to get An and generate sequence\nPress 2 to get A1\nPress 3 to get n\nPress 4 to get d\n"))
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
			value = int(input("Press 1 to get Sn\nPress 2 to get An\nPress 3 to get A1\nPress 4 to get n\nPress 5 to get d\n"))
			if value == 1:
				AS_sum.calcSumSn()
			elif value == 2:
				AS_sum.calcSumAn()
			elif value == 3:
				AS_sum.calcSumA1()
			elif value == 4:
				AS_sum.calcSumn()
			elif value == 5:
				AS_sum.calcSumd()
			else:
				raise(ValueError)
		elif mode == 3:
			value = int(input("Press 1 to get An and generate sequence\nPress 2 to get A1\nPress 3 to get n\nPress 4 to get r with 2 equations\nPress 5 to r with A1 & An\n"))
			if value == 1:
				GS_def.calcDefAn()
			elif value == 2:
				GS_def.calcDefA1()
			elif value == 3:
				GS_def.calcDefn()
			elif value == 4:
				GS_def.calcDefr()
			elif value == 5:
				GS_def.calcDefr2()
			else:
				raise(ValueError)
		elif mode == 4:
			value = int(input("Press 1 to get Sn\nPress 2 to get A1\nPress 3 to get r\nPress 4 to get n\n"))
			if value == 1:
				GS_sum.calcSumSn()
			elif value == 2:
				GS_sum.calcSumA1()
			elif value == 3:
				GS_sum.calcSumr()
			elif value == 4:
				GS_sum.calcSumn()
			else:
				raise(ValueError)
		else:
			raise(ValueError)
	except:
		print("Invalid Character")