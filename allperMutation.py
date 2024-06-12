# given [1,2,3] - generate all its permutations

def permute(oriList):
    ret = []

    def search(cur, remaining):
        if len(remaining) == 0:
            ret.append(cur.copy()) # either copy here, or create a new cur in search recurisve call
        else:
            for i in range(0, len(remaining)):
                cur.append(remaining[i])
                search(cur, remaining[:i] + remaining[i + 1:])
                cur.pop()

    search([], oriList)
    return ret


if __name__ == '__main__':
    print(permute([1, 2, 3]))
