def find_palindromic_paritions(a):
    n = len(a)

    solutions = []
    for i in range(n):
        if is_palindromic(a[:i+1]):
            solution = [a[:i+1]]

            sub_solutions = find_palindromic_paritions(a[i+1:])
            if len(sub_solutions) == 0:
                solutions.append(solution)
            else:
                for s in sub_solutions:
                    solutions.append(solution + s)

    return solutions

def is_palindromic(a):
    n = len(a)
    i = 0
    j = n -1

    while i < j:
        if a[i] != a[j]:
            return False
        i += 1
        j -= 1

    return True

a = "nitin"
print(find_palindromic_paritions(a))
