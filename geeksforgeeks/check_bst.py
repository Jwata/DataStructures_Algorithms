def is_bst(arr):
    if len(arr) == 0:
        raise Exception("empty input")

    parents = [arr[0]]
    min_v = INT_MIN

    for i in range(n):
if arr[i] < min_v: # check
    return False
while parents:
if arr[i] < parents[-1]:
    break
min_v = parents.pop()

parents.append(arr[i])

return True

