def max_duffel_bag_value(cake_tuples, capacity):
    M = [0] * (capacity + 1)

    for w, v in cake_tuples:
        for c in range(capacity+1):
            if c < w:
                continue
            max_cand = M[c-w] + v
            M[c] = max([M[c], max_cand])

    return M[capacity]


cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

# Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
max_value = max_duffel_bag_value(cake_tuples, capacity)
print(max_value)
