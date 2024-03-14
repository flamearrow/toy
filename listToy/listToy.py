if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    l[1], l[2], l[3] = l[2], l[3], l[1]
    doubleL = list(map(lambda i: i*2, l))
    print(doubleL)
    filteredL = list(filter(lambda i: i % 2 == 0, l))
    print(filteredL)