from functools import reduce

def testZip():
    l = [1,2,3,4]
    def is_sorted(l):
        ll = zip(l, l[1:]) # zip creates a list of pair of length the min of the two, so this is a pariwise
        return all(x < y for (x, y) in ll)

    print(is_sorted(l))


def testReduce(l):
    sum = reduce(lambda x, y: x + y, l) # with initial value, the first element will be initial value
    print(sum)


if __name__ == '__main__':
    # l = [1, 2, 3, 4, 5]
    # l[1], l[2], l[3] = l[2], l[3], l[1]
    # doubleL = list(map(lambda i: i*2, l))
    # print(doubleL)
    # filteredL = list(filter(lambda i: i % 2 == 0, l))
    # print(filteredL)
    # testZip()
    testReduce([1, 2, 4, 3])

