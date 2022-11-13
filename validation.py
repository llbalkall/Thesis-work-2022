import math
from utilities import *
from analytical_results import *

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from random import random
from multipart_partitions import *
import gc
from time import time

class Validator:
    def __init__(self, base_c_v=0.2, base_c_s=0.5, profit_func=profit_simple_bidding,
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

    def expected_profit_function(self):
        """

        """
        print("expected_profit")

    def validate(self):
        print("validate")

    def show(self):
        pass


#deltaa = 0.001965
#v = Validator(distribution=step_wise_distribution_np, profit_func=profit_block_bidding_np)
#v2 = Validator(distribution=step_wise_distribution, profit_func=profit_block_bidding)
#for i in tqdm(range(2)):
#    print(v2.expected_profit_legacy(0.2, deltaa))
"""for i in tqdm(range(10)):
    print(v.expected_profit(0.2, 0.001))"""
"""for i in tqdm(range(2)):
    print("eredmény", v.expected_profit__(0.2, deltaa))

gc.collect()
"""

"""delta_opt = 0
for delta_d in tqdm(np.arange(0.00018, 1, 1e-6)):
    try:
        v.expected_profit__(0.2, delta_d)
        delta_opt = delta_d
        break
    except Exception:
        pass
print(delta_opt)"""


class MultipartBiddingValidator(Validator):
    def expected_profit(self):
        bs, xs, ys, b_v, b_s, delta = [], [], [], 0, 0, 0.01

        mean_err = []

        for b_v in tqdm(np.arange(0, 1, delta)):
            while b_s < 2 - 2 * b_v:
                bs_to_append = evaluate_b((b_s, b_v), distribution=distribution, profit_func=profit_multipart_bidding)
                # bs.append(bs_to_append)
                ys.append(b_s)
                xs.append(b_v)
                b_s += delta
                if b_v < 0.25 and 1.75 - 2 * b_v <= b_s <= 2 - 2 * b_v:
                    # 1.75 − 2bv ≤ bs ≤ 2 − 2bv
                    a = bs_to_append
                    b = case1i(b_s, b_v)
                    err = abs(a - b) / abs(a)
                    print(a, b, err)
                    mean_err.append(err)
                    bs.append(b)
                else:
                    bs.append(bs_to_append)
            b_s = 0
            print_progress_bar(b_v, delta, 1)


def eval_b_(b=0.4, profit_func=profit_simple_bidding):
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


def evaluate_b(b, distribution=uniform_distribution, profit_func=profit_simple_bidding, c_v=0.2, c_s=0.5, delta=0.01):
    """
        Can use simple/block/multipart with uniform/stepwise
    """
    summa = 0
    point_number = 0
    i = delta / 2
    while i < 1:
        j = delta / 2
        while j < 1:
            summa += distribution(i, j, b, profit_func, c_v, c_s)
            j += delta
            point_number += 1
        i += delta
    return summa / point_number


def eval_b(b=0.4, randi=random, db=10000):
    """
        only using block bidding, random uniform/stepwise
    """
    summa = 0
    for i in range(db):
        summa += profit_block_bidding(randi(), randi(), b)
    return summa / i


def random_stepwise():
    """
    Random number between 0 and 1 and with a stepwise distribution
    """
    a = random()
    return (a * 2) if a <= 0.5 else (a - 0.25)


def show_multipart(distribution=uniform_distribution):
    bs, xs, ys, b_v, b_s, delta = [], [], [], 0, 0, 0.01

    mean_err = []

    for b_v in tqdm(np.arange(0, 1, delta)):
        while b_s < 2 - 2 * b_v:
            bs_to_append = evaluate_b((b_s, b_v), distribution=distribution, profit_func=profit_multipart_bidding)
            # bs.append(bs_to_append)
            ys.append(b_s)
            xs.append(b_v)
            b_s += delta
            if b_v < 0.25 and 0 <= b_s <= 0.25 -  b_v:
                # 1.75 − 2bv ≤ bs ≤ 2 − 2bv
                a = bs_to_append
                b = case1a(b_s, b_v)
                err = abs(a - b) / abs(a)
                print(a, b, err)
                mean_err.append(err)
                bs.append(b)
            else:
                bs.append(bs_to_append)
        b_s = 0
        # print_progress_bar(b_v, delta, 1)

    print("Atlagerr", sum(mean_err) / len(mean_err))
    print("max value: ", max(bs), "b_s: ", ys[bs.index(max(bs))], "b_v: ", xs[bs.index(max(bs))])
    ax = plt.axes(projection='3d')
    ax.scatter3D(xs, ys, bs, c=bs, cmap='Greens')
    ax.set_xlabel('b_v')
    ax.set_ylabel('b_s')
    ax.set_zlabel('E[π_multipart]')

    plt.show()


def show(profit_func=profit_simple_bidding, distribution=step_wise_distribution, c_v=0.2, c_s=0.5):
    bs, bss, xs, b, delta = [], [], [], 0, 0.01
    while b < 1:
        bs.append(evaluate_b(b))
        bss.append(evaluate_b(b, profit_func=profit_func, distribution=step_wise_distribution, c_v=c_v, c_s=c_s))
        xs.append(b)
        b += delta
        print_progress_bar(b, delta, 1)
    # plt.plot(xs, bs, color='r', label='uniform distribution')
    plt.plot(xs, bss, color='r')  # , color='g', label='step-wise distribution'
    # print("max value: ", max(bs), "b: ", xs[bs.index(max(bs))])
    print("max value: ", max(bss), "b: ", xs[bss.index(max(bss))])
    plt.legend()
    plt.ylabel('E[π_block(b)]')
    plt.xlabel('b')
    plt.show()


def show_error(delta, func, name="error", start_b=0, max_b=1):
    print(name + ": ", end="")
    cs, bs, xs, b = [], [], [], start_b
    for delttta in [0.01, 0.008, 0.005, 0.001, 0.0005]:  # [9000, 10000, 50000, 100000, 1000000]:
        bss = []
        b = start_b
        while b < max_b:
            bss.append(func(b) - evaluate_b(b, profit_func=profit_block_bidding, distribution=step_wise_distribution,
                                            delta=delttta))
            # bss.append(func(b) - eval_b(b, rand_2, db = delttta))
            # cs.append(func(b))
            # bs.append(eval_b_2(b, profit_func=profit_block_bidding, distribution=step_wise_distribution))
            print_progress_bar(b, delta, max_b)
            b += delta
        bs.append(bss)
    b = start_b
    while b < max_b:
        xs.append(b)
        b += delta
    plt.plot(xs, bs[0], color="darkred", label="0.01")
    # plt.plot(xs, bs[1], color = "g")
    plt.plot(xs, bs[2], color="red", label="0.005")
    plt.plot(xs, bs[3], color="orange", label=" 0.001")
    plt.plot(xs, bs[4], color="gold", label="0.0005")
    plt.legend()
    # plt.plot(xs, cs, color = "r")
    plt.ylabel("error")
    plt.xlabel('b')
    plt.show(block=False)
    plt.show()


def show_random_vs_homo(func=hand_a, max_b=1):
    bs, b, delta = [], 0, 0.06
    while b < max_b:
        bs.append(eval_b(b, random_stepwise) - evaluate_b(b))
        b += delta
        print_progress_bar(b, delta, max_b)
    plt.plot(bs)
    plt.ylabel('random_vs_homo')
    plt.show(block=False)
    plt.show()


def b_optimal_for_step_simple_simple(c_v=0.2, c_s=0.5):
    b_s = [0, 0.25, 0.75, 1, (-2 * c_v) / (c_s - 2), (-c_s - 2 * c_v) / (c_s - 2),
           -1 * (-c_s + 4 * c_v) / (6 * c_s - 4)]
    candidates = []
    for b in b_s:
        candidates.append((evaluate_b(b, step_wise_distribution, profit_simple_bidding, c_v, c_s), b))
    print(max(candidates))


def show_multipart_with_max(b, distribution=step_wise_distribution, profit_func=profit_simple_bidding):
    bs, xs, ys = [], [], []
    summa = 0
    point_number = 0
    delta = 0.005
    i = delta / 2
    while i < 1:
        j = delta / 2
        while j < 1:
            summa += distribution(i, j, b, profit_func)
            bs.append(distribution(i, j, b, profit_func))
            ys.append(i)
            xs.append(j)
            j += delta
            point_number += 1
        i += delta
    ax = plt.axes(projection='3d')
    ax.scatter3D(xs, ys, bs, c=bs, cmap='hot')
    ax.set_xlabel('p_1')
    ax.set_ylabel('p_2')
    ax.set_zlabel('π_multipart(' + str(b[0]) + " " + str(b[1]) + ")")
    print(b, " -- max value: ", max(bs), "b: ", xs[bs.index(max(bs))])
    plt.show()
    return summa / point_number


# show_error(0.05, hand_block, "step_wise_distribution", start_b=0, max_b=2)


# show(profit_block_bidding, step_wise_distribution)
# show_random_vs_homo()
#
# b_optimal_for_step_simple()
# show()

"""b_ss = [(0.2, 0.2), (0.2, 0.5), (0.2, 0.8), (0.2, 0.2), (0.5, 0.2), (0.8, 0.2)]
for ss in b_ss:
    eval_b_2_show(ss, distribution=step_wise_distribution, profit_func=profit_multipart_bidding)


cscv = [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5), (0.2, 0.2), (0.2, 0.5), (0.2, 0.2), (0.2, 0.5)]


for vs in cscv:
    b_optimal_for_step_simple(vs[0], vs[1])
    show(c_v=vs[0], c_s=vs[1])"""

# show_multipart(uniform_distribution)
show_multipart(step_wise_distribution)

"""
    0.0004
    0.0008
"""
