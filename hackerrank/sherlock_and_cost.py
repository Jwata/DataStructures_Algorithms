#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(B):
    i = 0
    j = 1

    dp = {}
    for v in range(1, B[0]+1):
        dp[v] = 0

    while j < len(B):
        new_dp = {}
        for vj in range(1, B[j]+1):
            max_cost_vj = 0
            for vi, cost in dp.items():
                cost_vj_vi = cost + abs(vj - vi)
                max_cost_vj = max([max_cost_vj, cost_vj_vi])
            new_dp[vi] = max_cost_vj
        # update params
        dp = new_dp
        i+=1
        j+=1

    return max(dp.values())

if __name__ == '__main__':
    Bs = [
            [10, 1, 10, 1, 10],
            [100, 2, 100, 2, 100],
        ]
    for B in Bs:
        result = cost(B)
        print(B, result)
