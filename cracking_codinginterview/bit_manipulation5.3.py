import math

def flip_longest(a):
    cnt = 0
    seqs = []
    longest = 0

    while a > 0: 
        if a & 1:
            cnt += 1
        else:
            seqs.append(0)

        a >>= 1

        if not a & 1 and cnt > 0:
            seqs.append(cnt)
            cnt = 0
            longest = max(sum(seqs[-3:]) + 1, longest)

    return longest

## Debug
# a = 0 # 0
# seqs = [1, 0, 1, 0, 2]
# cnt = 2
# longest = 4

print(flip_longest(1775)) # 8
