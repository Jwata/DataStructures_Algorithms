#!/usr/bin/env python

def find_highest_product_of_three(list_of_ints):
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        # update highest product of 3
        highest_product_of_3 = max(
                highest_product_of_3,
                highest_product_of_2 * current,
                lowest_product_of_2 * current)

        highest_product_of_2 = max(
                highest_product_of_2,
                highest * current,
                lowest * current)

        lowest_product_of_2 = min(
                lowest_product_of_2,
                highest * current,
                lowest * current)

        highest = max(highest, current)

        lowest = min(lowest, current)

    return highest_product_of_3

product = find_highest_product_of_three([1, 3, 2, 4, 6, 1])
print(product)
# should be 3 * 4 * 6 = 72

product = find_highest_product_of_three([1, 10, -5, 1, -100])
print(product)
# should be 10 * -5 * -100 = 5000
