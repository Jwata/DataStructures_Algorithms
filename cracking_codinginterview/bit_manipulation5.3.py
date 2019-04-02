import math

# Let b is the lengts of bits of a
# Time O(b), Space O(b)
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

# Time: O(b), Space: O(1)
def flip_longest_optimal(a):
    seq = 0
    prev_seq = 0
    longest = 1

    while a > 0:
        if a & 1:
            seq += 1
        else:
            if a & 2:
                prev_seq = seq
            else:
                prev_seq = 0
            seq = 0

        longest = max(seq+prev_seq+1, longest)
        a >>= 1

    return longest

# Debug
# a_2 = 10
# seq = 0
# prev_seq = 1
# longest = 2

print(flip_longest_optimal(1775)) # 11011101111 -> 8
print(flip_longest_optimal(1700)) # 11010100100 -> 4
