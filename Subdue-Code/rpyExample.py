__author__ = 'devashishthakur'

import rpy2
from rpy2 import robjects


def estimate_cp_r_(ts, method="binseg.mean.CUSUM", Q=1, penalty_value=0.01):
    ts = [x / min(ts) for x in ts]
    # print(ts)
    robjects.r("library(changepoint)")
    method_map = {
        "mean": "cpt.mean({})",
        "var": "cpt.var({})",
        "meanvar": "cpt.meanvar({})",
        "binseg.mean.CUSUM": "cpt.mean({},penalty='Manual',test.stat='CUSUM',method='BinSeg',Q={},pen.value={})"
    }
    mt = robjects.FloatVector(ts)
    robjects.globalenv["mt"] = mt
    if method == "binseg.mean.CUSUM":
        cmd = method_map[method].format("mt", Q, penalty_value)

    else:
        cmd = method_map[method].format("mt")
    robjects.globalenv["mycpt"] = robjects.r(cmd)
    ecp = robjects.r("cpts(mycpt)")
    return ecp

# print(estimate_cp_r_([0.004686, 0.004686, 0.004686, 0.004686, 0.004686, 0.004639, 0.004639, 0.004639, 0.004639, 0.004639]))
# print(
# estimate_cp_r_(
#         [0.006622, 0.006622, 0.006622, 0.006622, 0.006622, 0.011456, 0.011456, 0.011456, 0.011456, 0.011456]))

# arr = [1, 2, 3, 4, 5]
# arr = [0.12337662337662343, 0.14459930313588834, 0.20491803278688514, 0.073937153419593241, 0.19750889679715289, -0.031315240083507376, 0.2473684210526314, 0.042693926638604926, 0.20512820512820512, -1.5000000000000027, -0.026673338208690944, 0.2158940397350993, 0.20412517780938841, 0.19696969696969674, 0.17965023847376793]
# val = estimate_cp_r_(arr)
# print val

