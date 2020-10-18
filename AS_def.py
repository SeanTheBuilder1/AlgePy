from sympy import symbols, solveset, solve
An, A1, n, d = symbols("An A1 n d")
def calcDefAn():
	while True:
		try:
			a1In = input("A1 = ")
			nIn = int(input("n = "))
			dIn = input("d = ")
			expr = A1 + (n - 1) * d - An
			expr = expr.subs(A1, a1In)
			expr = expr.subs(n, nIn)
			expr = expr.subs(d, dIn)
			value = []
			for i in range(nIn):
				sol = A1 + (n) * d - An
				sol = sol.subs(A1, a1In)
				sol = sol.subs(d, dIn)
				sol = sol.subs(n, i)
				sol = solve(sol, An)
				value.append(str(sol[0]))
			print("\nResults:")
			for i in range(len(value)):
				print(i + 1, " | ", value[i])
			expr = solve(expr, An)
			print("An = ", a1In, " + (", nIn, " - 1) * ", dIn, sep='')
			print("An =", str(expr[0]))
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
			expr = solve(expr, A1)
			print("\nResults:")
			print("A1 = ", anIn, " - (", nIn, " - 1) * ", dIn, sep='')
			print("A1 =", str(expr[0]))
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
			expr = solve(expr, n)
			print("\nResults:")
			print("n = ((", anIn, " - ", a1In, ") / ", dIn, ") + 1", sep='')
			print("n =", str(expr[0]))
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
			expr = solve(expr, d)
			print("\nResults:")
			print("d = (", anIn, " - ", a1In, ") / (", nIn, " - 1)", sep='')
			print("d =", str(expr[0]))
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
			
