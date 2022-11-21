from analytical_results import *

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from random import random
from profit_functions import *
from distributions import *
from expected_profit import *
from optimal_bids import *
from constants import *
"""
everything is stepwise:

Simple:
    -profit_simple(p1, p2, b, cs, cv)
    -expected_profit_simple(b, cs, cv)
    -expected_profit_analytical_simple(b, cs, cv)
    optimal_bid_simple(cs, cv)

Block
    -profit_block(p1, p2, b, cs, cv)
    -expected_profit_block(b, cs, cv)
    -expected_profit_analytical_block(b, cs, cv)
    optimal_bid_block(cs, cv)

Multi-part
    -profit_multipart(p1, p2, bs, bv, cs, cv)
    -expected_profit_multipart(bs, bv, cs, cv)
    -expected_profit_analytical_multipart(bs, bv, cs, cv)               not validated
    optimal_bid_multipart(cs, cv)                                       not even calculated
"""


def random_stepwise():
    number = random()
    return number * 2 if number < 0.5 else number - 0.25


def show_multipart(distribution=uniform_distribution):
    b_surface, xs, ys, bv, bs, delta = [], [], [], 0, 0, 0.005
    mean_err = []

    for bv in tqdm(np.arange(0, 1, delta)):
        while bs < 2 - 2 * bv:
            bs_to_append = None
            if bv < 0.25 and 0.25 - bs < bv < 0.5-2*bs:
                simu_b = expected_profit((bs, bv), distribution=distribution, profit_func=profit_multipart)
                analytical_b = analytical_expected_profit_multi_part(bv, bs, 0.2, 0.5)
                b_surface.append(abs(simu_b - analytical_b))
                ys.append(bs)
                xs.append(bv)
            bs += delta
            """
            if b_v < 0.25 and 0 <= b_s <= 0.25 - b_v:
                # 1.75 − 2bv ≤ bs ≤ 2 − 2bv
                a = bs_to_append
                b = case1a(b_s, b_v)
                err = abs(a - b) / abs(a)
                print(a, b, err)
                mean_err.append(err)
                bs.append(b)
            else:
                bs.append(bs_to_append)"""
        bs = 0
        # print_progress_bar(b_v, delta, 1)

    # print("Atlagerr", sum(mean_err) / len(mean_err))
    print("max value: ", max(b_surface), "b_s: ", ys[b_surface.index(max(b_surface))], "b_v: ", xs[b_surface.index(max(b_surface))])
    ax = plt.axes(projection='3d')
    ax.scatter3D(xs, ys, b_surface, c=b_surface, cmap=plt.get_cmap('hsv'))
    ax.set_xlabel('b_v')
    ax.set_ylabel('b_s')
    ax.set_zlabel('E[π_multipart]')

    plt.show()


def show(profit_func=profit_simple, distribution=stepwise_distribution, c_v=0.2, c_s=0.5):
    bs, bss, xs, b, delta = [], [], [], 0, 0.01
    while b < 1:
        bs.append(expected_profit(b))
        bss.append(expected_profit(b, profit_func=profit_func, distribution=stepwise_distribution, cv=c_v, cs=c_s))
        xs.append(b)
        b += delta
        # print_progress_bar(b, delta, 1)
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
            bss.append(func(b) - expected_profit(b, profit_func=profit_block, distribution=stepwise_distribution,
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


def show_random_vs_homo(func=analytical_expected_profit_simple, max_b=1):
    bs, b, delta = [], 0, 0.06
    while b < max_b:
        bs.append(expected_profit_monte_carlo_block(b, random_stepwise) - expected_profit(b))
        b += delta
        print_progress_bar(b, delta, max_b)
    plt.plot(bs)
    plt.ylabel('random_vs_homo')
    plt.show(block=False)
    plt.show()


def b_optimal_for_step_simple_simple(cv=0.2, cs=0.5):
    bs = [0, 0.25, 0.75, 1, (-2 * cv) / (cs - 2), (-cs - 2 * cv) / (cs - 2),
           -1 * (-cs + 4 * cv) / (6 * cs - 4)]
    candidates = []
    for b in bs:
        candidates.append((expected_profit(b, stepwise_distribution, profit_simple, cv, cs), b))
    print(max(candidates))


def show_multipart_with_max(b, distribution=stepwise_distribution, profit_func=profit_simple):
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
# show_multipart(stepwise_distribution)

"""
    0.0004
    0.0008
"""


def validate_expected_profit_simple():
    analytical_plot, simulation_plot, xs, b, delta = [], [], [], 0, 0.01
    cv = 0.2
    cs = 0.5
    for b in np.arange(0, 1, delta):
        analytical_plot.append(analytical_expected_profit_simple(b, cv, cs))
        simulation_plot.append(
            expected_profit(b, cv, cs, profit_func=profit_simple, distribution=stepwise_distribution))
        xs.append(b)
        b += delta
    plt.plot(xs, simulation_plot, color='r')  # , color='g', label='step-wise distribution'
    plt.plot(xs, analytical_plot, color='b')
    # print("max value: ", max(bs), "b: ", xs[bs.index(max(bs))])
    print("max value: ", max(simulation_plot), "b: ", xs[simulation_plot.index(max(simulation_plot))])
    plt.legend()
    plt.ylabel('E[π_block(b)]')
    plt.xlabel('b')
    plt.show()


def validate_expected_profit_block():
    analytical_plot, simulation_plot, xs, b, delta = [], [], [], 0, 0.01
    monte_carlo_plot = []
    cv = 0.2
    cs = 0.5
    for b in np.arange(0, 2, delta):
        analytical_plot.append(analytical_expected_profit_block(b, cs=cs, cv=cv))
        simulation_plot.append(
            expected_profit(b, cv=cv, cs=cs, profit_func=profit_block, distribution=stepwise_distribution))
        monte_carlo_plot.append(expected_profit_monte_carlo_block(b, cv=cv, cs=cs))
        xs.append(b)
        b += delta
    plt.plot(xs, simulation_plot, color='r')  # , color='g', label='step-wise distribution'
    plt.plot(xs, analytical_plot, color='b')
    plt.plot(xs, monte_carlo_plot)
    # print("max value: ", max(bs), "b: ", xs[bs.index(max(bs))])
    print("max value: ", max(simulation_plot), "b: ", xs[simulation_plot.index(max(simulation_plot))])
    plt.legend()
    plt.ylabel('E[π_block(b)]')
    plt.xlabel('b')
    plt.show()


def validate_optimal_bid_simple():
    cv = 0.2
    for cs in np.arange(0, 1, 0.1):
        print(cs, cv)
        analytical_optimal_bid = analytical_optimal_bid_simple(cs=cs, cv=cv)
        simulation_bid = simulation_optimal_bid_simple(cs=cs, cv=cv)
        print("  ANALYTICAL:", analytical_optimal_bid)
        print("  SIMULATION:", simulation_bid)


def validate_optimal_bid_block():
    cs_cv_pairs = [
        (0.5, 0.2),
        (0.3, 0.1),
    ]
    # for cs_cv in cs_cv_pairs:
    cs = 0.2
    for cv in np.arange(0, 1, 0.1):
        print(cs, cv)
        analytical_optimal_bid = analytical_optimal_bid_block(cs=cs, cv=cv)
        simulation_bid = simulation_optimal_bid_block(cs=cs, cv=cv)
        print("  ANALYTICAL:", analytical_optimal_bid)
        print("  SIMULATION:", simulation_bid)



