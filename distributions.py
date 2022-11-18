def uniform_distribution(p1, p2):
    return 1


def stepwise_distribution(p1, p2):
    m1 = 0.5 if p1 <= 0.25 or p1 >= 0.75 else 1.5
    m2 = 0.5 if p2 <= 0.25 or p2 >= 0.75 else 1.5
    return m1 * m2
