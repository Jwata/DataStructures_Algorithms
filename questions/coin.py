# https://www.interviewcake.com/question/python/coin

def change_possibilities(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount+1)
    ways_of_doing_n_cents[0] = 1 # always 1 pattern to make zero

    for d in denominations:
        for n_cents in range(d, len(ways_of_doing_n_cents)):
            if n_cents >= d:
                ways_of_doing_n_cents[n_cents] += ways_of_doing_n_cents[n_cents - d]

    return ways_of_doing_n_cents[amount]

p = change_possibilities(4, [1,2,3])
print(p) # should be 4

p = change_possibilities(5, [3, 7])
print(p) # should be 0

p = change_possibilities(5, [1, 3, 5])
print(p) # should be 3
