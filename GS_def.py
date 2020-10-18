from sympy import solveset, symbols, solve
An, A1, r, n= symbols("An A1 r n")
# An = a * (r**(n-1))

def calcDefAn():
	while True:
		try:
			a1In = input("A1 = ")
			rIn = input("r = ")
			nIn = int(input("n = "))
			expr = A1 * (r**(n -1)) - An
			expr = expr.subs(A1, a1In)
			expr = expr.subs(r, rIn)
			expr = expr.subs(n, nIn)
			value = []
			for i in range(nIn):
				sol = A1 * (r **(n)) - An
				sol = sol.subs(A1, a1In)
				sol = sol.subs(r, rIn)
				sol = sol.subs(n, i)
				sol = solve(sol, An)
				value.append(str(sol[0]))
			print("\nResults:")
			for i in range(len(value)):
				print(i + 1, " | ", value[i])
			expr = solve(expr, An)
			print("An = ", a1In, " * (", rIn, "^(", nIn, " - 1))", sep='')
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
			rIn = input("r = ")
			nIn = int(input("n = "))
			expr = An / r**(n-1) - A1
			expr = expr.subs(An, anIn)
			expr = expr.subs(r, rIn)
			expr = expr.subs(n, nIn)
			expr = solve(expr, A1)
			print("\nResults:")
			print("A1 = (", anIn, " / ", rIn, "^(", nIn, " - 1))", sep='')
			print("A1 =", str(expr[0]))
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
			
			