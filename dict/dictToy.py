def containsDict(dict1, dict2):
    # for (key, value) in dict2.items():
    #     if key in dict1 and dict1[key] == value:
    #         continue
    #     else:
    #         return False
    # return True
    for (key, value) in dict2.items():
        if key not in dict1 or dict1[key] != value:
            return False
    return True


def containsDict2(dict1, dict2):
    arr = list(item for item in dict2.items())
    print(arr)
    arr2 = list(item in dict1.items() for item in dict2.items())
    print(arr2)
    return all(item in dict1.items() for item in dict2.items())


if __name__ == '__main__':
    dict1 = {1: 2, 3: 4}
    dict2 = {1: 2, 3: 4, 5: 6}
    print(containsDict2(dict2, dict1))
