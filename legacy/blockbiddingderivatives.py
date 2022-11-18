from sympy import *

s, v, b = symbols('s v b')

first = (-2 * b ** 3 - 24 * s - 48 * v + 3 * s * b ** 2 + 6 * b ** 2 * v + 24) / 24
first_diff = diff(first, b)


f = open("block step", "r")

i = 0
for l in f:
    i += 1
    if i%2 == 0:
        # print(i, l)
        eq = diff(l, b)
        # print(latex(eq))
        print(f"$${latex(roots(eq, b))}$$")


print(latex(roots(Rational(1/2) * (b * (-2 + s) + s + 2 * v), b)))
