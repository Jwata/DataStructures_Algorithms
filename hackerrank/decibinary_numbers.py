for(d=0;d<20;d++)
    FOR(x,300000) if(dp[d][x])
    FOR(y,10) if(x+(y<<d)<300000)
        dp[d+1][x+(y<<d)] += dp[d][x];


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
    db = 0
    dec = 0

    while index < x:
        index += 1

        dec, db = heapq.heappop(queue)
        while len(queue) > 0 and (dec, db) == queue[0]:
            heapq.heappop(queue)
        # print(index, db, dec)

        if db % 10 < 9:
            heapq.heappush(queue, (dec+1, db+1))

        #if db % 10 == 0:
        #    for n in range(1, n_db):
        #        heapq.heappush(queue, (dec+2**n, db+10**n))
        # increment db
        next_dec, next_db = queue[0]
        if next_dec > dec and dec % 2 == 0:
            _db = db
            while _db % 10 > 0:
                _db = _db - 2 + 10
                heapq.heappush(queue, (decibinary_to_decimal(_db), _db))

            n_db = len_db(db)
            if 2**n_db == dec:
                if not (2**n_db, 10**n_db) == queue[0]:
                    heapq.heappush(queue, (2**n_db, 10**n_db))

    return db, dec

def len_db(x):
    n = 0
    while x > 0:
        n += 1
        x = x // 10
    return n 

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
    for i in range(101):
        # print('From: {}, to: {}'.format(i*10, (i+1)*10-1))
        dcimals = [decibinary_to_decimal(db) for db in range(i*10, (i+1)*10)]
        print(i*10, (i+1)*10-1, dcimals)

    for x in range(637+1):
        db, dec = decibinary_numbers(x)
        print(x, db, dec)

    # inputs = open('data/decibinary.input02.txt').readlines()
    # outputs = open('data/decibinary.output02.txt').readlines()
    inputs = open('data/decibinary.input03.txt').readlines()
    outputs = open('data/decibinary.output03.txt').readlines()

    err_count = 0
    for i in range(len(inputs)-1):
        x = int(inputs[i+1])
        expected = int(outputs[i])
        db, dec = decibinary_numbers(x)
        try:
            assert db == expected, 'expected: {}'.format(expected)
        except AssertionError as err:
            print('input: {}, db: {}, dec: {}'.format(x, db, dec))
            print(err)
            err_count += 1
            if err_count > 10:
                break
