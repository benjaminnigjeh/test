d = 1
def fd(n):
    if n == 1 or n== 2:
        return 1
    else:
        d = fd(n-1) + fd(n-2)
    return d

