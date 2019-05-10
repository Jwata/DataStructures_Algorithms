def find_longest(x):
    n = len(x)

    if n == 0:
        return 0
    if n == 1:
        return 1        

    for i in range(n//2):
        matched = False
        for j in range(i+1):
            if x[j] != x[-i+j-1]:
                break
            if j == i:
                matched = True
        if matched:
            return 2 + find_longest(x[i+1:n-1-i])

    return 1

print(find_longest('aba'))
print(find_longest('merchant'))
print(find_longest('ghiabcdefhelloadamhelloabcdefghi'))
print(find_longest('antaprezatepzapreanta'))
