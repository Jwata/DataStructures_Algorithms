def pow_mod_p(x, y, p):
    x = x % p # 2
    
    r = 1
    while y > 0:
        if y % 2 == 0:
            y = y / 2
            x = (x * x)  % p
        else:
            y = y - 1
            r = (r * x) % p

    return r

x = 2
y = 3
p = 5
print(pow_mod_p(x,y,p)) # 3

x = 2
y = 5
p = 13
print(pow_mod_p(x,y,p)) # 6

