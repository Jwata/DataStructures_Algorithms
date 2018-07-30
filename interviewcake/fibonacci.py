def fib(n):
    fib_memo = [0, 1]

    step = 0
    while len(fib_memo) < n + 1:
        step += 1
        fib_memo.append(fib_memo[-2] + fib_memo[-1])

    return fib_memo[n], step

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(9))
print(fib(100))
