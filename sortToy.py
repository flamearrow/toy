from functools import cmp_to_key

class ToSor:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


def comp(a, b):
    return len(a.name) - len(b.name)


if __name__ == '__main__':
    names =  ["a", "ab", "cde", "egf", "z"]
    # toSorts = list(map(lambda a: ToSor(a), names))
    toSorts = [ToSor(a) for a in names]
    sorted = sorted(toSorts, key=cmp_to_key(comp))
    toSorts.sort(key=cmp_to_key(comp))
    for s in toSorts:
        print(s)


