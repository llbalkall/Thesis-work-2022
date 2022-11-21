from analytical_results import *
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from profit_functions import *
from distributions import *
from expected_profit import *
from constants import *


def analytical_optimal_bid_simple(cs, cv):
    possible_b = [0, 0.25, 0.75, 1, (-2 * cv) / (cs - 2), (-cs + 4 * cv) / (6 * cs - 4), (-cs - 2 * cv) / (cs - 2)]
    expected_profits = []
    for b in possible_b:
        ep = expected_profit(b, cv, cs, stepwise_distribution, profit_simple)
        # print(f"{b}: {ep}")
        expected_profits.append(ep)
    maximum_expected_profit = max(expected_profits)
    optimal_bid = possible_b[expected_profits.index(maximum_expected_profit)]
    return optimal_bid


def simulation_optimal_bid_simple(cs, cv, delta=0.005):
    list_of_expected_profits = []
    for b in np.arange(0, 1, delta):
        list_of_expected_profits.append(expected_profit(b, cv, cs, stepwise_distribution, profit_simple))
    maximum_expected_profit = max(list_of_expected_profits)
    optimal_bid = list_of_expected_profits.index(maximum_expected_profit) * delta
    return optimal_bid


def simulation_optimal_bid_block(cs, cv, delta=0.01):
    list_of_expected_profits = []
    for b in np.arange(0, 2, delta):
        ep = expected_profit(b, cv, cs, stepwise_distribution, profit_block)
        list_of_expected_profits.append((ep, b))
    maximum_expected_profit = max(list_of_expected_profits)
    return maximum_expected_profit[1]


def analytical_optimal_bid_block(cs, cv):
    possible_b = [0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, cs + 2*cv]
    expected_profits = [(expected_profit(b, cv, cs, stepwise_distribution, profit_block), b) for b in possible_b]
    maximum_expected_profit = max(expected_profits)
    optimal_bid = possible_b[expected_profits.index(maximum_expected_profit)]
    return optimal_bid


