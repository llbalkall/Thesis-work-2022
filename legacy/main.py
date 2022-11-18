from multipart_partitions import *
import numpy as np
from tqdm import tqdm
import pprint
import matplotlib.pyplot as plt


def eval_sympy_stuff(sympy_expression, i, j, bs, bv):
    if sympy_expression == r14:
        return 0.25
    elif sympy_expression == r34:
        return 0.75
    elif sympy_expression == r94:
        return 2.25
    elif sympy_expression == 0 or sympy_expression == 1:
        return sympy_expression
    else:
        return sympy_expression.subs([(b_v, bv), (b_s, bs), (x, i), (y, j)])


def draw_case(parti_, bss, bvv):

    for i in range(len(case_to_show)):
        draw_case(case_to_show[i], print(parti_))
        iis, jjs, ffs = [], [], []
        for i_ in np.arange(0, 1, 0.01):
            for j_ in np.arange(0, 1, 0.01):
                lower_i = eval_sympy_stuff(parti_.x_0, i_, j_, bss, bvv)
                upper_i = eval_sympy_stuff(parti_.x_1, i_, j_, bss, bvv)
                lower_j = eval_sympy_stuff(parti_.y_0, i_, j_, bss, bvv)
                upper_j = eval_sympy_stuff(parti_.y_1, i_, j_, bss, bvv)
                if lower_i < i_ < upper_i and lower_j < j_ < upper_j:
                    iis.append(i_)
                    jjs.append(j_)
        plt.plot(iis, jjs)

    x1, y1 = [0.25, 0.25], [0, 1]
    x2, y2 = [0, 1], [0.25, 0.25]
    x3, y3 = [0.75, 0.75], [0, 1]
    x4, y4 = [0, 1], [0.75, 0.75]
    plt.xlim(0, 1), plt.ylim(0, 1)
    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4)
    plt.axis('square')
    plt.show()


def integrate_param(param):
    return simplify(
        param.pre * integrate(
            param.loc * param.pi,
            (x, param.x_0, param.x_1),
            (y, param.y_0, param.y_1)
        )
    )


def eval_para(case: list) -> object:
    """
  Evaluate a case going througth all the partitions and integrate the parameters
  each of them
  Args:
    case: list of Para-s
  """
    simpara = 0
    for param in case:
        simpara += integrate_param(param)
    # pretty_print(simplify(simpara))
    return simplify(simpara)


def analytical_multi_part(b_v_, b_s_, c_v_, c_s_):
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


def rewrite_multipart():
    for case in tqdm(cases):
        for b_s_bound in case['b_ss']:
            b_s_bound['areas'] = eval_para(b_s_bound['areas'])
    pprint.pprint(cases)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    case_to_show = Case1f
    for i in range(len(case_to_show)):
        draw_case(case_to_show[i], 1, 0.1)

    rewrite_multipart()

    expression = eval_para(Case1a)
    print(expression)
    rewrite_multipart()
    # print(expression.evalf(subs={'b_s': 0.1, 'b_v': 0.1, 'c_v': 0.5, 'c_s': 0.2}))
    delta = 0.01
    for xx in tqdm(np.arange(0, 1, delta)):
        for yy in np.arange(0, 1, delta):
            analytical_multi_part(xx, yy, 0.5, 0.2)
    """d_b_s = diff(output, b_s)
    d_b_v = diff(output, b_v)
    d_b_s_s = diff(diff(output, b_s), b_s)
    d_b_v_v = diff(diff(output, b_v), b_v)
    d_b_s_v = diff(diff(output, b_s), b_v)
    d_b_v_s = diff(diff(output, b_v), b_s)
    print("o_b_s:", d_b_s)
    print("o_b_v:", d_b_v)
    print("o_b_s_s:", d_b_s_s)
    print("o_b_v_v:", d_b_v_v)
    print("o_b_s_v:", d_b_s_v)
    print("o_b_v_s:", d_b_v_s)

    """
    # print(output.subs([(c_s, 0.2), (c_v, 0.5)]))
    f = open("multioutput", "w")
    f.write(str(expression))
    f.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
