def pair(n):
    if n == 0:
        return True
    else:
        return impair(n-1)


def impair(n):
    if n == 0:
        return False
    else:
        return pair(n-1)


if __name__ == '__main__':
    p_5 = pair(5)
    print(f'5 est-il pair ? {p_5}')
