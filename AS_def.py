
A1, n, An, d = symbols("A1 n An d")
def calcDefAn():
	while True:
		try:
			a1In = input("A1 = ")
			nIn = input("n = ")
			dIn = input("d = ")
			expr = A1 + (n - 1) * d - An
			expr = expr.subs(A1, a1In)
			expr = expr.subs(n, nIn)
			expr = expr.subs(d, dIn)
			expr = solveset(expr, An)
			print("An = ", a1In, " + (", nIn, " - 1) * ", dIn, sep='')
			print(str(expr))
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
			
def calcDefA1():
	while True:
		try:
			anIn = input("An = ")
			nIn = input("n = ")
			dIn = input("d = ")
			expr = An - (n - 1) * d - A1
			expr = expr.subs(An, anIn)
			expr = expr.subs(n, nIn)
			expr = expr.subs(d, dIn)
			expr = solveset(expr, A1)
			print("A1 = ", anIn, " - (", nIn, " - 1) * ", dIn, sep='')
			print(str(expr))
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
			
			
def calcDefn():
	while True:
		try:
			anIn = input("An = ")
			a1In = input("A1 = ")
			dIn = input("d = ")
			expr = ((An - A1) / d) + 1 - n
			expr = expr.subs(An, anIn)
			expr = expr.subs(A1, a1In)
			expr = expr.subs(d, dIn)
			expr = solveset(expr, n)
			print("n = ((", anIn, " - ", a1In, ") / ", dIn, ") + 1", sep='')
			print(str(expr))
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
			
			
def calcDefd():
	while True:
		try:
			anIn = input("An = ")
			a1In = input("A1 = ")
			nIn = input("n = ")
			expr = (An - A1) / (n - 1) - d
			expr = expr.subs(An, anIn)
			expr = expr.subs(A1, a1In)
			expr = expr.subs(n, nIn)
			expr = solveset(expr, d)
			print("d = (", anIn, " - ", a1In, ") / (", nIn, " - 1)", sep='')
			print(str(expr))
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
			
