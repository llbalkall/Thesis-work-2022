import math
import numpy as np


def profit_simple_bidding(p_1, p_2, b=0.4, c_v=0.2, c_s=0.5):
    if p_1 >= b:
        if p_2 >= b:
            return p_1 + p_2 - c_s - 2 * c_v
        else:
            return p_1 - c_s - c_v
    else:
        if p_2 >= b:
            return p_2 - c_s - c_v
    return 0


def profit_multipart_bidding(p_1, p_2, b, c_v=0.4, c_s=0.6):
    b_s, b_v = b[0], b[1]
    if p_1 >= b_s + b_v and p_2 < b_v:
        return p_1 - c_s - c_v
    elif p_2 >= b_s + b_v and p_1 < b_v:
        return p_2 - c_s - c_v
    elif p_1 + p_2 >= b_s + 2 * b_v and p_1 >= b_v and p_2 >= b_v:
        return p_1 + p_2 - c_s - 2 * c_v
    else:
        return 0


def profit_block_bidding(p_1, p_2, b_b, c_v=0.2, c_s=0.5):
    return p_1 + p_2 - c_s - 2 * c_v if p_1 + p_2 >= b_b else 0


def step_wise_distribution(p_1, p_2, b=0.4, profit_func=profit_simple_bidding, c_v=0.2, c_s=0.5):
    m_1 = 0.5 if p_1 <= 0.25 or p_1 >= 0.75 else 1.5
    m_2 = 0.5 if p_2 <= 0.25 or p_2 >= 0.75 else 1.5
    return m_1 * m_2 * profit_func(p_1, p_2, b, c_v, c_s)


def uniform_distribution(p_1, p_2, b=0.4, profit_func=profit_simple_bidding, c_v=0.2, c_s=0.5):
    return profit_func(p_1, p_2, b, c_v, c_s)


def uniform_distribution_np(prices, b=0.4, profit_func=profit_simple_bidding, c_v=0.2, c_s=0.5):
    return profit_func(prices, b, c_v, c_s)


def profit_block_bidding_np(prices, b_b, c_v=0.2, c_s=0.5):
    """print(prices)
    print(b_b)
    print(prices[0, :] + prices[1, :] - c_s - 2 * c_v)
    print((prices[0, :] + prices[1, :]) >= b_b)"""
    wheres_stuff = np.where((prices[:, 0] + prices[:, 1]) >= b_b,  prices[:, 0] + prices[:, 1] - c_s - 2 * c_v, 0)
    # print(np.sum(wheres_stuff))
    return wheres_stuff


def step_wise_distribution_np(prices, b=0.4, profit_func=profit_simple_bidding, c_v=0.2, c_s=0.5):
    m_1 = np.where((prices[:, 0] <= 0.25) | (prices[:, 0] >= 0.75), 0.5, 1.5)
    m_2 = np.where((prices[:, 1] <= 0.25) | (prices[:, 1] >= 0.75), 0.5, 1.5)
    return m_1 * m_2 * profit_func(prices, b, c_v, c_s)


def print_progress_bar(current, delta, target=1):
    needed = math.ceil(current / target * 10) % 10
    prev_needed = math.ceil((current - delta) / target * 10) % 10
    if needed != prev_needed:
        if current / target < 0.98:
            print("=" + str(prev_needed * 10) + "=", end="")
        else:
            print("=100=")