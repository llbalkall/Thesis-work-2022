from multipart_partitions import *
import numpy as np

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
    for case in cases:
        print("=====================================")
        print(case['b_s'])
        lower_b_s_bound, upper_b_s_bound = case['b_s']
        print(lower_b_s_bound, upper_b_s_bound)
        for b_v_bound in case['b_vs']:
            lower_b_v_bound, upper_b_v_bound = b_v_bound['b_v']
            print(lower_b_v_bound, upper_b_v_bound)
            print(type(lower_b_v_bound), type(upper_b_v_bound))
            print(lower_b_s_bound < b_s_ <= upper_b_s_bound)
            lower_b_v_bound = lower_b_v_bound if isinstance(lower_b_v_bound, int) else lower_b_v_bound.subs([(b_s, b_s_)])
            upper_b_v_bound = upper_b_v_bound if isinstance(upper_b_v_bound, int) else upper_b_v_bound.subs([(b_s, b_s_)])
            print("Ráázzz", lower_b_v_bound.subs([(b_s, b_s_)]) < b_v_ <= upper_b_v_bound.subs([(b_s, b_s_)]))
            if lower_b_s_bound < b_s_ <= upper_b_s_bound and lower_b_v_bound < b_v_ <= upper_b_v_bound:
                expression = eval_para(b_v_bound['areas'])
                print(expression)
                evaluation = expression.evalf(subs={'b_s': b_s_, 'b_v': b_v_, 'c_v': c_v_, 'c_s': c_s_})
                print(evaluation)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    expression = eval_para(Case1a)
    print(expression)
    print(expression.evalf(subs={'b_s': 0.1, 'b_v': 0.1, 'c_v': 0.5, 'c_s': 0.2}))
    for x in np.arange(0, 1, 0.01):
        for y in np.arange(0, 1, 0.01):
            analytical_multi_part(x, y, 0.5, 0.2)
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
