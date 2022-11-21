import numpy as np
from profit_functions import *
from utilities import *
from sympy import *

"""
class Validator:
    def __init__(self, base_c_v=0.2, base_c_s=0.5, profit_func=profit_simple,
                 distribution=uniform_distribution):
        self.c_v = base_c_v
        self.c_s = base_c_s
        self.profit_func = profit_func
        self.distribution = distribution

    def expected_profit_legacy(self, b, delta):
        summa = 0
        point_number = 0
        i = delta / 2
        while i < 1:
            j = delta / 2
            while j < 1:
                summa += self.distribution(i, j, b, self.profit_func, self.c_v, self.c_s)
                j += delta
                point_number += 1
            i += delta
        return summa / point_number

    def expected_profit(self, b, delta):
        summa = 0
        point_number = 0
        for p_1 in np.arange(delta / 2, 1, delta):
            for p_2 in np.arange(delta / 2, 1, delta):
                summa += self.distribution(p_1, p_2, b, self.profit_func, self.c_v, self.c_s)
                point_number += 1
        return summa / point_number

    def expected_profit_np(self, b, delta):
        p_1 = np.arange(delta / 2, 1, delta).astype(np.float32)
        p_2 = np.arange(delta / 2, 1, delta).astype(np.float32)
        result = np.transpose([np.tile(p_1, len(p_2)), np.repeat(p_2, len(p_1))])
        return self.distribution(result, b, self.profit_func, self.c_v, self.c_s).mean()
"""


def eval_b_(b=0.4, profit_func=profit_simple):
    """
    only simple bidding, uniform dist
    """
    summa = 0
    point_number = 0
    delta = 0.002
    i = 0.002
    while i < 1:
        j = 0
        while j < 1:
            summa += profit_func(i, j, b)
            j += delta
            point_number += 1
        i += delta
    return summa / point_number


def hand_a(b=0.4, c_v=0.2, c_s=0.5):
    return (-b ** 2 + 2 * b ** 2 * c_s + 8 * b * c_v - 8 * c_s - 16 * c_v + 4) / 8


def geo(b=0.4, c_v=0.2, c_s=0.5):
    if b < 0.25:
        return (-2 * b ** 2 + b ** 2 * c_s + 4 * b * c_v - 8 * c_v - 4 * c_s + 4) / 4
    elif b < 0.75:
        return (-24 * b ** 2 - 40 * c_v + 36 * b ** 2 * c_s - 12 * b * c_s + 48 * b * c_v + 17 - 15 * c_s) / 16
    else:
        return (-2 * b ** 2 + b ** 2 * c_s + 4 * b * c_v + 2 * b * c_s - 4 * c_v - 3 * c_s + 2) / 4


costs = [48.34, 52.99, 16, 28, 36.10, 38.91, 23, 54, 16.90, 18.71, 28, 74]
means = [
    (costs[i * 2] + costs[i * 2 + 1]) / 2 for i in range(6)
]
print(means)
costs_ = [50.665000000000006, 16, 28, 37.504999999999995, 23, 54, 17.805, 28, 74]
print([
    round(a_mean / max(costs_), 2) for a_mean in costs_
])

normalized_power_plant_costs = [
    {"c_v": 0.68,
     "c_smin": 0.22,
     "c_smax": 0.38},
    {"c_v": 0.51,
     "c_s": 0.31,
     "c_smax": 0.7},
    {"c_v": 0.24,
     "c_smin": 0.38,
     "c_smax": 1.0}
]
