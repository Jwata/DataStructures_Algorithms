import string

def reverse_alphabets(s):
    buf = []

    for c in s:
        if c in string.ascii_letters:
            buf.append(c)

    r_str = ''
    for i in range(len(s)):
        if s[i] in string.ascii_letters:
            r_str += buf.pop()
        else:
            r_str += s[i]

    return r_str

s = "Ab,c,de!$"
print(reverse_alphabets(s))
