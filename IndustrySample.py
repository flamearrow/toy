class Solution:
    def __init__(self):
        self.l = list()

    def add(self, val):
        self.l.append(int(val))

    def delete(self, val):
        toRemove = int(val)
        if toRemove in self.l:
            self.l.remove(toRemove)
            return "true"
        else:
            return "false"

    def size(self):
        return str(len(self.l))

    def hasMore(self):
        if self.l:
            return "true"
        else:
            return "false"

    def getMdian(self):
        if not self.l:
            return ""
        s = sorted(self.l)
        if (len(s) % 2) == 0:
            return str(s[int(len(s) / 2) - 1])
        else:
            return str(s[len(s) // 2])


def solution(queries):
    s = Solution()
    ret = []
    for query in queries:
        op = query[0]
        if op == 'ADD':
            num = query[1]
            s.add(num)
            ret.append(s.size())
        elif op == 'DELETE':
            num = query[1]
            ret.append(s.delete(num))
        elif op == 'GET_MEDIAN':
            ret.append(s.getMdian())
    return ret


if __name__ == '__main__':
    print(solution(
        [["ADD", "10"],
         ["ADD", "100"]]
    )
    )