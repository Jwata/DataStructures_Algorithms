#!/bin/python3

import math
import os
import random
import re
import sys

def create_longest_memo(a, b):
    dp = []
    for i in range(len(a)):
        dp.append([])
        for j in range(len(b)):
            if a[i] == b[j]:
                if i == 0 and j == 0:
                    longest = 1
                elif i == 0:
                    longest = min(1, dp[i][j-1] + 1)
                elif j == 0:
                    longest = min(1, dp[i-1][j] + 1)
                else:
                    longest = dp[i-1][j-1] + 1
            else:
                if i == 0 and j == 0:
                    longest = 0
                elif i == 0:
                    longest = dp[i][j-1]
                elif j == 0:
                    longest = dp[i-1][j]
                else:
                    longest = max(dp[i-1][j], dp[i][j-1])

            dp[i].append(longest)
    return dp

def longestCommonSubsequence(a, b):
    dp = create_longest_memo(a, b)
    import pandas as pd
    print(pd.DataFrame(dp, index=a, columns=b))

    i = len(a) - 1
    j = len(b) - 1
    lcs_length = dp[i][j]

    lcs = [None] * lcs_length
    cnt = 0
    while cnt < lcs_length:
        print('i: {}, j: {}, dp[i][j]: {}'.format(i, j, dp[i][j]))
        if a[i] == b[j]:
            print('Common element {} found at {} {}'.format(a[i], i, j))
            pos = -1*(cnt+1)
            lcs[pos] = a[i]
            cnt += 1
            i = max(0, i-1)
            j = max(0, j-1)
        else:
            if i == 0:
                j = j - 1
            elif j == 0:
                i = i - 1
            else:
                if dp[i][j-1] < dp[i][j]:
                    i = i-1
                elif dp[i-1][j] < dp[i][j]:
                    j = j-1
                else:
                    i = i-1

    return lcs

if __name__ == '__main__':
    a = '1 2 3 4 1'.split(' ')
    b = '3 4 1 2 1 3'.split(' ')
    # a = '3 9 8 3 9 7 9 7 0'.split(' ')
    # b = '3 3 9 9 9 1 7 2 0 6'.split(' ')
    result = longestCommonSubsequence(a, b)

    import numpy as np
    print(np.array(result))
