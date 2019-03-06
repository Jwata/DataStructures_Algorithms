def next_greater_elements(arr):
    n = len(arr)
    buf = []
    nge = []

    for i in range(n-1, -1, -1):
        while len(buf) > 0 and buf[-1] < arr[i]:
            buf.pop()

        if len(buf) > 0:
            nge.append(buf[-1])
        else:
            nge.append(-1)

        buf.append(arr[i])

    return nge
def next_greater_elements(arr):
    n = len(arr)
    buf = []
    nge = []

    for i in range(n-1, -1, -1):
        while len(buf) > 0 and buf[-1] < arr[i]:
                buf.pop()
        if len(buf) > 0:
            nge.append(buf[-1])
        else:
            nge.append(-1)

        buf.append(arr[i])

    nge.reverse() # O(n)

    return nge

arr = [4, 5, 2, 25]
print(next_greater_elements(arr)) # [5, 25, 25, -1]
