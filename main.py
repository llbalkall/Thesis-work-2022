from multipart_partitions import *


def eval_para(case: list):
    """
  Evaluate a case going throuth all the partitions and integrate the parameters
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
    pretty_print(simplify(simpara))
    return simplify(simpara)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    latex_output = latex(eval_para(Case4b))
    print(latex_output)
    f = open("Output", "w")
    f.write(latex_output)
    f.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
