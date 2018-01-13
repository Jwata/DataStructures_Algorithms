def get_products_of_all_ints_except_at_index(ints):
    products_exepct_zeros = 1
    zero_count = 0

    # O(n)
    for n in ints:
        if n == 0:
            zero_count += 1
        else:
            products_exepct_zeros = products_exepct_zeros * n

    # O(n)
    products = []
    for m in ints:
        if zero_count == 0:
            product = products_exepct_zeros // m
        elif zero_count == 1 and m == 0:
            product = products_exepct_zeros
        else: # the other elements includes at least one zero
            product = 0

        products.append(product)

    return products

products = get_products_of_all_ints_except_at_index([1, 7, 3, 4])
print(products)
# should be [84, 12, 28, 21]

products = get_products_of_all_ints_except_at_index([1, 7, 3, 0])
print(products)
# should be [0, 0, 0, 21]

products = get_products_of_all_ints_except_at_index([1, 0, 3, 0])
print(products)
# should be [0, 0, 0, 0]
