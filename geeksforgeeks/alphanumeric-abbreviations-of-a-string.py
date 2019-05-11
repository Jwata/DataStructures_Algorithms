def all_abbrs(s):
    return all_abbrs_helper(s, '')

def all_abbrs_helper(s, pre):
    if len(s) == 0 :
        return [pre]

    abbrs = []
    abbrs += all_abbrs_helper(s[1:], pre+s[0])

    if len(pre) > 0:
        prev_n = char_to_number(pre[-1])
        if prev_n and prev_n < 9:
            pre = pre[:-1] + str(prev_n + 1)
            abbrs += all_abbrs_helper(s[1:], pre)
        else:
            abbrs += all_abbrs_helper(s[1:], pre+'1')
    else:
        abbrs += all_abbrs_helper(s[1:], pre+'1')

    return abbrs

def char_to_number(c):
    d = {str(i): i for i in range(0, 10)}
    if c in d:
        return d[c]
    return None

s = 'AB'
print(all_abbrs(s))

s = 'ABC'
print(all_abbrs(s))

s = 'ANKS'
print(all_abbrs(s))
