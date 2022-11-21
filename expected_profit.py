from distributions import random_stepwise


def expected_profit(b, cv, cs, distribution, profit_func, delta=0.01):
    """
        Can use simple/block/multipart with uniform/stepwise
    """
    summa = 0
    point_number = 0
    p1 = delta / 2
    while p1 < 1:
        p2 = delta / 2
        while p2 < 1:
            summa += distribution(p1, p2) * profit_func(p1, p2, b, cv=cv, cs=cs)
            p2 += delta
            point_number += 1
        p1 += delta
    return summa / point_number


def expected_profit_monte_carlo_block(b, cv, cs, profit_func, db=10000):
    """
        only using block bidding, random uniform/stepwise
    """
    summa = 0
    count = 0
    for i_ in range(db):
        summa += profit_func(random_stepwise(), random_stepwise(), b, cv, cs)
        count = i_
    return summa / count
