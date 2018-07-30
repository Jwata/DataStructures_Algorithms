def coin_combination(amount, denoms):
    comb_memo = [0]*(amount+1)
    comb_memo[0] = 1

    for denom in denoms:
        for a, count in enumerate(comb_memo):
            if a < denom:
                continue
            comb_memo[a] = comb_memo[a] + comb_memo[a-denom]

    return comb_memo

amount = 4
denoms = [1, 2, 3]
comb = coin_combination(amount, denoms)
print(comb)

amount = 5
denoms = [1, 3, 5]
comb = coin_combination(amount, denoms)
print(comb)

amount = 5
denoms = [3, 7]
comb = coin_combination(amount, denoms)
print(comb)
