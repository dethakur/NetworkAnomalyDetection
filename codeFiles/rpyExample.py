__author__ = 'devashishthakur'

import rpy2
from rpy2 import robjects


def estimate_cp_r_(ts, method="binseg.mean.CUSUM", Q = 1, penalty_value = 0.1):
    ts = [x / min(ts) for x in ts]
    robjects.r("library(changepoint)")
    method_map = {
                  "mean":"cpt.mean({})",
                  "var": "cpt.var({})",
                  "meanvar":"cpt.meanvar({})",
                  "binseg.mean.CUSUM" : "cpt.mean({},penalty='Manual',test.stat='CUSUM',method='BinSeg',Q={},pen.value={})"
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
# print(estimate_cp_r_([0.006622, 0.006622, 0.006622, 0.006622, 0.006622, 0.011456, 0.011456, 0.011456, 0.011456, 0.011456]))