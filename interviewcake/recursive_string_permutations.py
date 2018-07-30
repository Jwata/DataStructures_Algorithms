def find_permutations(string):
    perms = []
    for i in range(len(string)):
        perms.append(set())
        char = string[i]
        if i == 0:
            perms[i].add(char)
        else:
            for perm in perms[i-1]:
                for pos in range(len(perm)+1):
                    new_perm = perm[0:pos] + char + perm[pos:]
                    perms[i].add(new_perm)

    return perms[-1]

def find_permutations_recursive(string):
    if len(string) <= 1:
        return set([string])

    perms_except_last = string[:-1]
    last_char = string[-1]

    permutations_exclude_last = find_permutations_recursive(perms_except_last)

    perms = set()
    for perm in permutations_exclude_last:
        for pos in range(len(string)):
            new_perm = perm[0:pos] + last_char + perm[pos:]
            perms.add(new_perm)

    return perms


perms = find_permutations('junji')
print(len(perms))
print(perms)

perms = find_permutations_recursive('junji')
print(len(perms))
print(perms)
