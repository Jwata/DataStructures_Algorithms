def get_products_of_all_ints_except_at_index(int_list):
    num_ints = len(int_list)

    products_of_all_ints_except_at_index = [None] * len(int_list)

    product_so_far = 1
    for i in range(num_ints):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]

    product_so_far = 1
    for i in range(num_ints):
        j = num_ints - i - 1
        products_of_all_ints_except_at_index[j] *= product_so_far
        product_so_far *= int_list[j]

    return products_of_all_ints_except_at_index

products = get_products_of_all_ints_except_at_index([1, 7, 3, 4])
print(products)
# should be [84, 12, 28, 21]

products = get_products_of_all_ints_except_at_index([1, 7, 3, 0])
print(products)
# should be [0, 0, 0, 21]

products = get_products_of_all_ints_except_at_index([1, 0, 3, 0])
print(products)
# should be [0, 0, 0, 0]

