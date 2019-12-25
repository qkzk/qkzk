def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)


if __name__ == '__main__':
    fact_5 = fact(5)
    print(fact_5)
