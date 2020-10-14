% ruletest4.al

FRAMES A, B
MOTIONVARIABLES Q{3}
SIMPROT(A, B, 1, Q3)
DCM = A_B
M = DCM*3 - A_B

VARIABLES R
CIRCLE_AREA = PI*R^2

VARIABLES U, A
VARIABLES X, Y
S = U*T - 1/2*A*T^2

EXPR1 = 2*A*0.5 - 1.25 + 0.25
EXPR2 = -X^2 + Y^2 + 0.25*(X+Y)^2
EXPR3 = 0.5E-10

DYADIC>> = A1>*A1> + A2>*A2> + A3>*A3>
