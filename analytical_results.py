from sympy import *

b_v, b_s = symbols('b_v b_s')


def analytical_expected_profit_simple(b=0.4, cv=0.2, cs=0.5):
    if b < 0.25:
        return (-2 * b ** 2 + b ** 2 * cs + 4 * b * cv - 8 * cv - 4 * cs + 4) / 4
    elif b < 0.75:
        expression = 192 * b ** 3 - 416 * b ** 2 - 384 * b ** 2 * cv + 192 * b ** 2 * cs + 1072 * b * cv
        return (expression + 112 * b * cs - 66 * b - 680 * cv - 280 * cs + 283) / 256
    else:
        return (2 * b ** 2 * cs - 3 * b ** 2 + 2 * b * cs + 6 * b * cv - 4 * cs - 6 * cv + 3) / 8


def analytical_expected_profit_block(b, cs=0.5, cv=0.2):
    if b < 0.25:
        return (-2 * b ** 3 - 24 * cs - 48 * cv + 3 * cs * b ** 2 + 6 * b ** 2 * cv + 24) / 24
    elif 0.25 <= b < 0.5:
        return (-160 * b ** 3 + 48 * b ** 2 - 372 * cs - 744 * cv + 240 * cs * b ** 2 - 96 * b * cs + 480 * b ** 2 * cv - 192 * b * cv + 383) / 384
    elif 0.5 <= b < 0.75:
        return (-96 * b ** 3 + 48 * b ** 2 - 108 * cs - 216 * cv + 144 * b ** 2 * cs - 96 * b * cs + 288 * b ** 2 * cv - 192 * cv * b + 125) / 128
    elif 0.75 <= b < 1:
        return (-80 * b ** 3 - 216 * cs - 432 * cv + 120 * cs * b ** 2 + 240 * b ** 2 * cv + 201) / 192
    elif 1 <= b < 1.25:
        return (80 * b ** 3 - 240 * b ** 2 - 120 * b ** 2 * cs - 456 * cs + 480 * b * cs - 912 * cv - 240 * b ** 2 * cv + 960 * b * cv + 281) / 192
    elif 1.25 <= b < 1.5:
        return (96 * b ** 3 - 240 * b ** 2 + 480 * b * cs - 144 * b ** 2 * cs - 404 * cs + 960 * cv * b - 808 * cv - 288 * b ** 2 * cv + 229) / 128
    elif 1.5 <= b < 1.75:
        return 27 / 256 + (1728 * b * cs - 480 * b ** 2 * cs - 1560 * cs + 3456 * cv * b + 320 * b ** 3 + 861 - 3120 * cv - 960 * cv * b ** 2 - 864 * b ** 2) / 768
    elif 1.75 <= b < 2:
        return (2 * b ** 3 - 6 * cv * b ** 2 - 3 * b ** 2 * cs - 6 * b ** 2 + 24 * cv * b + 12 * b * cs + 8 - 24 * cv - 12 * cs) / 24
    else:
        return 0


def area_1(b_v_, b_s_, c_v_, c_s_):
    return -b_s_ ** 3 / 12 - b_s_ ** 2 * b_v_ / 2 + b_s_ ** 2 * c_s_ / 8 + b_s_ ** 2 * c_v_ / 4 - b_s_ * b_v_ ** 2 / 2 + b_s_ * b_v_ * c_s_ / 2 + b_s_ * b_v_ * c_v_ / 2 + b_v_ ** 2 * c_s_ / 4 - b_v_ ** 2 / 2 + b_v_ * c_v_ - c_s_ - 2 * c_v_ + 1,


def area_2(b_v_, b_s_, c_v_, c_s_):
    return -b_s_ ** 3 / 6 - 3 * b_s_ ** 2 * b_v_ / 2 + 5 * b_s_ ** 2 * c_s_ / 8 + b_s_ ** 2 * c_v_ / 2 + b_s_ ** 2 / 16 - 2 * b_s_ * b_v_ ** 2 + 7 * b_s_ * b_v_ * c_s_ / 2 + 5 * b_s_ * b_v_ * c_v_ / 2 - b_s_ * c_s_ / 2 - b_s_ * c_v_ / 4 + b_s_ / 32 - 7 * b_v_ ** 3 / 12 + 11 * b_v_ ** 2 * c_s_ / 4 + 7 * b_v_ ** 2 * c_v_ / 4 - 3 * b_v_ ** 2 / 8 - 3 * b_v_ * c_s_ / 2 - 5 * b_v_ * c_v_ / 8 + 23 * b_v_ / 64 - 25 * c_s_ / 32 - 109 * c_v_ / 64 + 175 / 192,


