#!/bin/python3

import math
import os
import random
import re
import sys


class Transmitter:
    def __init__(self, xmtr_house, k):
        self.houses = [xmtr_house]
        self.position = xmtr_house
        self.k = k

    def is_covered(self, location):
        min_pos = self.position - self.k
        max_pos = self.position + self.k

        return location in range(min_pos, max_pos + 1)

    def can_move(self, house):
        return house - self.k <= self.houses[0]


# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    x.sort()

    xmtr = None
    fixed_xmtrs = []
    for loc in x:
        if not xmtr:
            xmtr = Transmitter(loc, k)
            continue
        if xmtr.is_covered(loc):
            xmtr.houses.append(loc)
            if xmtr.can_move(loc):
                xmtr.position = loc
        else:
            fixed_xmtrs.append(xmtr.position)
            xmtr = Transmitter(loc, k)
    fixed_xmtrs.append(xmtr.position)
    return len(fixed_xmtrs)


if __name__ == '__main__':

    cases = [
        ['1 2 3 4 5', 1],
        ['7 2 4 6 5 9 12 11', 2]
    ]

    for case in cases:
        x = list(map(int, case[0].split(' ')))
        k = case[1]
        result = hackerlandRadioTransmitters(x, k)
        print(result)
