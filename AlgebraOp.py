from sympy import symbols, solve

a, b, c = symbols("a b c")

def Arith(mode):
	try:
		aIn = input("a = ")
		bIn = input("b = ")
		if mode == 1:
			expr = a + b - c
		elif mode == 2:
			expr = a - b - c
		elif mode == 3:
			expr = a * b - c
		elif mode == 4:
			expr = a / b - c
			if int(bIn) == 0:
				raise
		expr = expr.subs(a, aIn)
		expr = expr.subs(b, bIn)
		expr = solve(expr, c)
		print(expr)
		return
	except:
		print("Invalid Character")


def Init():
	while True:
		try:
			mode = int(input("1 to Add\n2 to Subtract\n3 to Multiply\n4 to Divide\n"))
			if 0 < mode < 5:
				Arith(mode)
			else:
				raise Stupid
		except:
			print('Invalid Character')
			
if __name__ == "__main__":
	Init()