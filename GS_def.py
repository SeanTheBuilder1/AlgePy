from sympy import solveset, symbols, solve, N
from sys import stdout
An, An1, An2, A1, r, n, n1, n2, sm= symbols("An An1 An2 A1 r n n1 n2 sm")
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
			
			
			
def calcDefr():
	while True:
		try:
			an1In = input("An1 = ")
			an2In = input("An2 = ")
			n1In = int(input("n1 = "))
			n2In = int(input("n2 = "))
			nIn = n1In - n2In
			expr = (An1/An2)**(1/n) - (r**n)**(1/n)
			expr = expr.subs(An1, an1In)
			expr = expr.subs(An2, an2In)
			expr = expr.subs(n, nIn)
			print("\nResults: Restart or press Ctrl+C if taking too long")
			expr = solveset(expr, r)
			print("r^(1/", nIn, ") = (", an1In, " / ", an2In, ")^(1/", nIn, ")", sep='')
			print("r =", str(expr))
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
				expr = (An / A1) / (r**sm)
				expr = expr.subs(An, anIn)
				expr = expr.subs(A1, a1In)
				expr = expr.subs(r, rIn)
				expr = expr.subs(sm, sum)
				sol = N(expr)
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
			print("n =", sum)
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
			
def calcDefr2():
	while True:
		try:
			anIn = input("An = ")
			a1In = input("A1 = ")
			nIn = int(input("n = "))
			expr = (An / A1)**(1 / (n - 1)) - r
			expr = expr.subs(An, anIn)
			expr = expr.subs(A1, a1In)
			expr = expr.subs(n, nIn)
			expr = solveset(expr, r)
			print("\nResults:")
			print("r = (", anIn, " / ", a1In, ")**(1 / (", nIn, " - 1))", sep='')
			print("r =", str(expr))
			closer = str(input("\nEnter 1 to exit.\n"
			"Press any key to continue.\n"))
			if(closer == '1'):
				return
		except:
			print("Invalid Character")
			
			