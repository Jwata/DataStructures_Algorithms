def coin_combination(amount, denoms):
    default_comb = (0, 0, 0)
    comb_memo = {}

    for a in range(amount+1):
        combs = set()
        if a == 0:
            combs.add(default_comb)

        for denom in denoms:
            if denom > a:
                continue
            if not (a-denom) in comb_memo:
                base_combs = set([default_comb])
            else:
                base_combs = comb_memo[a-denom]
            for base_comb in base_combs:
                lst = list(base_comb)
                lst[denom-1] += 1
                combs.add(tuple(lst))
        comb_memo[a] = combs

    return comb_memo[amount]

amount = 4
denoms = [1, 2, 3]
comb = coin_combination(amount, denoms)
print(comb)
