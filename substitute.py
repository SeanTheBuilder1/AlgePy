from sympy import symbols, solve, N, solveset, Eq
from sympy.parsing.sympy_parser import parse_expr

x, y = symbols('x y')

def calcSub():
    while True:
        try:
            xArr = []
            poly = input("Input polynomial\n")
            polyArc = poly
            while True:
                xIn = input("What is x array press = if end\n")
                if xIn == "=":
                    break
                else:
                    xArr.append(xIn)
                
            print("Results:\n")
            for xIn in xArr:
                poly = parse_expr(polyArc)
                poly = poly - y
                poly = poly.subs(x, xIn)
                print(xIn, '=', solve(poly, y))
            
            
            closer = str(input("\nEnter 1 to exit.\n"
            "Press any key to continue.\n"))
            if(closer == '1'):
                return
        except:
            print("Invalid Character")
        
if __name__ == "__main__":
	calcSub()