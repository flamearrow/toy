if __name__ == '__main__':
    d = {"a": 12, "b": 23, "c": 1, "d": 15}
    print(d.get("c", 123))
    print(d.get("a"))

    unsortedMap = dict(d.items())

    print(unsortedMap)

    sortedTupleArrays = list(sorted(d.items(), key=lambda item: item[1]))
    print(sortedTupleArrays)

    sortedMap = dict(sorted(d.items(), key=lambda item: item[1]))
    print(sortedMap)

    mappedArrays = list(map(lambda item: item[1] * 10, sortedTupleArrays))
    print(mappedArrays)

    values = ((3, 2), (3, 4), (5, 6))
    createddict = dict(values)
    print(createddict)

