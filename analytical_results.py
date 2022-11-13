
def pc(b=0.4, c_v=0.2, c_s=0.5):
    if b < 0.25:
        return (-2 * b ** 2 + b ** 2 * c_s + 4 * b * c_v - 8 * c_v - 4 * c_s + 4) / 4
    elif b < 0.75:
        expression = 192 * b ** 3 - 416 * b ** 2 - 384 * b ** 2 * c_v + 192 * b ** 2 * c_s + 1072 * b * c_v
        return (expression + 112 * b * c_s - 66 * b - 680 * c_v - 280 * c_s + 283) / 256
    else:
        return (2 * b ** 2 * c_s - 3 * b ** 2 + 2 * b * c_s + 6 * b * c_v - 4 * c_s - 6 * c_v + 3) / 8


def hand_a(b=0.4, c_v=0.2, c_s=0.5):
    return (-b ** 2 + 2 * b ** 2 * c_s + 8 * b * c_v - 8 * c_s - 16 * c_v + 4) / 8


def geo(b=0.4, c_v=0.2, c_s=0.5):
    if b < 0.25:
        return (-2 * b ** 2 + b ** 2 * c_s + 4 * b * c_v - 8 * c_v - 4 * c_s + 4) / 4
    elif b < 0.75:
        return (-24 * b ** 2 - 40 * c_v + 36 * b ** 2 * c_s - 12 * b * c_s + 48 * b * c_v + 17 - 15 * c_s) / 16
    else:
        return (-2 * b ** 2 + b ** 2 * c_s + 4 * b * c_v + 2 * b * c_s - 4 * c_v - 3 * c_s + 2) / 4


def hand_block(b, s=0.5, v=0.2):
    if b < 0.25:
        return (-2 * b ** 3 - 24 * s - 48 * v + 3 * s * b ** 2 + 6 * b ** 2 * v + 24) / 24
    elif 0.25 <= b < 0.5:
        return (
                       -160 * b ** 3 + 48 * b ** 2 - 372 * s - 744 * v + 240 * s * b ** 2 - 96 * b * s + 480 * b ** 2 * v - 192 * b * v + 383) / 384
    elif 0.5 <= b < 0.75:
        return (
                       -96 * b ** 3 + 48 * b ** 2 - 108 * s - 216 * v + 144 * b ** 2 * s - 96 * b * s + 288 * b ** 2 * v - 192 * v * b + 125) / 128
    elif 0.75 <= b < 1:
        return (-80 * b ** 3 - 216 * s - 432 * v + 120 * s * b ** 2 + 240 * b ** 2 * v + 201) / 192
    elif 1 <= b < 1.25:
        return (
                       80 * b ** 3 - 240 * b ** 2 - 120 * b ** 2 * s - 456 * s + 480 * b * s - 912 * v - 240 * b ** 2 * v + 960 * b * v + 281) / 192
    elif 1.25 <= b < 1.5:
        return (
                       96 * b ** 3 - 240 * b ** 2 + 480 * b * s - 144 * b ** 2 * s - 404 * s + 960 * v * b - 808 * v - 288 * b ** 2 * v + 229) / 128
    elif 1.5 <= b < 1.75:
        return 27 / 256 + (
                1728 * b * s - 480 * b ** 2 * s - 1560 * s + 3456 * v * b + 320 * b ** 3 + 861 - 3120 * v - 960 * v * b ** 2 - 864 * b ** 2) / 768
    elif 1.75 <= b < 2:
        return (
                       2 * b ** 3 - 6 * v * b ** 2 - 3 * b ** 2 * s - 6 * b ** 2 + 24 * v * b + 12 * b * s + 8 - 24 * v - 12 * s) / 24
    else:
        return 0


def case1a(b_s, b_v, c_v=0.2, c_s=0.5):
    return -b_s ** 3 / 12 - b_s ** 2 * b_v / 2 + b_s ** 2 * c_s / 8 + b_s ** 2 * c_v / 4 - b_s * b_v ** 2 / 2 + b_s * b_v * c_s / 2 + b_s * b_v * c_v / 2 + b_v ** 2 * c_s / 4 - b_v ** 2 / 2 + b_v * c_v - 29 * c_s / 32 - 29 * c_v / 16 + 223 / 256


def case1i(b_s, b_v, c_v=0.2, c_s=0.5):
    return b_s**3/12 + b_s**2*b_v/2 - b_s**2*c_s/8 - b_s**2*c_v/4 - b_s**2/4 + b_s*b_v**2 - b_s*b_v*c_s/2 - b_s*b_v*c_v - b_s*b_v + b_s*c_s/2 + b_s*c_v + 2*b_v**3/3 - b_v**2*c_s/2 - b_v**2*c_v - b_v**2 + b_v*c_s + 2*b_v*c_v - c_s/2 - c_v + 1/3
