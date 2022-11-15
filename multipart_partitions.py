import dataclasses
from collections import namedtuple
from typing import Any

from sympy import *

x, y = symbols('x y')
c_s, c_v, b_v, b_s = symbols('c_s c_v b_v b_s')

pi_block = x + y - c_s - 2 * c_v

mb = x + y - c_s - 2 * c_v
ma = x - c_s - c_v
mc = y - c_s - c_v

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
    part(pre=1, loc=r14, x_0=b_s + 2 * b_v - y, x_1=r14, y_0=b_v, y_1=b_v + b_s, pi=mb),
    part(pre=1, loc=r14, x_0=b_v + b_s, x_1=r14, y_0=b_v, y_1=r14, pi=mb),
    part(pre=2, loc=r34, x_0=r14, x_1=r34, y_0=b_v, y_1=r14, pi=mb),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=b_v, y_1=r14, pi=mb),
    part(pre=1, loc=r94, x_0=r14, x_1=r34, y_0=r14, y_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]


Case1b = [
    part(pre=2, loc=r34, x_0=b_v + b_s, x_1=r34, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=0, y_1=b_v, pi=ma),
    part(pre=1, loc=r14, x_0=b_s + 2 * b_v - y, x_1=r14, y_0=b_s + 2 * b_v - r14, y_1=r14, pi=mb),
    part(pre=2, loc=r34, x_0=b_s + 2 * b_v - y, x_1=r14, y_0=r14, y_1=b_s + b_v, pi=mb),
    part(pre=2, loc=r14, x_0=b_s + b_v, x_1=r34, y_0=b_v, y_1=r14, pi=mb),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=b_v, y_1=r14, pi=mb),
    part(pre=1, loc=r94, x_0=r14, x_1=r34, y_0=r14, y_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1c = [
    part(pre=2, loc=r34, x_0=b_v + b_s, x_1=r34, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, x_0=b_s + 2 * b_v - y, x_1=r34, y_0=b_v, y_1=r14, pi=mb),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=b_v, y_1=r14, pi=mb),
    part(pre=1, loc=r94, x_0=r14, x_1=b_s + 2 * b_v - r14, y_0=b_s + 2 * b_v - x, y_1=r34, pi=mb),
    part(pre=1, loc=r94, x_0=b_s + 2 * b_v - r14, x_1=r34, y_0=r14, y_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1d = [
    part(pre=2, loc=r14, x_0=b_v + b_s, x_1=1, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, y_0=b_s + 2 * b_v - r14, y_1=r34, x_0=b_s + 2 * b_v - y, x_1=r14, pi=mb),
    part(pre=2, loc=r14, y_0=r34, y_1=b_s + b_v, x_0=b_s + 2 * b_v - y, x_1=r14, pi=mb),
    part(pre=2, loc=r14, x_0=b_s + b_v, x_1=1, y_0=b_v, y_1=r14, pi=mb),
    part(pre=1, loc=r94, y_0=r14, y_1=b_s + 2 * b_v - r14, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=1, loc=r94, x_0=b_s + 2 * b_v - r14, x_1=r34, y_0=r14, y_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1e = [
    part(pre=2, loc=r14, x_0=b_v + b_s, x_1=1, y_0=0, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, x_0=b_s + 2 * b_v - y, x_1=1, y_0=b_v, y_1=r14, pi=mb),
    part(pre=1, loc=r94, y_0=b_s + 2 * b_v - r34, y_1=r34, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=2, loc=r34, y_0=r34, y_1=b_s + 2 * b_v - r14, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=b_s + 2 * b_v - r14, x_1=1, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1f = [
    part(pre=2, loc=r14, y_0=b_s + 2 * b_v - r14, y_1=1, x_0=b_s + 2 * b_v - y, x_1=r14, pi=mb),
    part(pre=1, loc=r94, y_0=b_s + 2 * b_v - r34, y_1=r34, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=2, loc=r34, y_0=r34, y_1=b_s + 2 * b_v - r14, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=b_s + 2 * b_v - r14, x_1=1, y_0=r14, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1g = [
    part(pre=2, loc=r94, y_0=b_s + 2 * b_v - r34, y_1=r34, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=1, loc=r34, y_0=r34, y_1=1, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1h = [
    part(pre=2, loc=r34, y_0=b_s + 2 * b_v - r34, y_1=1, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=1, loc=r14, y_0=r34, y_1=b_s + 2 * b_v - r34, x_0=b_s + 2 * b_v - y, x_1=1, pi=mb),
    part(pre=1, loc=r14, x_0=b_s + 2 * b_v - r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case1i = [
    part(pre=1, loc=r14, y_0=b_s + 2 * b_v - 1, y_1=1, x_0=b_s + 2 * b_v - y, x_1=1, pi=mb)
]

Case2a = [
    part(pre=2, loc=r34, x_0=b_s + b_v, x_1=r34, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r34, x_0=b_s + b_v, x_1=r34, y_0=r14, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=r14, y_1=b_v, pi=ma),
    part(pre=1, loc=r94, y_0=b_v, y_1=b_s + b_v, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=1, loc=r94, x_0=b_s + b_v, x_1=r34, y_0=b_v, y_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=b_v, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case2b = [
    part(pre=2, loc=r14, x_0=b_s + b_v, x_1=1, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r34, x_0=b_s + b_v, x_1=1, y_0=r14, y_1=b_v, pi=ma),
    part(pre=1, loc=r94, y_0=b_s + 2 * b_v - r34, y_1=r34, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=2, loc=r34, y_0=r34, y_1=b_s + b_v, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=2, loc=r34, x_0=b_s + b_v, x_1=1, y_0=b_v, y_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case2c = [
    part(pre=2, loc=r34, y_0=r34, y_1=1, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=1, loc=r94, y_0=b_s + 2 * b_v - r34, y_1=r34, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=1, loc=r14, x_0=r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case2d = [
    part(pre=2, loc=r34, y_0=b_s + 2 * b_v - r34, y_1=1, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=1, loc=r14, y_0=r34, y_1=b_s + 2 * b_v - r34, x_0=b_s + 2 * b_v - y, x_1=1, pi=mb),
    part(pre=1, loc=r14, x_0=b_s + 2 * b_v - r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case2e = [
    part(pre=1, loc=r14, y_0=b_s + 2 * b_v - 1, y_1=1, x_0=b_s + 2 * b_v - y, x_1=1, pi=mb)
]

Case3a = [
    part(pre=2, loc=r34, x_0=b_s + b_v, x_1=r34, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r14, x_0=r34, x_1=1, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r34, x_0=b_s + b_v, x_1=r34, y_0=r14, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, x_0=r34, x_1=1, y_0=r14, y_1=b_v, pi=ma),
    part(pre=1, loc=r94, y_0=b_v, y_1=b_s + b_v, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=1, loc=r94, x_0=b_s + b_v, x_1=r34, y_0=b_v, y_1=r34, pi=mb),
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
    part(pre=2, loc=r14, x_0=b_s + b_v, x_1=1, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r34, x_0=b_s + b_v, x_1=1, y_0=r14, y_1=b_v, pi=ma),
    part(pre=2, loc=r34, x_0=b_s + 2 * b_v - y, x_1=1, y_0=b_v, y_1=r34, pi=mb),
    part(pre=1, loc=r14, y_0=r34, y_1=b_s + 2 * b_v - r34, x_0=b_s + 2 * b_v - y, x_1=1, pi=mb),
    part(pre=1, loc=r14, x_0=b_s + 2 * b_v - r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case3d = [
    part(pre=2, loc=r34, y_0=b_s + 2 * b_v - r34, y_1=1, x_0=b_s + 2 * b_v - y, x_1=r34, pi=mb),
    part(pre=1, loc=r14, y_0=r34, y_1=b_s + 2 * b_v - r34, x_0=b_s + 2 * b_v - y, x_1=1, pi=mb),
    part(pre=1, loc=r14, x_0=b_s + 2 * b_v - r34, x_1=1, y_0=r34, y_1=1, pi=mb)
]

Case3e = [
    part(pre=1, loc=r14, y_0=b_s + 2 * b_v - 1, y_1=1, x_0=b_s + 2 * b_v - y, x_1=1, pi=mb)
]

Case4a = [
    part(pre=2, loc=r14, x_0=b_s + b_v, x_1=1, y_0=0, y_1=r14, pi=ma),
    part(pre=2, loc=r34, x_0=b_s + b_v, x_1=1, y_0=r14, y_1=r34, pi=ma),
    part(pre=2, loc=r14, x_0=b_s + b_v, x_1=1, y_0=r34, y_1=b_v, pi=mb),
    part(pre=1, loc=r14, y_0=b_v, y_1=b_s + b_v, x_0=b_s + 2 * b_v - y, x_1=1, pi=mb),
    part(pre=1, loc=r14, x_0=b_s + b_v, x_1=1, y_0=b_v, y_1=1, pi=mb)
]

Case4b = [
    part(pre=1, loc=r14, y_0=b_s + 2 * b_v - 1, y_1=1, x_0=b_s + 2 * b_v - y, x_1=1, pi=mb)
]

cases = [{
    "b_v": (0, 0.25),
    "b_ss": [{
        "b_s": (0, 0.25 - b_v),
        "areas": Case1a
    }, {
        "b_s": (0.25 - b_v, 0.5 - 2 * b_v),
        "areas": Case1b
    }, {
        "b_s": (0.5 - 2 * b_v, 0.75 - b_v),
        "areas": Case1c
    }, {
        "b_s": (0.75 - b_v, 1 - 2 * b_v),
        "areas": Case1d
    }, {
        "b_s": (1 - 2 * b_v, 1 - b_v),
        "areas": Case1e
    }, {
        "b_s": (1 - b_v, 1.25 - 2 * b_v),
        "areas": Case1f
    }, {
        "b_s": (1.25 - 2 * b_v, 1.5 - 2 * b_v),
        "areas": Case1g
    }, {
        "b_s": (1.5 - 2 * b_v, 1.75 - 2 * b_v),
        "areas": Case1h
    }, {
        "b_s": (1.75 - 2 * b_v, 2 - 2 * b_v),
        "areas": Case1i
    }],
}, {
    "b_v": (0.25, 0.5),
    "b_ss": [{
        "b_s": (0, 0.75 - b_v),
        "areas": Case2a
    }, {
        "b_s": (0.75 - b_v, 1 - b_v),
        "areas": Case2b
    }, {
        "b_s": (1 - b_v, 1.5 - 2 * b_v),
        "areas": Case2c
    }, {
        "b_s": (1.5 - 2 * b_v, 1.75 - 2 * b_v),
        "areas": Case2d
    }, {
        "b_s": (1.75 - 2 * b_v, 2 - 2 * b_v),
        "areas": Case2e
    }],
}, {
    "b_v": (0.5, 0.75),
    "b_ss": [{
        "b_s": (0, 0.75 - b_v),
        "areas": Case3a
    }, {
        "b_s": (0.75 - b_v, 1.5 - 2 * b_v),
        "areas": Case3b
    }, {
        "b_s": (1.5 - 2 * b_v, 1 - b_v),
        "areas": Case3c
    }, {
        "b_s": (1 - b_v, 1.75 - 2 * b_v),
        "areas": Case3d
    }, {
        "b_s": (1.75 - 2 * b_v, 2 - 2 * b_v),
        "areas": Case3e
    }],
}, {
    "b_v": (0.75, 1),
    "b_ss": [{
        "b_s": (0, 1 - b_v),
        "areas": Case4a
    }, {
        "b_s": (1 - b_v, 2 - 2 * b_v),
        "areas": Case4b
    }],
}]

expressions = [{'b_ss': [{
    'areas': -b_s ** 3 / 12 - b_s ** 2 * b_v / 2 + b_s ** 2 * c_s / 8 + b_s ** 2 * c_v / 4 - b_s * b_v ** 2 / 2 + b_s * b_v * c_s / 2 + b_s * b_v * c_v / 2 + b_v ** 2 * c_s / 4 - b_v ** 2 / 2 + b_v * c_v - c_s - 2 * c_v + 1,
    'b_s': (0, 0.25 - b_v)},
    {
        'areas': -5 * b_s ** 3 / 12 - 3 * b_s ** 2 * b_v + 5 * b_s ** 2 * c_s / 8 + 5 * b_s ** 2 * c_v / 4 + b_s ** 2 / 4 - 5 * b_s * b_v ** 2 + 7 * b_s * b_v * c_s / 2 + 11 * b_s * b_v * c_v / 2 + 3 * b_s * b_v / 4 - b_s * c_s / 2 - b_s * c_v - 7 * b_v ** 3 / 3 + 11 * b_v ** 2 * c_s / 4 + 4 * b_v ** 2 * c_v + 3 * b_v ** 2 / 8 - 3 * b_v * c_s / 2 - 7 * b_v * c_v / 4 + b_v / 4 - 3 * c_s / 4 - 3 * c_v / 2 + 115 / 128,
        'b_s': (0.25 - b_v, 0.5 - 2 * b_v)},
    {
        'areas': -3 * b_s ** 2 * b_v / 4 - 3 * b_s * b_v ** 2 / 4 + 3 * b_s * b_v * c_s / 2 + 3 * b_s * b_v * c_v / 2 - 3 * b_s * b_v / 8 + 3 * b_s / 64 + b_v ** 3 / 2 + 3 * b_v ** 2 * c_s / 4 - 5 * b_v ** 2 / 8 - 3 * b_v * c_s / 4 - b_v * c_v / 4 + 15 * b_v / 32 - 27 * c_s / 32 - 27 * c_v / 16 + 113 / 128,
        'b_s': (0.5 - 2 * b_v, 0.75 - b_v)},
    {
        'areas': -5 * b_s ** 3 / 12 - 5 * b_s ** 2 * b_v / 2 + 5 * b_s ** 2 * c_s / 8 + 5 * b_s ** 2 * c_v / 4 - 9 * b_s * b_v ** 2 / 2 + 5 * b_s * b_v * c_s / 2 + 9 * b_s * b_v * c_v / 2 - 8 * b_v ** 3 / 3 + 9 * b_v ** 2 * c_s / 4 + 4 * b_v ** 2 * c_v - b_v ** 2 / 4 + b_v * c_v / 2 - 9 * c_s / 8 - 9 * c_v / 4 + 67 / 64,
        'b_s': (0.75 - b_v, 1 - 2 * b_v)},
    {
        'areas': b_s ** 3 / 4 + 2 * b_s ** 2 * b_v - 3 * b_s ** 2 * c_s / 8 - 3 * b_s ** 2 * c_v / 4 - 9 * b_s ** 2 / 8 + 11 * b_s * b_v ** 2 / 2 - 5 * b_s * b_v * c_s / 2 - 11 * b_s * b_v * c_v / 2 - 9 * b_s * b_v / 2 + 9 * b_s * c_s / 4 + 9 * b_s * c_v / 2 + 9 * b_v ** 3 / 2 - 13 * b_v ** 2 * c_s / 4 - 7 * b_v ** 2 * c_v - 21 * b_v ** 2 / 4 + 11 * b_v * c_s / 2 + 23 * b_v * c_v / 2 - b_v / 2 - 77 * c_s / 32 - 77 * c_v / 16 + 197 / 128,
        'b_s': (1 - 2 * b_v, 1 - b_v)},
    {
        'areas': 5 * b_s ** 3 / 12 + 5 * b_s ** 2 * b_v / 2 - 5 * b_s ** 2 * c_s / 8 - 5 * b_s ** 2 * c_v / 4 - 5 * b_s ** 2 / 4 + 5 * b_s * b_v ** 2 - 5 * b_s * b_v * c_s / 2 - 5 * b_s * b_v * c_v - 5 * b_s * b_v + 5 * b_s * c_s / 2 + 5 * b_s * c_v + 10 * b_v ** 3 / 3 - 5 * b_v ** 2 * c_s / 2 - 5 * b_v ** 2 * c_v - 5 * b_v ** 2 + 5 * b_v * c_s + 10 * b_v * c_v - 19 * c_s / 8 - 19 * c_v / 4 + 281 / 192,
        'b_s': (1 - b_v, 1.25 - 2 * b_v)},
    {
        'areas': 3 * b_s ** 3 / 2 + 9 * b_s ** 2 * b_v - 9 * b_s ** 2 * c_s / 4 - 9 * b_s ** 2 * c_v / 2 - 111 * b_s ** 2 / 32 + 18 * b_s * b_v ** 2 - 9 * b_s * b_v * c_s - 18 * b_s * b_v * c_v - 111 * b_s * b_v / 8 + 111 * b_s * c_s / 16 + 111 * b_s * c_v / 8 + 12 * b_v ** 3 - 9 * b_v ** 2 * c_s - 18 * b_v ** 2 * c_v - 111 * b_v ** 2 / 8 + 111 * b_v * c_s / 8 + 111 * b_v * c_v / 4 - 689 * c_s / 128 - 689 * c_v / 64 + 1437 / 512,
        'b_s': (1.25 - 2 * b_v, 1.5 - 2 * b_v)},
    {
        'areas': 5 * b_s ** 3 / 12 + 5 * b_s ** 2 * b_v / 2 - 5 * b_s ** 2 * c_s / 8 - 5 * b_s ** 2 * c_v / 4 - 9 * b_s ** 2 / 8 + 5 * b_s * b_v ** 2 - 5 * b_s * b_v * c_s / 2 - 5 * b_s * b_v * c_v - 9 * b_s * b_v / 2 + 9 * b_s * c_s / 4 + 9 * b_s * c_v / 2 + 10 * b_v ** 3 / 3 - 5 * b_v ** 2 * c_s / 2 - 5 * b_v ** 2 * c_v - 9 * b_v ** 2 / 2 + 9 * b_v * c_s / 2 + 9 * b_v * c_v - 65 * c_s / 32 - 65 * c_v / 16 + 157 / 128,
        'b_s': (1.5 - 2 * b_v, 1.75 - 2 * b_v)},
    {
        'areas': b_s ** 3 / 12 + b_s ** 2 * b_v / 2 - b_s ** 2 * c_s / 8 - b_s ** 2 * c_v / 4 - b_s ** 2 / 4 + b_s * b_v ** 2 - b_s * b_v * c_s / 2 - b_s * b_v * c_v - b_s * b_v + b_s * c_s / 2 + b_s * c_v + 2 * b_v ** 3 / 3 - b_v ** 2 * c_s / 2 - b_v ** 2 * c_v - b_v ** 2 + b_v * c_s + 2 * b_v * c_v - c_s / 2 - c_v + 1 / 3,
        'b_s': (1.75 - 2 * b_v, 2 - 2 * b_v)}],
    'b_v': (0, 0.25)},
    {'b_ss': [{
        'areas': -3 * b_s ** 3 / 4 - 3 * b_s ** 2 * b_v + 9 * b_s ** 2 * c_s / 8 + 9 * b_s ** 2 * c_v / 4 - 3 * b_s * b_v ** 2 / 2 + 3 * b_s * b_v * c_s / 2 + 3 * b_s * b_v * c_v / 2 + 3 * b_v ** 3 / 2 - 3 * b_v ** 2 * c_s / 4 - 3 * b_v ** 2 * c_v - 15 * b_v ** 2 / 8 + 9 * b_v * c_s / 4 + 6 * b_v * c_v - 27 * b_v / 32 - 3 * c_s / 2 - 49 * c_v / 16 + 163 / 128,
        'b_s': (0, 0.75 - b_v)},
        {
            'areas': b_s ** 3 / 4 + 3 * b_s ** 2 * b_v / 2 - 3 * b_s ** 2 * c_s / 8 - 3 * b_s ** 2 * c_v / 4 - b_s ** 2 + 9 * b_s * b_v ** 2 / 2 - 3 * b_s * b_v * c_s / 2 - 9 * b_s * b_v * c_v / 2 - 17 * b_s * b_v / 4 + 2 * b_s * c_s + 17 * b_s * c_v / 4 + 4 * b_v ** 3 - 9 * b_v ** 2 * c_s / 4 - 6 * b_v ** 2 * c_v - 41 * b_v ** 2 / 8 + 17 * b_v * c_s / 4 + 41 * b_v * c_v / 4 - 69 * c_s / 32 - 73 * c_v / 16 + 181 / 128,
            'b_s': (0.75 - b_v, 1 - b_v)},
        {
            'areas': 3 * b_s ** 3 / 4 + 9 * b_s ** 2 * b_v / 2 - 9 * b_s ** 2 * c_s / 8 - 9 * b_s ** 2 * c_v / 4 - 15 * b_s ** 2 / 8 + 9 * b_s * b_v ** 2 - 9 * b_s * b_v * c_s / 2 - 9 * b_s * b_v * c_v - 15 * b_s * b_v / 2 + 15 * b_s * c_s / 4 + 15 * b_s * c_v / 2 + 6 * b_v ** 3 - 9 * b_v ** 2 * c_s / 2 - 9 * b_v ** 2 * c_v - 15 * b_v ** 2 / 2 + 15 * b_v * c_s / 2 + 15 * b_v * c_v - 101 * c_s / 32 - 101 * c_v / 16 + 229 / 128,
            'b_s': (1 - b_v, 1.5 - 2 * b_v)},
        {
            'areas': 5 * b_s ** 3 / 12 + 5 * b_s ** 2 * b_v / 2 - 5 * b_s ** 2 * c_s / 8 - 5 * b_s ** 2 * c_v / 4 - 9 * b_s ** 2 / 8 + 5 * b_s * b_v ** 2 - 5 * b_s * b_v * c_s / 2 - 5 * b_s * b_v * c_v - 9 * b_s * b_v / 2 + 9 * b_s * c_s / 4 + 9 * b_s * c_v / 2 + 10 * b_v ** 3 / 3 - 5 * b_v ** 2 * c_s / 2 - 5 * b_v ** 2 * c_v - 9 * b_v ** 2 / 2 + 9 * b_v * c_s / 2 + 9 * b_v * c_v - 65 * c_s / 32 - 65 * c_v / 16 + 157 / 128,
            'b_s': (1.5 - 2 * b_v, 1.75 - 2 * b_v)},
        {
            'areas': b_s ** 3 / 12 + b_s ** 2 * b_v / 2 - b_s ** 2 * c_s / 8 - b_s ** 2 * c_v / 4 - b_s ** 2 / 4 + b_s * b_v ** 2 - b_s * b_v * c_s / 2 - b_s * b_v * c_v - b_s * b_v + b_s * c_s / 2 + b_s * c_v + 2 * b_v ** 3 / 3 - b_v ** 2 * c_s / 2 - b_v ** 2 * c_v - b_v ** 2 + b_v * c_s + 2 * b_v * c_v - c_s / 2 - c_v + 1 / 3,
            'b_s': (1.75 - 2 * b_v, 2 - 2 * b_v)}],
        'b_v': (0.25, 0.5)},
    {'b_ss': [{
        'areas': -3 * b_s ** 3 / 4 - 3 * b_s ** 2 * b_v + 9 * b_s ** 2 * c_s / 8 + 9 * b_s ** 2 * c_v / 4 - 3 * b_s * b_v ** 2 / 2 + 3 * b_s * b_v * c_s / 2 + 3 * b_s * b_v * c_v / 2 + 3 * b_v ** 3 / 2 - 3 * b_v ** 2 * c_s / 4 - 3 * b_v ** 2 * c_v - 15 * b_v ** 2 / 8 + 9 * b_v * c_s / 4 + 6 * b_v * c_v - 27 * b_v / 32 - 3 * c_s / 2 - 49 * c_v / 16 + 163 / 128,
        'b_s': (0, 0.75 - b_v)},
        {
            'areas': b_s ** 3 / 4 + 3 * b_s ** 2 * b_v / 2 - 3 * b_s ** 2 * c_s / 8 - 3 * b_s ** 2 * c_v / 4 - b_s ** 2 + 9 * b_s * b_v ** 2 / 2 - 3 * b_s * b_v * c_s / 2 - 9 * b_s * b_v * c_v / 2 - 17 * b_s * b_v / 4 + 2 * b_s * c_s + 17 * b_s * c_v / 4 + 4 * b_v ** 3 - 9 * b_v ** 2 * c_s / 4 - 6 * b_v ** 2 * c_v - 41 * b_v ** 2 / 8 + 17 * b_v * c_s / 4 + 41 * b_v * c_v / 4 - 69 * c_s / 32 - 73 * c_v / 16 + 181 / 128,
            'b_s': (0.75 - b_v, 1.5 - 2 * b_v)},
        {
            'areas': -b_s ** 3 / 12 - b_s ** 2 * b_v / 2 + b_s ** 2 * c_s / 8 + b_s ** 2 * c_v / 4 - b_s ** 2 / 4 + b_s * b_v ** 2 / 2 + b_s * b_v * c_s / 2 - b_s * b_v * c_v / 2 - 5 * b_s * b_v / 4 + b_s * c_s / 2 + 5 * b_s * c_v / 4 + 4 * b_v ** 3 / 3 - b_v ** 2 * c_s / 4 - 2 * b_v ** 2 * c_v - 17 * b_v ** 2 / 8 + 5 * b_v * c_s / 4 + 17 * b_v * c_v / 4 - 33 * c_s / 32 - 37 * c_v / 16 + 109 / 128,
            'b_s': (1.5 - 2 * b_v, 1 - b_v)},
        {
            'areas': 5 * b_s ** 3 / 12 + 5 * b_s ** 2 * b_v / 2 - 5 * b_s ** 2 * c_s / 8 - 5 * b_s ** 2 * c_v / 4 - 9 * b_s ** 2 / 8 + 5 * b_s * b_v ** 2 - 5 * b_s * b_v * c_s / 2 - 5 * b_s * b_v * c_v - 9 * b_s * b_v / 2 + 9 * b_s * c_s / 4 + 9 * b_s * c_v / 2 + 10 * b_v ** 3 / 3 - 5 * b_v ** 2 * c_s / 2 - 5 * b_v ** 2 * c_v - 9 * b_v ** 2 / 2 + 9 * b_v * c_s / 2 + 9 * b_v * c_v - 65 * c_s / 32 - 65 * c_v / 16 + 157 / 128,
            'b_s': (1 - b_v, 1.75 - 2 * b_v)},
        {
            'areas': b_s ** 3 / 12 + b_s ** 2 * b_v / 2 - b_s ** 2 * c_s / 8 - b_s ** 2 * c_v / 4 - b_s ** 2 / 4 + b_s * b_v ** 2 - b_s * b_v * c_s / 2 - b_s * b_v * c_v - b_s * b_v + b_s * c_s / 2 + b_s * c_v + 2 * b_v ** 3 / 3 - b_v ** 2 * c_s / 2 - b_v ** 2 * c_v - b_v ** 2 + b_v * c_s + 2 * b_v * c_v - c_s / 2 - c_v + 1 / 3,
            'b_s': (1.75 - 2 * b_v, 2 - 2 * b_v)}],
        'b_v': (0.5, 0.75)},
    {'b_ss': [{
        'areas': -b_s ** 3 / 12 - b_s ** 2 * b_v / 2 + b_s ** 2 * c_s / 8 + b_s ** 2 * c_v / 4 - b_s ** 2 / 4 - 3 * b_s * b_v ** 2 / 4 + b_s * b_v * c_s / 2 + b_s * b_v * c_v - b_s * b_v / 2 + b_s * c_s / 2 + b_s * c_v / 8 + 9 * b_s / 64 - b_v ** 3 / 4 + b_v ** 2 * c_s / 4 + b_v ** 2 * c_v / 2 - b_v ** 2 / 4 + b_v * c_s / 2 + b_v * c_v / 8 + 9 * b_v / 64 - 3 * c_s / 4 - 5 * c_v / 8 + 23 / 64,
        'b_s': (0, 1 - b_v)},
        {
            'areas': b_s ** 3 / 12 + b_s ** 2 * b_v / 2 - b_s ** 2 * c_s / 8 - b_s ** 2 * c_v / 4 - b_s ** 2 / 4 + b_s * b_v ** 2 - b_s * b_v * c_s / 2 - b_s * b_v * c_v - b_s * b_v + b_s * c_s / 2 + b_s * c_v + 2 * b_v ** 3 / 3 - b_v ** 2 * c_s / 2 - b_v ** 2 * c_v - b_v ** 2 + b_v * c_s + 2 * b_v * c_v - c_s / 2 - c_v + 1 / 3,
            'b_s': (1 - b_v, 2 - 2 * b_v)}],
        'b_v': (0.75, 1)}]


def area_1(b_v_, b_s_, c_v_, c_s_):
    return -b_s_ ** 3 / 12 - b_s_ ** 2 * b_v_ / 2 + b_s_ ** 2 * c_s_ / 8 + b_s_ ** 2 * c_v_ / 4 - b_s_ * b_v_ ** 2 / 2 + b_s_ * b_v_ * c_s_ / 2 + b_s_ * b_v_ * c_v_ / 2 + b_v_ ** 2 * c_s_ / 4 - b_v_ ** 2 / 2 + b_v_ * c_v_ - c_s_ - 2 * c_v_ + 1,


def area_2(b_v_, b_s_, c_v_, c_s_):
    return -b_s_ ** 3 / 6 - 3 * b_s_ ** 2 * b_v_ / 2 + 5 * b_s_ ** 2 * c_s_ / 8 + b_s_ ** 2 * c_v_ / 2 + b_s_ ** 2 / 16 - 2 * b_s_ * b_v_ ** 2 + 7 * b_s_ * b_v_ * c_s_ / 2 + 5 * b_s_ * b_v_ * c_v_ / 2 - b_s_ * c_s_ / 2 - b_s_ * c_v_ / 4 + b_s_ / 32 - 7 * b_v_ ** 3 / 12 + 11 * b_v_ ** 2 * c_s_ / 4 + 7 * b_v_ ** 2 * c_v_ / 4 - 3 * b_v_ ** 2 / 8 - 3 * b_v_ * c_s_ / 2 - 5 * b_v_ * c_v_ / 8 + 23 * b_v_ / 64 - 25 * c_s_ / 32 - 109 * c_v_ / 64 + 175 / 192,


def area_3(b_v_, b_s_, c_v_, c_s_):
    return -3 * b_s_ ** 2 * b_v_ / 4 - 3 * b_s_ * b_v_ ** 2 / 4 + 3 * b_s_ * b_v_ * c_s_ / 2 + 3 * b_s_ * b_v_ * c_v_ / 2 - 3 * b_s_ * b_v_ / 8 + 3 * b_s_ / 64 + b_v_ ** 3 / 2 + 3 * b_v_ ** 2 * c_s_ / 4 - 5 * b_v_ ** 2 / 8 - 3 * b_v_ * c_s_ / 4 - b_v_ * c_v_ / 4 + 15 * b_v_ / 32 - 27 * c_s_ / 32 - 27 * c_v_ / 16 + 113 / 128,


def area_4(b_v_, b_s_, c_v_, c_s_):
    return -5 * b_s_ ** 3 / 12 - 5 * b_s_ ** 2 * b_v_ / 2 + 5 * b_s_ ** 2 * c_s_ / 8 + 5 * b_s_ ** 2 * c_v_ / 4 - 9 * b_s_ * b_v_ ** 2 / 2 + 5 * b_s_ * b_v_ * c_s_ / 2 + 9 * b_s_ * b_v_ * c_v_ / 2 - 8 * b_v_ ** 3 / 3 + 9 * b_v_ ** 2 * c_s_ / 4 + 4 * b_v_ ** 2 * c_v_ - b_v_ ** 2 / 4 + b_v_ * c_v_ / 2 - 9 * c_s_ / 8 - 9 * c_v_ / 4 + 67 / 64,


def area_5(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 4 + 2 * b_s_ ** 2 * b_v_ - 3 * b_s_ ** 2 * c_s_ / 8 - 3 * b_s_ ** 2 * c_v_ / 4 - 9 * b_s_ ** 2 / 8 + 11 * b_s_ * b_v_ ** 2 / 2 - 5 * b_s_ * b_v_ * c_s_ / 2 - 11 * b_s_ * b_v_ * c_v_ / 2 - 9 * b_s_ * b_v_ / 2 + 9 * b_s_ * c_s_ / 4 + 9 * b_s_ * c_v_ / 2 + 9 * b_v_ ** 3 / 2 - 13 * b_v_ ** 2 * c_s_ / 4 - 7 * b_v_ ** 2 * c_v_ - 21 * b_v_ ** 2 / 4 + 11 * b_v_ * c_s_ / 2 + 23 * b_v_ * c_v_ / 2 - b_v_ / 2 - 77 * c_s_ / 32 - 77 * c_v_ / 16 + 197 / 128,


def area_6(b_v_, b_s_, c_v_, c_s_):
    return 5 * b_s_ ** 3 / 12 + 5 * b_s_ ** 2 * b_v_ / 2 - 5 * b_s_ ** 2 * c_s_ / 8 - 5 * b_s_ ** 2 * c_v_ / 4 - 5 * b_s_ ** 2 / 4 + 5 * b_s_ * b_v_ ** 2 - 5 * b_s_ * b_v_ * c_s_ / 2 - 5 * b_s_ * b_v_ * c_v_ - 5 * b_s_ * b_v_ + 5 * b_s_ * c_s_ / 2 + 5 * b_s_ * c_v_ + 10 * b_v_ ** 3 / 3 - 5 * b_v_ ** 2 * c_s_ / 2 - 5 * b_v_ ** 2 * c_v_ - 5 * b_v_ ** 2 + 5 * b_v_ * c_s_ + 10 * b_v_ * c_v_ - 19 * c_s_ / 8 - 19 * c_v_ / 4 + 281 / 192,


def area_7(b_v_, b_s_, c_v_, c_s_):
    return 3 * b_s_ ** 3 / 2 + 9 * b_s_ ** 2 * b_v_ - 9 * b_s_ ** 2 * c_s_ / 4 - 9 * b_s_ ** 2 * c_v_ / 2 - 111 * b_s_ ** 2 / 32 + 18 * b_s_ * b_v_ ** 2 - 9 * b_s_ * b_v_ * c_s_ - 18 * b_s_ * b_v_ * c_v_ - 111 * b_s_ * b_v_ / 8 + 111 * b_s_ * c_s_ / 16 + 111 * b_s_ * c_v_ / 8 + 12 * b_v_ ** 3 - 9 * b_v_ ** 2 * c_s_ - 18 * b_v_ ** 2 * c_v_ - 111 * b_v_ ** 2 / 8 + 111 * b_v_ * c_s_ / 8 + 111 * b_v_ * c_v_ / 4 - 689 * c_s_ / 128 - 689 * c_v_ / 64 + 1437 / 512,


def area_8(b_v_, b_s_, c_v_, c_s_):
    return 5 * b_s_ ** 3 / 12 + 5 * b_s_ ** 2 * b_v_ / 2 - 5 * b_s_ ** 2 * c_s_ / 8 - 5 * b_s_ ** 2 * c_v_ / 4 - 9 * b_s_ ** 2 / 8 + 5 * b_s_ * b_v_ ** 2 - 5 * b_s_ * b_v_ * c_s_ / 2 - 5 * b_s_ * b_v_ * c_v_ - 9 * b_s_ * b_v_ / 2 + 9 * b_s_ * c_s_ / 4 + 9 * b_s_ * c_v_ / 2 + 10 * b_v_ ** 3 / 3 - 5 * b_v_ ** 2 * c_s_ / 2 - 5 * b_v_ ** 2 * c_v_ - 9 * b_v_ ** 2 / 2 + 9 * b_v_ * c_s_ / 2 + 9 * b_v_ * c_v_ - 65 * c_s_ / 32 - 65 * c_v_ / 16 + 157 / 128,


def area_9(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 12 + b_s_ ** 2 * b_v_ / 2 - b_s_ ** 2 * c_s_ / 8 - b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 / 4 + b_s_ * b_v_ ** 2 - b_s_ * b_v_ * c_s_ / 2 - b_s_ * b_v_ * c_v_ - b_s_ * b_v_ + b_s_ * c_s_ / 2 + b_s_ * c_v_ + 2 * b_v_ ** 3 / 3 - b_v_ ** 2 * c_s_ / 2 - b_v_ ** 2 * c_v_ - b_v_ ** 2 + b_v_ * c_s_ + 2 * b_v_ * c_v_ - c_s_ / 2 - c_v_ + 1 / 3,


def area_10(b_v_, b_s_, c_v_, c_s_):
    return -3 * b_s_ ** 3 / 4 - 3 * b_s_ ** 2 * b_v_ + 9 * b_s_ ** 2 * c_s_ / 8 + 9 * b_s_ ** 2 * c_v_ / 4 - 3 * b_s_ * b_v_ ** 2 / 2 + 3 * b_s_ * b_v_ * c_s_ / 2 + 3 * b_s_ * b_v_ * c_v_ / 2 + 3 * b_v_ ** 3 / 2 - 3 * b_v_ ** 2 * c_s_ / 4 - 3 * b_v_ ** 2 * c_v_ - 15 * b_v_ ** 2 / 8 + 9 * b_v_ * c_s_ / 4 + 6 * b_v_ * c_v_ - 27 * b_v_ / 32 - 3 * c_s_ / 2 - 49 * c_v_ / 16 + 163 / 128,


def area_11(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 4 + 3 * b_s_ ** 2 * b_v_ / 2 - 3 * b_s_ ** 2 * c_s_ / 8 - 3 * b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 + 9 * b_s_ * b_v_ ** 2 / 2 - 3 * b_s_ * b_v_ * c_s_ / 2 - 9 * b_s_ * b_v_ * c_v_ / 2 - 17 * b_s_ * b_v_ / 4 + 2 * b_s_ * c_s_ + 17 * b_s_ * c_v_ / 4 + 4 * b_v_ ** 3 - 9 * b_v_ ** 2 * c_s_ / 4 - 6 * b_v_ ** 2 * c_v_ - 41 * b_v_ ** 2 / 8 + 17 * b_v_ * c_s_ / 4 + 41 * b_v_ * c_v_ / 4 - 69 * c_s_ / 32 - 73 * c_v_ / 16 + 181 / 128,


def area_12(b_v_, b_s_, c_v_, c_s_):
    return 3 * b_s_ ** 3 / 4 + 9 * b_s_ ** 2 * b_v_ / 2 - 9 * b_s_ ** 2 * c_s_ / 8 - 9 * b_s_ ** 2 * c_v_ / 4 - 15 * b_s_ ** 2 / 8 + 9 * b_s_ * b_v_ ** 2 - 9 * b_s_ * b_v_ * c_s_ / 2 - 9 * b_s_ * b_v_ * c_v_ - 15 * b_s_ * b_v_ / 2 + 15 * b_s_ * c_s_ / 4 + 15 * b_s_ * c_v_ / 2 + 6 * b_v_ ** 3 - 9 * b_v_ ** 2 * c_s_ / 2 - 9 * b_v_ ** 2 * c_v_ - 15 * b_v_ ** 2 / 2 + 15 * b_v_ * c_s_ / 2 + 15 * b_v_ * c_v_ - 101 * c_s_ / 32 - 101 * c_v_ / 16 + 229 / 128,


def area_13(b_v_, b_s_, c_v_, c_s_):
    return 5 * b_s_ ** 3 / 12 + 5 * b_s_ ** 2 * b_v_ / 2 - 5 * b_s_ ** 2 * c_s_ / 8 - 5 * b_s_ ** 2 * c_v_ / 4 - 9 * b_s_ ** 2 / 8 + 5 * b_s_ * b_v_ ** 2 - 5 * b_s_ * b_v_ * c_s_ / 2 - 5 * b_s_ * b_v_ * c_v_ - 9 * b_s_ * b_v_ / 2 + 9 * b_s_ * c_s_ / 4 + 9 * b_s_ * c_v_ / 2 + 10 * b_v_ ** 3 / 3 - 5 * b_v_ ** 2 * c_s_ / 2 - 5 * b_v_ ** 2 * c_v_ - 9 * b_v_ ** 2 / 2 + 9 * b_v_ * c_s_ / 2 + 9 * b_v_ * c_v_ - 65 * c_s_ / 32 - 65 * c_v_ / 16 + 157 / 128,


def area_14(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 12 + b_s_ ** 2 * b_v_ / 2 - b_s_ ** 2 * c_s_ / 8 - b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 / 4 + b_s_ * b_v_ ** 2 - b_s_ * b_v_ * c_s_ / 2 - b_s_ * b_v_ * c_v_ - b_s_ * b_v_ + b_s_ * c_s_ / 2 + b_s_ * c_v_ + 2 * b_v_ ** 3 / 3 - b_v_ ** 2 * c_s_ / 2 - b_v_ ** 2 * c_v_ - b_v_ ** 2 + b_v_ * c_s_ + 2 * b_v_ * c_v_ - c_s_ / 2 - c_v_ + 1 / 3,


def area_15(b_v_, b_s_, c_v_, c_s_):
    return -3 * b_s_ ** 3 / 4 - 3 * b_s_ ** 2 * b_v_ + 9 * b_s_ ** 2 * c_s_ / 8 + 9 * b_s_ ** 2 * c_v_ / 4 - 3 * b_s_ * b_v_ ** 2 / 2 + 3 * b_s_ * b_v_ * c_s_ / 2 + 3 * b_s_ * b_v_ * c_v_ / 2 + 3 * b_v_ ** 3 / 2 - 3 * b_v_ ** 2 * c_s_ / 4 - 3 * b_v_ ** 2 * c_v_ - 15 * b_v_ ** 2 / 8 + 9 * b_v_ * c_s_ / 4 + 6 * b_v_ * c_v_ - 27 * b_v_ / 32 - 3 * c_s_ / 2 - 49 * c_v_ / 16 + 163 / 128,


def area_16(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 4 + 3 * b_s_ ** 2 * b_v_ / 2 - 3 * b_s_ ** 2 * c_s_ / 8 - 3 * b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 + 9 * b_s_ * b_v_ ** 2 / 2 - 3 * b_s_ * b_v_ * c_s_ / 2 - 9 * b_s_ * b_v_ * c_v_ / 2 - 17 * b_s_ * b_v_ / 4 + 2 * b_s_ * c_s_ + 17 * b_s_ * c_v_ / 4 + 4 * b_v_ ** 3 - 9 * b_v_ ** 2 * c_s_ / 4 - 6 * b_v_ ** 2 * c_v_ - 41 * b_v_ ** 2 / 8 + 17 * b_v_ * c_s_ / 4 + 41 * b_v_ * c_v_ / 4 - 69 * c_s_ / 32 - 73 * c_v_ / 16 + 181 / 128,


def area_17(b_v_, b_s_, c_v_, c_s_):
    return -b_s_ ** 3 / 12 - b_s_ ** 2 * b_v_ / 2 + b_s_ ** 2 * c_s_ / 8 + b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 / 4 + b_s_ * b_v_ ** 2 / 2 + b_s_ * b_v_ * c_s_ / 2 - b_s_ * b_v_ * c_v_ / 2 - 5 * b_s_ * b_v_ / 4 + b_s_ * c_s_ / 2 + 5 * b_s_ * c_v_ / 4 + 4 * b_v_ ** 3 / 3 - b_v_ ** 2 * c_s_ / 4 - 2 * b_v_ ** 2 * c_v_ - 17 * b_v_ ** 2 / 8 + 5 * b_v_ * c_s_ / 4 + 17 * b_v_ * c_v_ / 4 - 33 * c_s_ / 32 - 37 * c_v_ / 16 + 109 / 128,


def area_18(b_v_, b_s_, c_v_, c_s_):
    return 5 * b_s_ ** 3 / 12 + 5 * b_s_ ** 2 * b_v_ / 2 - 5 * b_s_ ** 2 * c_s_ / 8 - 5 * b_s_ ** 2 * c_v_ / 4 - 9 * b_s_ ** 2 / 8 + 5 * b_s_ * b_v_ ** 2 - 5 * b_s_ * b_v_ * c_s_ / 2 - 5 * b_s_ * b_v_ * c_v_ - 9 * b_s_ * b_v_ / 2 + 9 * b_s_ * c_s_ / 4 + 9 * b_s_ * c_v_ / 2 + 10 * b_v_ ** 3 / 3 - 5 * b_v_ ** 2 * c_s_ / 2 - 5 * b_v_ ** 2 * c_v_ - 9 * b_v_ ** 2 / 2 + 9 * b_v_ * c_s_ / 2 + 9 * b_v_ * c_v_ - 65 * c_s_ / 32 - 65 * c_v_ / 16 + 157 / 128,


def area_19(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 12 + b_s_ ** 2 * b_v_ / 2 - b_s_ ** 2 * c_s_ / 8 - b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 / 4 + b_s_ * b_v_ ** 2 - b_s_ * b_v_ * c_s_ / 2 - b_s_ * b_v_ * c_v_ - b_s_ * b_v_ + b_s_ * c_s_ / 2 + b_s_ * c_v_ + 2 * b_v_ ** 3 / 3 - b_v_ ** 2 * c_s_ / 2 - b_v_ ** 2 * c_v_ - b_v_ ** 2 + b_v_ * c_s_ + 2 * b_v_ * c_v_ - c_s_ / 2 - c_v_ + 1 / 3,


def area_20(b_v_, b_s_, c_v_, c_s_):
    return -b_s_ ** 3 / 12 - b_s_ ** 2 * b_v_ / 2 + b_s_ ** 2 * c_s_ / 8 + b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 / 4 - 3 * b_s_ * b_v_ ** 2 / 4 + b_s_ * b_v_ * c_s_ / 2 + b_s_ * b_v_ * c_v_ - b_s_ * b_v_ / 2 + b_s_ * c_s_ / 2 + b_s_ * c_v_ / 8 + 9 * b_s_ / 64 - b_v_ ** 3 / 4 + b_v_ ** 2 * c_s_ / 4 + b_v_ ** 2 * c_v_ / 2 - b_v_ ** 2 / 4 + b_v_ * c_s_ / 2 + b_v_ * c_v_ / 8 + 9 * b_v_ / 64 - 3 * c_s_ / 4 - 5 * c_v_ / 8 + 23 / 64,


def area_21(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 12 + b_s_ ** 2 * b_v_ / 2 - b_s_ ** 2 * c_s_ / 8 - b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 / 4 + b_s_ * b_v_ ** 2 - b_s_ * b_v_ * c_s_ / 2 - b_s_ * b_v_ * c_v_ - b_s_ * b_v_ + b_s_ * c_s_ / 2 + b_s_ * c_v_ + 2 * b_v_ ** 3 / 3 - b_v_ ** 2 * c_s_ / 2 - b_v_ ** 2 * c_v_ - b_v_ ** 2 + b_v_ * c_s_ + 2 * b_v_ * c_v_ - c_s_ / 2 - c_v_ + 1 / 3,


expressions_using_functions = [{'b_ss': [{'areas': area_1,
                                          'b_s': (0, 0.25 - b_v)},
                                         {'areas': area_2,
                                          'b_s': (0.25 - b_v, 0.5 - 2 * b_v)},
                                         {'areas': area_3,
                                          'b_s': (0.5 - 2 * b_v, 0.75 - b_v)},
                                         {'areas': area_4,
                                          'b_s': (0.75 - b_v, 1 - 2 * b_v)},
                                         {'areas': area_5,
                                          'b_s': (1 - 2 * b_v, 1 - b_v)},
                                         {'areas': area_6,
                                          'b_s': (1 - b_v, 1.25 - 2 * b_v)},
                                         {'areas': area_7,
                                          'b_s': (1.25 - 2 * b_v, 1.5 - 2 * b_v)},
                                         {'areas': area_8,
                                          'b_s': (1.5 - 2 * b_v, 1.75 - 2 * b_v)},
                                         {'areas': area_9,
                                          'b_s': (1.75 - 2 * b_v, 2 - 2 * b_v)}],
                                'b_v': (0, 0.25)},
                               {'b_ss': [{'areas': area_10,
                                          'b_s': (0, 0.75 - b_v)},
                                         {'areas': area_11,
                                          'b_s': (0.75 - b_v, 1 - b_v)},
                                         {'areas': area_12,
                                          'b_s': (1 - b_v, 1.5 - 2 * b_v)},
                                         {'areas': area_13,
                                          'b_s': (1.5 - 2 * b_v, 1.75 - 2 * b_v)},
                                         {'areas': area_14,
                                          'b_s': (1.75 - 2 * b_v, 2 - 2 * b_v)}],
                                'b_v': (0.25, 0.5)},
                               {'b_ss': [{'areas': area_15,
                                          'b_s': (0, 0.75 - b_v)},
                                         {'areas': area_16,
                                          'b_s': (0.75 - b_v, 1.5 - 2 * b_v)},
                                         {'areas': area_17,
                                          'b_s': (1.5 - 2 * b_v, 1 - b_v)},
                                         {'areas': area_18,
                                          'b_s': (1 - b_v, 1.75 - 2 * b_v)},
                                         {'areas': area_19,
                                          'b_s': (1.75 - 2 * b_v, 2 - 2 * b_v)}],
                                'b_v': (0.5, 0.75)},
                               {'b_ss': [{'areas': area_20,
                                          'b_s': (0, 1 - b_v)},
                                         {'areas': area_21,
                                          'b_s': (1 - b_v, 2 - 2 * b_v)}],
                                'b_v': (0.75, 1)}]
