from random import randint
import math

def find_missing_integer(A, N, num_bits):
    m = 0
    j = 0
    idxs = range(N-1)

    while j < num_bits:
        ones = []
        zeros = []

        for i in idxs:
            if A[i][num_bits-j-1] == '1':
                ones.append(i)
            else:
                zeros.append(i)

        if len(ones) < len(zeros):
            m |= (1 << j)
            idxs = ones
        else:
            idxs = zeros

        j += 1

    return m

N = 16
num_bits = 4

A = [a for a in range(N)]
expected = A.pop(randint(0, N-1))
print("Expected: {}".format(expected))
A = ['{:4b}'.format(a) for a in A]
answer = find_missing_integer(A, N, num_bits)
print("Answer: {}".format(answer))
