def analytical_expected_profit_simple(b=0.4, cv=0.2, cs=0.5):
    if b < 0.25:
        return (-2 * b ** 2 + b ** 2 * cs + 4 * b * cv - 8 * cv - 4 * cs + 4) / 4
    elif b < 0.75:
        expression = 192 * b ** 3 - 416 * b ** 2 - 384 * b ** 2 * cv + 192 * b ** 2 * cs + 1072 * b * cv
        return (expression + 112 * b * cs - 66 * b - 680 * cv - 280 * cs + 283) / 256
    else:
        return (2 * b ** 2 * cs - 3 * b ** 2 + 2 * b * cs + 6 * b * cv - 4 * cs - 6 * cv + 3) / 8


def analytical_expected_profit_block(b, s=0.5, v=0.2):
    if b < 0.25:
        return (-2 * b ** 3 - 24 * s - 48 * v + 3 * s * b ** 2 + 6 * b ** 2 * v + 24) / 24
    elif 0.25 <= b < 0.5:
        return (-160 * b ** 3 + 48 * b ** 2 - 372 * s - 744 * v + 240 * s * b ** 2 - 96 * b * s + 480 * b ** 2 * v - 192 * b * v + 383) / 384
    elif 0.5 <= b < 0.75:
        return (-96 * b ** 3 + 48 * b ** 2 - 108 * s - 216 * v + 144 * b ** 2 * s - 96 * b * s + 288 * b ** 2 * v - 192 * v * b + 125) / 128
    elif 0.75 <= b < 1:
        return (-80 * b ** 3 - 216 * s - 432 * v + 120 * s * b ** 2 + 240 * b ** 2 * v + 201) / 192
    elif 1 <= b < 1.25:
        return (80 * b ** 3 - 240 * b ** 2 - 120 * b ** 2 * s - 456 * s + 480 * b * s - 912 * v - 240 * b ** 2 * v + 960 * b * v + 281) / 192
    elif 1.25 <= b < 1.5:
        return (96 * b ** 3 - 240 * b ** 2 + 480 * b * s - 144 * b ** 2 * s - 404 * s + 960 * v * b - 808 * v - 288 * b ** 2 * v + 229) / 128
    elif 1.5 <= b < 1.75:
        return 27 / 256 + (1728 * b * s - 480 * b ** 2 * s - 1560 * s + 3456 * v * b + 320 * b ** 3 + 861 - 3120 * v - 960 * v * b ** 2 - 864 * b ** 2) / 768
    elif 1.75 <= b < 2:
        return (2 * b ** 3 - 6 * v * b ** 2 - 3 * b ** 2 * s - 6 * b ** 2 + 24 * v * b + 12 * b * s + 8 - 24 * v - 12 * s) / 24
    else:
        return 0


def case1a(bs, bv, cv=0.2, cs=0.5):
    return -bs ** 3 / 12 - bs ** 2 * bv / 2 + bs ** 2 * cs / 8 + bs ** 2 * cv / 4 - bs * bv ** 2 / 2 + bs * bv * cs / 2 + bs * bv * cv / 2 + bv ** 2 * cs / 4 - bv ** 2 / 2 + bv * cv - 29 * cs / 32 - 29 * cv / 16 + 223 / 256


def case1i(bs, bv, cv=0.2, cs=0.5):
    return bs**3/12 + bs**2*bv/2 - bs**2*cs/8 - bs**2*cv/4 - bs**2/4 + bs*bv**2 - bs*bv*cs/2 - bs*bv*cv - bs*bv + bs*cs/2 + bs*cv + 2*bv**3/3 - bv**2*cs/2 - bv**2*cv - bv**2 + bv*cs + 2*bv*cv - cs/2 - cv + 1/3