def area_3(b_v_, b_s_, c_v_, c_s_):
    return -3 * b_s_ ** 2 * b_v_ / 4 - 3 * b_s_ * b_v_ ** 2 / 4 + 3 * b_s_ * b_v_ * c_s_ / 2 + 3 * b_s_ * b_v_ * c_v_ / 2 - 3 * b_s_ * b_v_ / 8 + 3 * b_s_ / 64 + b_v_ ** 3 / 2 + 3 * b_v_ ** 2 * c_s_ / 4 - 5 * b_v_ ** 2 / 8 - 3 * b_v_ * c_s_ / 4 - b_v_ * c_v_ / 4 + 15 * b_v_ / 32 - 27 * c_s_ / 32 - 27 * c_v_ / 16 + 113 / 128,


def area_4(b_v_, b_s_, c_v_, c_s_):
    return -5 * b_s_ ** 3 / 12 - 5 * b_s_ ** 2 * b_v_ / 2 + 5 * b_s_ ** 2 * c_s_ / 8 + 5 * b_s_ ** 2 * c_v_ / 4 - 9 * b_s_ * b_v_ ** 2 / 2 + 5 * b_s_ * b_v_ * c_s_ / 2 + 9 * b_s_ * b_v_ * c_v_ / 2 - 8 * b_v_ ** 3 / 3 + 9 * b_v_ ** 2 * c_s_ / 4 + 4 * b_v_ ** 2 * c_v_ - b_v_ ** 2 / 4 + b_v_ * c_v_ / 2 - 9 * c_s_ / 8 - 9 * c_v_ / 4 + 67 / 64,


