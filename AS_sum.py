from sympy import symbols, solveset, solve
Sn, An, A1, n, d= symbols("Sn An A1 n d")
def calcSumAn():
	while True:
		try:
			a1In = input("A1 = ")
			nIn = input("n = ")
			snIn = input("Sn = ")
			expr = (Sn / n) * 2 - A1 - An
			expr = expr.subs(A1, a1In)
			expr = expr.subs(n, nIn)
			expr = expr.subs(Sn, snIn)
			expr = solve(expr, An)
			print("\nResults:")
			print("An = (", snIn, " / ", nIn, ") * 2 - ", a1In, sep='')
			print("An =", str(expr[0]))
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
			
def calcSumSn():
	while True:
		try:
			formula = int(input("Press 1 if An is found\nPress 2 if d is found\n"))
			if formula == 1:
				anIn = input("An = ")
				a1In = input("A1 = ")
				nIn = input("n = ")
				expr = (n / 2) * (A1 + An) - Sn
				expr = expr.subs(An, anIn)
				expr = expr.subs(A1, a1In)
				expr = expr.subs(n, nIn)
				expr = solve(expr, Sn)
				print("\nResults:")
				print("Sn = (", nIn, " / 2) * (", a1In, " + ", anIn, ")", sep='')
				print("Sn =", str(expr[0]))
				closer = str(input("\nEnter 1 to exit.\n"
				"Press any key to continue.\n"))
				if(closer == '1'):
					return
			elif formula == 2:
				a1In = input("A1 = ")
				nIn = input("n = ")
				dIn = input("d = ")
				expr = (n / 2) * (2 * A1 + (n - 1) * d) - Sn
				expr = expr.subs(A1, a1In)
				expr = expr.subs(n, nIn)
				expr = expr.subs(d, dIn)
				expr = solve(expr, Sn)
				print("\nResults:")
				print("Sn = (", nIn, " / 2) * (2 * ", a1In, " + (", nIn, " -  1) * ", dIn, sep='')
				print("Sn =", str(expr[0]))
				closer = str(input("\nEnter 1 to exit.\n"
				"Press any key to continue.\n"))
				if(closer == '1'):
					return
			else:
				raise(ValueError)
		except:
			print("Invalid Character")
			
			
def calcSumA1():
	while True:
		try:
			formula = int(input("Press 1 if An is found\nPress 2 if d is found\n"))
			if formula == 1:
				snIn = input("Sn = ")
				anIn = input("An = ")
				nIn = input("n = ")
				expr = (Sn / n) * 2 - An - A1
				expr = expr.subs(Sn, snIn)
				expr = expr.subs(An, anIn)
				expr = expr.subs(n, nIn)
				expr = solve(expr, A1)
				print("\nResults:")
				print("A1 = (", snIn, " / ", nIn, ") * 2 - ", anIn, sep='')
				print("A1 =", str(expr[0]))
				closer = str(input("\nEnter 1 to exit.\n"
				"Press any key to continue.\n"))
				if(closer == '1'):
					return
			elif formula == 2:
				snIn = input("Sn = ")
				nIn = input("n = ")
				dIn = input("d = ")
				expr = (Sn / n - d * (n - 1) / 2) - A1
				expr = expr.subs(Sn, snIn)
				expr = expr.subs(n, nIn)
				expr = expr.subs(d, dIn)
				expr = solve(expr, A1)
				print("\nResults:")
				print("A1 = (", snIn, " / ", nIn, " - ", dIn, " * (", nIn, " - 1) / 2", sep='')
				print("A1 =", str(expr[0]))
				closer = str(input("\nEnter 1 to exit.\n"
				"Press any key to continue.\n"))
				if(closer == '1'):
					return
			else:
				raise(ValueError)
		except:
			print("Invalid Character")
			
def calcSumd():
	while True:
		try:
			snIn = input("Sn = ")
			a1In = input("A1 = ")
			nIn = input("n = ")
			expr = (-2 * (A1 - Sn / n) / (n - 1)) - d
			expr = expr.subs(A1, a1In)
			expr = expr.subs(n, nIn)
			expr = expr.subs(Sn, snIn)
			expr = solve(expr, d)
			print("\nResults:")
			print("d = (-2 * (", a1In, " - ", snIn, " / ", nIn, ") / (", nIn, " - 1))", sep='')
			print("d =", str(expr[0]))
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
			
			
def calcSumn():
	while True:
		try:
			snIn = input("Sn = ")
			anIn = input("An = ")
			a1In = input("A1 = ")
			expr = (2 * Sn / (A1 + An)) - n
			expr = expr.subs(Sn, snIn)
			expr = expr.subs(An, anIn)
			expr = expr.subs(A1, a1In)
			expr = solve(expr, n)
			print("\nResults:")
			print("n = (2 *", snIn, " / (", a1In, " + ", anIn, ")", sep='')
			print("n = ", str(expr[0]))
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
			
			