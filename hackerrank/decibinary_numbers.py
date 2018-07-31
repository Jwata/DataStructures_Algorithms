#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

def decibinary_numbers(x):
    # priority queue [(decimal, decibinary), ...]
    queue = [(0, 0)]
    index = 0

    while index < x:
        index += 1

        dec, db = heapq.heappop(queue)
        # print(index, db, dec)

        if db % 10 < 9:
            heapq.heappush(queue, (dec+1, db+1))
        if db % 10 == 0:
            heapq.heappush(queue, (dec+2, db+10))
            if dec >= 2:
                n_db = int(math.log(dec, 2)) + 1
                heapq.heappush(queue, (2**n_db, 10**n_db))

    return db, dec


def decibinary_to_decimal(x):
    digit = 0
    i = 0
    while x > 0:
        n = x % 10
        digit += n * pow(2, i)
        x = x // 10
        i += 1
    return digit

if __name__ == '__main__':
    xs = [1, 2, 3, 4, 10]

    # for i in range(101):
    #     # print('From: {}, to: {}'.format(i*10, (i+1)*10-1))
    #     dcimals = [decibinary_to_decimal(db) for db in range(i*10, (i+1)*10)]
    #     print(i*10, (i+1)*10-1, dcimals)
    for x in range(1, 11):
        db, dec = decibinary_numbers(x)
        print('Answer', x, db, dec)
