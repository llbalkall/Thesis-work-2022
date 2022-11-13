from multipart_partitions import *
import numpy as np
from tqdm import tqdm
import pprint

def eval_para(case: list) -> object:
    """
  Evaluate a case going througth all the partitions and integrate the parameters
  each of them
  Args:
    case: list of Para-s
  """
    simpara = 0
    for param in case:
        simpara += simplify(
            param.pre * integrate(
                param.loc * param.pi,
                (x, param.x_0, param.x_1),
                (y, param.y_0, param.y_1)
            )
        )
    # pretty_print(simplify(simpara))
    return simplify(simpara)


def analytical_multi_part(b_v_, b_s_, c_v_, c_s_):
    for case in expressions:
        lower_b_v_bound, upper_b_v_bound = case['b_v']
        for b_s_bound in case['b_ss']:
            lower_b_s_bound, upper_b_s_bound = b_s_bound['b_s']
            lower_b_s_bound = lower_b_s_bound if lower_b_s_bound == 0 else lower_b_s_bound.subs([(b_v, b_v_)])
            upper_b_s_bound = upper_b_s_bound.subs([(b_v, b_v_)])
            if lower_b_s_bound < b_s_ <= upper_b_s_bound and lower_b_v_bound < b_v_ <= upper_b_v_bound:
                expression = b_s_bound['areas']
                evaluation = expression.evalf(subs={'b_s': b_s_, 'b_v': b_v_, 'c_v': c_v_, 'c_s': c_s_})
                return evaluation


def rewrite_multipart():
    for case in tqdm(cases):
        for b_s_bound in case['b_ss']:
            b_s_bound['areas'] = eval_para(b_s_bound['areas'])
    pprint.pprint(cases)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    expression = eval_para(Case1a)
    # print(expression)
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
