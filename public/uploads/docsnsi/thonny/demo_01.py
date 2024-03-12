def syracuse(u):
    if u % 2 == 0:
        res = u // 2
    else:
        res = 3 * u + 1
    return res


def terme_syracuse(a, n):
    u = a
    for _ in range(n):
        u = syracuse(u)
    return u
