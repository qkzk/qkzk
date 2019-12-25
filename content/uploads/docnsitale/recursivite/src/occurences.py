def occurrences(c, s):
    if s == "":
        return 0
    elif c == s[0]:
        return 1 + occurrences(c, s[1:])
    else:
        return occurrences(c, s[1:])


if __name__ == '__main__':
    nbr_k = occurrences(
        "k", "konieczko")
    print(nbr_k)

    nbr_k = occurrences(
        "k",
        "konieczko ankylosé blackboule dans les balkans, kidnappe le khan, kiffe les bureks, zouk pour un kilo de markka"
    )  # 13
    print(nbr_k)
