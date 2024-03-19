import random

if __name__ == '__main__':
    l = [1, 5, 3, 2, 4]
    i = random.choices(l, k=2)
    print(i)
    ll = list(filter(lambda x: x % 2 == 0, l))
    print(ll)
    lll = list(map(lambda x: x * 2, l))
    print(lll)

    llll = sorted(l, key=lambda x: x)
    print(llll)
    l.sort(key = lambda x: x)
    print(l)
    for index, value in enumerate(lll):
        print("index", index, "value", value)
