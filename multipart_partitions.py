from collections import namedtuple
from sympy import *


x, y = symbols('x y')
c_s, c_v, b_v, b_s = symbols('c_s c_v b_v b_s')

pi_block = x + y - c_s - 2 * c_v

mb = x + y - c_s - 2 * c_v
ma = x - c_s - c_v


r14 = Rational(1 / 4)
r34 = Rational(3 / 4)
r94 = Rational(9 / 4)

part = namedtuple(
    "part", "pre loc x_0 x_1 y_0 y_1 pi"
)

Case1a = [
    part(pre=2, loc=r14, x_0=b_v + b_s, x_1=r14, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, x_0=r14, x_1=r34, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=0, y_1=b_v, pi=ma),
    part(pre=1, loc=r14, y_0=b_v, y_1=b_v + b_s, x_0=b_s + 2 * b_v - y, x_1=r14, pi=mb),
    part(pre=1, loc=r14, x_0=b_v + b_s, x_1=r14, y_0=b_v, y_1=r14, pi=mb),
    part(pre=2, loc=r34, x_0=r14, x_1=r34, y_0=b_v, y_1=r14, pi=mb),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=b_v, y_1=r14, pi=mb),
    part(pre=1, loc=r94, x_0=r14, x_1=r34, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r34, x_0=r34, x_1=1, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]


