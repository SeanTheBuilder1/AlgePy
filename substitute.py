from sympy import symbols, solve, N, solveset, Eq
from sympy.parsing.sympy_parser import parse_expr

x, y = symbols('x y')

def calcSub():
    while True:
        try:
            poly = input("Input polynomial\n")
            xIn = input("What is x\n")
            poly = parse_expr(poly)
            poly = poly - y
            poly = poly.subs(x, xIn)
            print("Results:\n")
            print(solve(poly, y))
            closer = str(input("\nEnter 1 to exit.\n"
            "Press any key to continue.\n"))
            if(closer == '1'):
                return
        except:
            print("Invalid Character")
        
if __name__ == "__main__":
	calcSub()