from sympy import solveset, symbols, N, solve
from sys import stdout
Sn, An, A1, r, n, sm= symbols("Sn An A1 r n  sm")

def calcSumSn():
	while True:
		try:
			formula = int(input("Press 1 if n is found\nPress 2 if An is found\nPress 3 to get infinite sum\n"))
			if formula == 1:
				a1In = input("A1 = ")
				nIn = input("n = ")
				rIn = input("r = ")
				expr = (A1 * (1 - r**n)) / (1-r) - Sn
				expr = expr.subs(A1, a1In)
				expr = expr.subs(n, nIn)
				expr = expr.subs(r, rIn)
				expr = solve(expr, Sn)
				print("\nResults:")
				print("Sn = (", a1In, " * (1 - ", rIn, "**", nIn, ")) / (1 - ", rIn, ")", sep='')
				print("Sn =", str(expr[0]))
				closer = str(input("\nEnter 1 to exit.\n"
				"Press any key to continue.\n"))
				if(closer == '1'):
					return
			elif formula == 2:
				anIn = input("An = ")
				a1In = input("A1 = ")
				rIn = input("r = ")
				expr = (A1 - (r * An)) / (1-r) - Sn
				expr = expr.subs(An, anIn)
				expr = expr.subs(A1, a1In)
				expr = expr.subs(r, rIn)
				expr = solve(expr, Sn)
				print("\nResults:")
				print("Sn = (", a1In, " - (", rIn, " * ", anIn, ")) / (1 - ", rIn, ")", sep='')
				print("Sn =", str(expr[0]))
				closer = str(input("\nEnter 1 to exit.\n"
				"Press any key to continue.\n"))
				if(closer == '1'):
					return
			elif formula == 3:
				a1In = input("A1 = ")
				rIn = input("r = ")
				expr = A1 / (1 - r) - Sn
				expr = expr.subs(A1, a1In)
				expr = expr.subs(r, rIn)
				expr = solve(expr, Sn)
				print("\nResults:")
				print("Sn = ", a1In, " / (1 - ", rIn, sep='')
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
			snIn = input("Sn = ")
			nIn = input("n = ")
			rIn = input("r = ")
			expr = (Sn * (1-r)) / (1 - (r**n)) - A1
			expr = expr.subs(Sn, snIn)
			expr = expr.subs(n, nIn)
			expr = expr.subs(r, rIn)
			expr = solveset(expr, A1)
			print("\nResults:")
			print("A1 = ", snIn, " * (1 -", rIn, ") / (1 - (", rIn, "**", nIn, "))", sep='')
			print("A1 =", str(expr))
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
	
def calcSumr():
	while True:
		try:
			snIn = input("Sn = ")
			anIn = input("An = ")
			a1In = input("A1 = ")
			expr = (A1 - Sn) / (-Sn +An) - r
			expr = expr.subs(Sn, snIn)
			expr = expr.subs(An, anIn)
			expr = expr.subs(A1, a1In)
			expr = solve(expr, r)
			print("\nResults:")
			print("r = (", a1In, " - ", snIn, ") / (-(", snIn, ") + ", anIn, ")", sep='')
			print("r =", str(expr[0]))
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
			a1In = input("A1 = ")
			rIn = int(input("r = "))
			print("\n")
			#expr = An/A1 - r**(n-1)
			#num = An / A1
			#num.subs(An, anIn)
			#num.subs(A1, a1In)
			sum = 0
			succ = True
			sol = 0
			while sol != 1:
				expr = (1 - Sn / ((A1) / (1 - r))) / (r**sm)
				expr = expr.subs(Sn, snIn)
				expr = expr.subs(A1, a1In)
				expr = expr.subs(r, rIn)
				expr = expr.subs(sm, sum)
				sol = float(N(expr))
				print('\r',str(sol), sep="", end="")
				stdout.flush()
				sum = sum + 1
				if sum % 100 == 0:
					print("",end="")
					closer = str(input("\nEnter 1 to cancel.\n"
					"Press any key to continue calculating\n"))
					if(closer == '1'):
						sum = "Failed to get n, cancelled"
						succ = False
						break
			print("\nResults:")
			if succ == True:
				print(rIn, "**(n - 1) = ", rIn, "**", sum - 1, sep= '')
			print("n =", sum - 1)
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
			