def area_5(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 4 + 2 * b_s_ ** 2 * b_v_ - 3 * b_s_ ** 2 * c_s_ / 8 - 3 * b_s_ ** 2 * c_v_ / 4 - 9 * b_s_ ** 2 / 8 + 11 * b_s_ * b_v_ ** 2 / 2 - 5 * b_s_ * b_v_ * c_s_ / 2 - 11 * b_s_ * b_v_ * c_v_ / 2 - 9 * b_s_ * b_v_ / 2 + 9 * b_s_ * c_s_ / 4 + 9 * b_s_ * c_v_ / 2 + 9 * b_v_ ** 3 / 2 - 13 * b_v_ ** 2 * c_s_ / 4 - 7 * b_v_ ** 2 * c_v_ - 21 * b_v_ ** 2 / 4 + 11 * b_v_ * c_s_ / 2 + 23 * b_v_ * c_v_ / 2 - b_v_ / 2 - 77 * c_s_ / 32 - 77 * c_v_ / 16 + 197 / 128,


def area_6(b_v_, b_s_, c_v_, c_s_):
    return 5 * b_s_ ** 3 / 12 + 5 * b_s_ ** 2 * b_v_ / 2 - 5 * b_s_ ** 2 * c_s_ / 8 - 5 * b_s_ ** 2 * c_v_ / 4 - 5 * b_s_ ** 2 / 4 + 5 * b_s_ * b_v_ ** 2 - 5 * b_s_ * b_v_ * c_s_ / 2 - 5 * b_s_ * b_v_ * c_v_ - 5 * b_s_ * b_v_ + 5 * b_s_ * c_s_ / 2 + 5 * b_s_ * c_v_ + 10 * b_v_ ** 3 / 3 - 5 * b_v_ ** 2 * c_s_ / 2 - 5 * b_v_ ** 2 * c_v_ - 5 * b_v_ ** 2 + 5 * b_v_ * c_s_ + 10 * b_v_ * c_v_ - 19 * c_s_ / 8 - 19 * c_v_ / 4 + 281 / 192,


def area_7(b_v_, b_s_, c_v_, c_s_):
    return 3 * b_s_ ** 3 / 2 + 9 * b_s_ ** 2 * b_v_ - 9 * b_s_ ** 2 * c_s_ / 4 - 9 * b_s_ ** 2 * c_v_ / 2 - 111 * b_s_ ** 2 / 32 + 18 * b_s_ * b_v_ ** 2 - 9 * b_s_ * b_v_ * c_s_ - 18 * b_s_ * b_v_ * c_v_ - 111 * b_s_ * b_v_ / 8 + 111 * b_s_ * c_s_ / 16 + 111 * b_s_ * c_v_ / 8 + 12 * b_v_ ** 3 - 9 * b_v_ ** 2 * c_s_ - 18 * b_v_ ** 2 * c_v_ - 111 * b_v_ ** 2 / 8 + 111 * b_v_ * c_s_ / 8 + 111 * b_v_ * c_v_ / 4 - 689 * c_s_ / 128 - 689 * c_v_ / 64 + 1437 / 512,


def area_8(b_v_, b_s_, c_v_, c_s_):
    return 5 * b_s_ ** 3 / 12 + 5 * b_s_ ** 2 * b_v_ / 2 - 5 * b_s_ ** 2 * c_s_ / 8 - 5 * b_s_ ** 2 * c_v_ / 4 - 9 * b_s_ ** 2 / 8 + 5 * b_s_ * b_v_ ** 2 - 5 * b_s_ * b_v_ * c_s_ / 2 - 5 * b_s_ * b_v_ * c_v_ - 9 * b_s_ * b_v_ / 2 + 9 * b_s_ * c_s_ / 4 + 9 * b_s_ * c_v_ / 2 + 10 * b_v_ ** 3 / 3 - 5 * b_v_ ** 2 * c_s_ / 2 - 5 * b_v_ ** 2 * c_v_ - 9 * b_v_ ** 2 / 2 + 9 * b_v_ * c_s_ / 2 + 9 * b_v_ * c_v_ - 65 * c_s_ / 32 - 65 * c_v_ / 16 + 157 / 128,


def area_9(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 12 + b_s_ ** 2 * b_v_ / 2 - b_s_ ** 2 * c_s_ / 8 - b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 / 4 + b_s_ * b_v_ ** 2 - b_s_ * b_v_ * c_s_ / 2 - b_s_ * b_v_ * c_v_ - b_s_ * b_v_ + b_s_ * c_s_ / 2 + b_s_ * c_v_ + 2 * b_v_ ** 3 / 3 - b_v_ ** 2 * c_s_ / 2 - b_v_ ** 2 * c_v_ - b_v_ ** 2 + b_v_ * c_s_ + 2 * b_v_ * c_v_ - c_s_ / 2 - c_v_ + 1 / 3,


def area_10(b_v_, b_s_, c_v_, c_s_):
    return -3 * b_s_ ** 3 / 4 - 3 * b_s_ ** 2 * b_v_ + 9 * b_s_ ** 2 * c_s_ / 8 + 9 * b_s_ ** 2 * c_v_ / 4 - 3 * b_s_ * b_v_ ** 2 / 2 + 3 * b_s_ * b_v_ * c_s_ / 2 + 3 * b_s_ * b_v_ * c_v_ / 2 + 3 * b_v_ ** 3 / 2 - 3 * b_v_ ** 2 * c_s_ / 4 - 3 * b_v_ ** 2 * c_v_ - 15 * b_v_ ** 2 / 8 + 9 * b_v_ * c_s_ / 4 + 6 * b_v_ * c_v_ - 27 * b_v_ / 32 - 3 * c_s_ / 2 - 49 * c_v_ / 16 + 163 / 128,


def area_11(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 4 + 3 * b_s_ ** 2 * b_v_ / 2 - 3 * b_s_ ** 2 * c_s_ / 8 - 3 * b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 + 9 * b_s_ * b_v_ ** 2 / 2 - 3 * b_s_ * b_v_ * c_s_ / 2 - 9 * b_s_ * b_v_ * c_v_ / 2 - 17 * b_s_ * b_v_ / 4 + 2 * b_s_ * c_s_ + 17 * b_s_ * c_v_ / 4 + 4 * b_v_ ** 3 - 9 * b_v_ ** 2 * c_s_ / 4 - 6 * b_v_ ** 2 * c_v_ - 41 * b_v_ ** 2 / 8 + 17 * b_v_ * c_s_ / 4 + 41 * b_v_ * c_v_ / 4 - 69 * c_s_ / 32 - 73 * c_v_ / 16 + 181 / 128,


def area_12(b_v_, b_s_, c_v_, c_s_):
    return 3 * b_s_ ** 3 / 4 + 9 * b_s_ ** 2 * b_v_ / 2 - 9 * b_s_ ** 2 * c_s_ / 8 - 9 * b_s_ ** 2 * c_v_ / 4 - 15 * b_s_ ** 2 / 8 + 9 * b_s_ * b_v_ ** 2 - 9 * b_s_ * b_v_ * c_s_ / 2 - 9 * b_s_ * b_v_ * c_v_ - 15 * b_s_ * b_v_ / 2 + 15 * b_s_ * c_s_ / 4 + 15 * b_s_ * c_v_ / 2 + 6 * b_v_ ** 3 - 9 * b_v_ ** 2 * c_s_ / 2 - 9 * b_v_ ** 2 * c_v_ - 15 * b_v_ ** 2 / 2 + 15 * b_v_ * c_s_ / 2 + 15 * b_v_ * c_v_ - 101 * c_s_ / 32 - 101 * c_v_ / 16 + 229 / 128,


def area_13(b_v_, b_s_, c_v_, c_s_):
    return 5 * b_s_ ** 3 / 12 + 5 * b_s_ ** 2 * b_v_ / 2 - 5 * b_s_ ** 2 * c_s_ / 8 - 5 * b_s_ ** 2 * c_v_ / 4 - 9 * b_s_ ** 2 / 8 + 5 * b_s_ * b_v_ ** 2 - 5 * b_s_ * b_v_ * c_s_ / 2 - 5 * b_s_ * b_v_ * c_v_ - 9 * b_s_ * b_v_ / 2 + 9 * b_s_ * c_s_ / 4 + 9 * b_s_ * c_v_ / 2 + 10 * b_v_ ** 3 / 3 - 5 * b_v_ ** 2 * c_s_ / 2 - 5 * b_v_ ** 2 * c_v_ - 9 * b_v_ ** 2 / 2 + 9 * b_v_ * c_s_ / 2 + 9 * b_v_ * c_v_ - 65 * c_s_ / 32 - 65 * c_v_ / 16 + 157 / 128,


def area_14(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 12 + b_s_ ** 2 * b_v_ / 2 - b_s_ ** 2 * c_s_ / 8 - b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 / 4 + b_s_ * b_v_ ** 2 - b_s_ * b_v_ * c_s_ / 2 - b_s_ * b_v_ * c_v_ - b_s_ * b_v_ + b_s_ * c_s_ / 2 + b_s_ * c_v_ + 2 * b_v_ ** 3 / 3 - b_v_ ** 2 * c_s_ / 2 - b_v_ ** 2 * c_v_ - b_v_ ** 2 + b_v_ * c_s_ + 2 * b_v_ * c_v_ - c_s_ / 2 - c_v_ + 1 / 3,


def area_15(b_v_, b_s_, c_v_, c_s_):
    return -3 * b_s_ ** 3 / 4 - 3 * b_s_ ** 2 * b_v_ + 9 * b_s_ ** 2 * c_s_ / 8 + 9 * b_s_ ** 2 * c_v_ / 4 - 3 * b_s_ * b_v_ ** 2 / 2 + 3 * b_s_ * b_v_ * c_s_ / 2 + 3 * b_s_ * b_v_ * c_v_ / 2 + 3 * b_v_ ** 3 / 2 - 3 * b_v_ ** 2 * c_s_ / 4 - 3 * b_v_ ** 2 * c_v_ - 15 * b_v_ ** 2 / 8 + 9 * b_v_ * c_s_ / 4 + 6 * b_v_ * c_v_ - 27 * b_v_ / 32 - 3 * c_s_ / 2 - 49 * c_v_ / 16 + 163 / 128,


def area_16(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 4 + 3 * b_s_ ** 2 * b_v_ / 2 - 3 * b_s_ ** 2 * c_s_ / 8 - 3 * b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 + 9 * b_s_ * b_v_ ** 2 / 2 - 3 * b_s_ * b_v_ * c_s_ / 2 - 9 * b_s_ * b_v_ * c_v_ / 2 - 17 * b_s_ * b_v_ / 4 + 2 * b_s_ * c_s_ + 17 * b_s_ * c_v_ / 4 + 4 * b_v_ ** 3 - 9 * b_v_ ** 2 * c_s_ / 4 - 6 * b_v_ ** 2 * c_v_ - 41 * b_v_ ** 2 / 8 + 17 * b_v_ * c_s_ / 4 + 41 * b_v_ * c_v_ / 4 - 69 * c_s_ / 32 - 73 * c_v_ / 16 + 181 / 128,


def area_17(b_v_, b_s_, c_v_, c_s_):
    return -b_s_ ** 3 / 12 - b_s_ ** 2 * b_v_ / 2 + b_s_ ** 2 * c_s_ / 8 + b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 / 4 + b_s_ * b_v_ ** 2 / 2 + b_s_ * b_v_ * c_s_ / 2 - b_s_ * b_v_ * c_v_ / 2 - 5 * b_s_ * b_v_ / 4 + b_s_ * c_s_ / 2 + 5 * b_s_ * c_v_ / 4 + 4 * b_v_ ** 3 / 3 - b_v_ ** 2 * c_s_ / 4 - 2 * b_v_ ** 2 * c_v_ - 17 * b_v_ ** 2 / 8 + 5 * b_v_ * c_s_ / 4 + 17 * b_v_ * c_v_ / 4 - 33 * c_s_ / 32 - 37 * c_v_ / 16 + 109 / 128,


def area_18(b_v_, b_s_, c_v_, c_s_):
    return 5 * b_s_ ** 3 / 12 + 5 * b_s_ ** 2 * b_v_ / 2 - 5 * b_s_ ** 2 * c_s_ / 8 - 5 * b_s_ ** 2 * c_v_ / 4 - 9 * b_s_ ** 2 / 8 + 5 * b_s_ * b_v_ ** 2 - 5 * b_s_ * b_v_ * c_s_ / 2 - 5 * b_s_ * b_v_ * c_v_ - 9 * b_s_ * b_v_ / 2 + 9 * b_s_ * c_s_ / 4 + 9 * b_s_ * c_v_ / 2 + 10 * b_v_ ** 3 / 3 - 5 * b_v_ ** 2 * c_s_ / 2 - 5 * b_v_ ** 2 * c_v_ - 9 * b_v_ ** 2 / 2 + 9 * b_v_ * c_s_ / 2 + 9 * b_v_ * c_v_ - 65 * c_s_ / 32 - 65 * c_v_ / 16 + 157 / 128,


def area_19(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 12 + b_s_ ** 2 * b_v_ / 2 - b_s_ ** 2 * c_s_ / 8 - b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 / 4 + b_s_ * b_v_ ** 2 - b_s_ * b_v_ * c_s_ / 2 - b_s_ * b_v_ * c_v_ - b_s_ * b_v_ + b_s_ * c_s_ / 2 + b_s_ * c_v_ + 2 * b_v_ ** 3 / 3 - b_v_ ** 2 * c_s_ / 2 - b_v_ ** 2 * c_v_ - b_v_ ** 2 + b_v_ * c_s_ + 2 * b_v_ * c_v_ - c_s_ / 2 - c_v_ + 1 / 3,


def area_20(b_v_, b_s_, c_v_, c_s_):
    return -b_s_ ** 3 / 12 - b_s_ ** 2 * b_v_ / 2 + b_s_ ** 2 * c_s_ / 8 + b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 / 4 - 3 * b_s_ * b_v_ ** 2 / 4 + b_s_ * b_v_ * c_s_ / 2 + b_s_ * b_v_ * c_v_ - b_s_ * b_v_ / 2 + b_s_ * c_s_ / 2 + b_s_ * c_v_ / 8 + 9 * b_s_ / 64 - b_v_ ** 3 / 4 + b_v_ ** 2 * c_s_ / 4 + b_v_ ** 2 * c_v_ / 2 - b_v_ ** 2 / 4 + b_v_ * c_s_ / 2 + b_v_ * c_v_ / 8 + 9 * b_v_ / 64 - 3 * c_s_ / 4 - 5 * c_v_ / 8 + 23 / 64,


def area_21(b_v_, b_s_, c_v_, c_s_):
    return b_s_ ** 3 / 12 + b_s_ ** 2 * b_v_ / 2 - b_s_ ** 2 * c_s_ / 8 - b_s_ ** 2 * c_v_ / 4 - b_s_ ** 2 / 4 + b_s_ * b_v_ ** 2 - b_s_ * b_v_ * c_s_ / 2 - b_s_ * b_v_ * c_v_ - b_s_ * b_v_ + b_s_ * c_s_ / 2 + b_s_ * c_v_ + 2 * b_v_ ** 3 / 3 - b_v_ ** 2 * c_s_ / 2 - b_v_ ** 2 * c_v_ - b_v_ ** 2 + b_v_ * c_s_ + 2 * b_v_ * c_v_ - c_s_ / 2 - c_v_ + 1 / 3,


expressions_using_functions = [{'b_ss': [{'areas': area_1,
                                          'b_s': (0, 0.25 - b_v)},
                                         {'areas': area_2,
                                          'b_s': (0.25 - b_v, 0.5 - 2 * b_v)},
                                         {'areas': area_3,
                                          'b_s': (0.5 - 2 * b_v, 0.75 - b_v)},
                                         {'areas': area_4,
                                          'b_s': (0.75 - b_v, 1 - 2 * b_v)},
                                         {'areas': area_5,
                                          'b_s': (1 - 2 * b_v, 1 - b_v)},
                                         {'areas': area_6,
                                          'b_s': (1 - b_v, 1.25 - 2 * b_v)},
                                         {'areas': area_7,
                                          'b_s': (1.25 - 2 * b_v, 1.5 - 2 * b_v)},
                                         {'areas': area_8,
                                          'b_s': (1.5 - 2 * b_v, 1.75 - 2 * b_v)},
                                         {'areas': area_9,
                                          'b_s': (1.75 - 2 * b_v, 2 - 2 * b_v)}],
                                'b_v': (0, 0.25)},
                               {'b_ss': [{'areas': area_10,
                                          'b_s': (0, 0.75 - b_v)},
                                         {'areas': area_11,
                                          'b_s': (0.75 - b_v, 1 - b_v)},
                                         {'areas': area_12,
                                          'b_s': (1 - b_v, 1.5 - 2 * b_v)},
                                         {'areas': area_13,
                                          'b_s': (1.5 - 2 * b_v, 1.75 - 2 * b_v)},
                                         {'areas': area_14,
                                          'b_s': (1.75 - 2 * b_v, 2 - 2 * b_v)}],
                                'b_v': (0.25, 0.5)},
                               {'b_ss': [{'areas': area_15,
                                          'b_s': (0, 0.75 - b_v)},
                                         {'areas': area_16,
                                          'b_s': (0.75 - b_v, 1.5 - 2 * b_v)},
                                         {'areas': area_17,
                                          'b_s': (1.5 - 2 * b_v, 1 - b_v)},
                                         {'areas': area_18,
                                          'b_s': (1 - b_v, 1.75 - 2 * b_v)},
                                         {'areas': area_19,
                                          'b_s': (1.75 - 2 * b_v, 2 - 2 * b_v)}],
                                'b_v': (0.5, 0.75)},
                               {'b_ss': [{'areas': area_20,
                                          'b_s': (0, 1 - b_v)},
                                         {'areas': area_21,
                                          'b_s': (1 - b_v, 2 - 2 * b_v)}],
                                'b_v': (0.75, 1)}]


def analytical_expected_profit_multi_part(b_v_, b_s_, c_v_, c_s_):
    for case in expressions_using_functions:
        lower_b_v_bound, upper_b_v_bound = case['b_v']
        for b_s_bound in case['b_ss']:
            lower_b_s_bound, upper_b_s_bound = b_s_bound['b_s']
            lower_b_s_bound = lower_b_s_bound if lower_b_s_bound == 0 else lower_b_s_bound.subs([(b_v, b_v_)])
            upper_b_s_bound = upper_b_s_bound.subs([(b_v, b_v_)])
            if lower_b_s_bound <= b_s_ < upper_b_s_bound and lower_b_v_bound <= b_v_ < upper_b_v_bound:
                expression_defi = b_s_bound['areas']
                evaluation = expression_defi(b_v_, b_s_, c_v_, c_s_)[0]
                return evaluation


"""
def case1a(bs, bv, cv=0.2, cs=0.5):
    return -bs ** 3 / 12 - bs ** 2 * bv / 2 + bs ** 2 * cs / 8 + bs ** 2 * cv / 4 - bs * bv ** 2 / 2 + bs * bv * cs / 2 + bs * bv * cv / 2 + bv ** 2 * cs / 4 - bv ** 2 / 2 + bv * cv - 29 * cs / 32 - 29 * cv / 16 + 223 / 256


def case1i(bs, bv, cv=0.2, cs=0.5):
    return bs**3/12 + bs**2*bv/2 - bs**2*cs/8 - bs**2*cv/4 - bs**2/4 + bs*bv**2 - bs*bv*cs/2 - bs*bv*cv - bs*bv + bs*cs/2 + bs*cv + 2*bv**3/3 - bv**2*cs/2 - bv**2*cv - bv**2 + bv*cs + 2*bv*cv - cs/2 - cv + 1/3
"""