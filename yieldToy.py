def blah(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


if __name__ == '__main__':
    print(list(blah(5)))
