from analytical_results import *

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from random import random
from profit_functions import *
from distributions import *
from expected_profit import *
from optimal_bids import *
from constants import *


test_p1, test_p2 = 0.1, 0.1
test_b, test_bb, test_bv, test_bs = 0.4, 0.4, 0.2, 0.5
test_cs, test_cv = 0.5, 0.2

""" Simple bidding """
profit_simple(test_p1, test_p2, test_b, test_cs, test_cv)
expected_profit(test_b, test_cs, test_cv, stepwise_distribution, profit_simple)
analytical_expected_profit_simple(test_b, test_cs, test_cv)
analytical_optimal_bid_simple(test_cs, test_cv)
simulation_optimal_bid_simple(test_cs, test_cv)


""" Block bidding """
profit_block(test_p1, test_p2, test_bb, test_cs, test_cv)
expected_profit(test_bb, test_cs, test_cv, stepwise_distribution, profit_block)
analytical_expected_profit_block(test_bb, test_cs, test_cv)
analytical_optimal_bid_block(test_cs, test_cv)

""" Multipart bidding """
profit_multipart(test_p1, test_p2, (test_bs, test_bv), test_cs, test_cv)
expected_profit((test_bs, test_bv), test_cs, test_cv, stepwise_distribution, profit_multipart)
analytical_expected_profit_multi_part(test_bs, test_bv, test_cs, test_cv)
# optimal_bid_multipart(test_cs, test_cv)


validate_optimal_bid_simple()