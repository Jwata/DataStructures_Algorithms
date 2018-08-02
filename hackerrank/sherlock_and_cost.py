#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cost function below.
def cost(B):
    j = 1
    dp = ((1, 0), (B[0], 0))

    while j < len(B):
        (min_ai, cost_at_min_ai), (max_ai, cost_at_max_ai) = dp
        min_aj, max_aj = 1, B[j]

        max_cost_at_min_aj = cost_at_max_ai + abs(max_ai - min_aj)
        max_cost_at_max_aj = max([
            cost_at_min_ai + abs(max_aj - min_ai),
            cost_at_max_ai + abs(max_ai - max_aj)
        ])

        dp = ((min_aj, max_cost_at_min_aj), (max_aj, max_cost_at_max_aj))
        j+=1

    (_, cost1), (_, cost2) = dp
    return max([cost1, cost2])

if __name__ == '__main__':
    Bs = [
            [10, 1, 10, 1, 10],
            [100, 2, 100, 2, 100],
        ]
    for B in Bs:
        result = cost(B)
        print(B, result)
