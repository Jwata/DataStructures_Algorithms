def n_bonachi(n, m):
    if n <= 1:
        raise Exception("n must be grather than 1")

    arr = [] 
    for i in range(m):
        if i < n - 1:
            arr.append(0)
        elif i <= n:
            arr.append(1) 
        else:
            x = arr[i-1] * 2 - arr[i-n-1]
            arr.append(x)
    return arr

print(n_bonachi(2, 10))
print(n_bonachi(3, 10))
print(n_bonachi(4, 10))
print(n_bonachi(5, 10))
