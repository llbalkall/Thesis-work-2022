def profit_simple(p1, p2, b=0.4, cv=0.2, cs=0.5):
    if p1 >= b:
        if p2 >= b:
            return p1 + p2 - cs - 2 * cv
        else:
            return p1 - cs - cv
    else:
        if p2 >= b:
            return p2 - cs - cv
    return 0


def profit_multipart(p1, p2, b, cv=0.4, cs=0.6):
    bs, bv = b[0], b[1]
    if p1 >= bs + bv and p2 < bv:
        return p1 - cs - cv
    elif p2 >= bs + bv and p1 < bv:
        return p2 - cs - cv
    elif p1 + p2 >= bs + 2 * bv and p1 >= bv and p2 >= bv:
        return p1 + p2 - cs - 2 * cv
    else:
        return 0


def profit_block(p1, p2, bb, cv=0.2, cs=0.5):
    return p1 + p2 - cs - 2 * cv if p1 + p2 >= bb else 0