Case1b = [
    part(pre=2, loc=r34, x_0=b_v+b_s, x_1=r34, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, x_0=b_s+2*b_v-y, x_1=b_s+b_v, y_0=b_v, y_1=r14, pi=mb),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=b_v, y_1=r14, pi=mb),
    part(pre=1, loc=r94, x_0=r14, x_1=b_s+2*b_v-r14, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r94, x_0=b_s+2*b_v-r14, x_1=r34, y_0=r14, y_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1c = [
    part(pre=2, loc=r34, x_0=b_v+b_s, x_1=r34, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, x_0=b_s+2*b_v-y, x_1=b_s+b_v, y_0=b_v, y_1=r14, pi=mb),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=b_v, y_1=r14, pi=mb),
    part(pre=1, loc=r94, x_0=r14, x_1=b_s+2*b_v-r14, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r94, x_0=b_s+2*b_v-r14, x_1=r34, y_0=r14, y_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1d = [
    part(pre=2, loc=r14, x_0=b_v+b_s, x_1=1, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, y_0=b_s+2*b_v-r14, y_1=r34, x_0=b_s+2*b_v-y,x_1=r14, pi=mb),
    part(pre=2, loc=r14, y_0=r34, y_1=b_s+b_v, x_0=b_s+2*b_v-y,x_1=r14, pi=mb),
    part(pre=2, loc=r14, x_0=b_s+b_v, x_1=1, y_0=b_v, y_1=r14, pi=mb),
    part(pre=1, loc=r94, y_0=r14, y_1=b_s+2*b_v-r14, x_0=b_s+2*b_v-y,x_1=r34, pi=mb),
    part(pre=1, loc=r94, x_0=b_s+2*b_v-r14, x_1=r34, y_0=r14, y_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1e = [
    part(pre=2, loc=r14, x_0=b_v+b_s, x_1=1, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, x_0=b_s+2*b_v-y, x_1=1, y_0=b_v, y_1=r14, pi=mb),
    part(pre=1, loc=r94, y_0=b_s+2*b_v-r34, y_1=r34, x_0=b_s+2*b_v-y,x_1=r34, pi=mb),
    part(pre=2, loc=r34, y_0=r34, y_1=b_s+2*b_v-r14, x_0=b_s+2*b_v-y,x_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=b_s+2*b_v-r14, x_1=1, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1f = [
    part(pre=2, loc=r14, y_0=b_s+2*b_v-r14, y_1=1, x_0=b_s+2*b_v-y,x_1=r14, pi=mb),
    part(pre=1, loc=r94, y_0=b_s+2*b_v-r34, y_1=r34, x_0=b_s+2*b_v-y,x_1=r34, pi=mb),
    part(pre=2, loc=r34, y_0=r34, y_1=b_s+2*b_v-r14, x_0=b_s+2*b_v-y,x_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=b_s+2*b_v-r14, x_1=1, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1g = [
    part(pre=2, loc=r94, y_0=b_s+2*b_v-r34, y_1=r34, x_0=b_s+2*b_v-y, x_1=r34, pi=mb),
    part(pre=1, loc=r34, y_0=r34, y_1=1, x_0=b_s+2*b_v-y,x_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1h = [
    part(pre=2, loc=r34, y_0=b_s+2*b_v-r34, y_1=1, x_0=b_s+2*b_v-y, x_1=r34, pi=mb),
    part(pre=1, loc=r14, y_0=r34, y_1=b_s+2*b_v-r34, x_0=b_s+2*b_v-y, x_1=1, pi=mb),
    part(pre=1, loc=r14, x_0=b_s+2*b_v-r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1i = [
    part(pre=1, loc=r14, y_0=b_s+2*b_v-1, y_1=1, x_0=b_s+2*b_v-y, x_1=1, pi=mb)
]

Case2a = [
    part(pre=2, loc=r34, x_0=b_s+b_v, x_1=r34, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r34, x_0=b_s+b_v, x_1=r34, y_0=r14, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=r14, y_1=b_v, pi=ma),
    part(pre=1, loc=r94, y_0=b_v, y_1=b_s+b_v, x_0=b_s+2*b_v-y, x_1=r34, pi=mb),
    part(pre=1, loc=r94, x_0=b_s+b_v, x_1=r34, y_0=b_v, y_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=b_v, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case2b = [
    part(pre=2, loc=r14, x_0=b_s+b_v, x_1=1, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r34, x_0=b_s+b_v, x_1=1, y_0=r14, y_1=b_v, pi=ma),
    part(pre=1, loc=r94, y_0=b_s+2*b_v-r34, y_1=r34, x_0=b_s+2*b_v-y, x_1=r34, pi=mb),
    part(pre=2, loc=r34, y_0=r34, y_1=b_s+b_v, x_0=b_s+2*b_v-y, x_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=b_s+b_v, x_1=1, y_0=b_v, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case2c = [
    part(pre=2, loc=r34, y_0=r34, y_1=1, x_0=b_s+2*b_v-y, x_1=r34, pi=mb),
    part(pre=1, loc=r94, y_0=b_s+2*b_v-r34, y_1=r34, x_0=b_s+2*b_v-y, x_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case2d = [
    part(pre=2, loc=r34, y_0=b_s+2*b_v-r34, y_1=1, x_0=b_s+2*b_v-y, x_1=r34, pi=mb),
    part(pre=1, loc=r14, y_0=r34, y_1=b_s+2*b_v-r34, x_0=b_s+2*b_v-y, x_1=1, pi=mb),
    part(pre=1, loc=r14, x_0=b_s+2*b_v-r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case2e = [
    part(pre=1, loc=r14, y_0=b_s+2*b_v-1, y_1=1, x_0=b_s+2*b_v-y, x_1=1, pi=mb)
]

Case3a = [
    part(pre=2, loc=r34, x_0=b_s+b_v, x_1=r34, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r34, x_0=b_s+b_v, x_1=r34, y_0=r14, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=r14, y_1=b_v, pi=ma),
    part(pre=1, loc=r94, y_0=b_v, y_1=b_s+b_v, x_0=b_s+2*b_v-y, x_1=r34, pi=mb),
    part(pre=1, loc=r94, x_0=b_s+b_v, x_1=r34, y_0=b_v, y_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=b_v, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case3b = [
    part(pre=2, loc=r14, x_0=b_s + b_v, x_1=1, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r34, x_0=b_s + b_v, x_1=1, y_0=r14, y_1=b_v, pi=ma),
    part(pre=1, loc=r94, y_0=b_s + 2 * b_v - r34, y_1=r34, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=2, loc=r34, y_0=r34, y_1=b_s + b_v, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=b_s + b_v, x_1=1, y_0=b_v, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case3c = [
    part(pre=2, loc=r14, x_0=b_s+b_v, x_1=1, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r34, x_0=b_s+b_v, x_1=1, y_0=r14, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, x_0=b_s+2*b_v-y, x_1=1, y_0=b_v, y_1=r34, pi=mb),
    part(pre=1, loc=r14, y_0=r34, y_1=b_s+2*b_v-r34, x_0=b_s+2*b_v-y, x_1=1, pi=mb),
    part(pre=1, loc=r14, x_0=b_s+2*b_v-r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case3d = [
    part(pre=2, loc=r34, y_0=b_s+2*b_v-r34, y_1=1, x_0=b_s+2*b_v-y, x_1=r34, pi=mb),
    part(pre=1, loc=r14, y_0=r34, y_1=b_s+2*b_v-r34, x_0=b_s+2*b_v-y, x_1=1, pi=mb),
    part(pre=1, loc=r14, x_0=b_s+2*b_v-r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case3e = [
    part(pre=1, loc=r14, y_0=b_s+2*b_v-1, y_1=1, x_0=b_s+2*b_v-y, x_1=1, pi=mb)
]

Case4a = [
    part(pre=2, loc=r14, x_0=b_s+b_v, x_1=1, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r34, x_0=b_s+b_v, x_1=1, y_0=r14, y_1=r34, pi=ma),
    part(pre=2, loc=r14, x_0=b_s+b_v, x_1=1, y_0=r34, y_1=b_v, pi=mb),
    part(pre=1, loc=r14, y_0=b_v, y_1=b_s+b_v, x_0=b_s+2*b_v-y, x_1=1, pi=mb),
    part(pre=1, loc=r14, x_0=b_s+b_v, x_1=1, y_0=b_v, y_1=1, pi=mb)
]

Case4b = [
    part(pre=1, loc=r14, y_0=b_s+2*b_v-1, y_1=1, x_0=b_s+2*b_v-y, x_1=1, pi=mb)
]
