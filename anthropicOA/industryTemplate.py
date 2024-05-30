# industry template

class Solution:
    def __init__(self):
        pass

    def add(self, v):
        return "added"

    def delete(self, v):
        return "deleted"

    def getMdian(self):
        return "getMdian"


def solution(queries):
    s = Solution()
    ret = []
    for query in queries:
        op = query[0]
        if op == 'ADD':
            num = query[1]
            ret.append(s.add(num))
        elif op == 'DELETE':
            num = query[1]
            ret.append(s.delete(num))
        elif op == 'GET_MEDIAN':
            ret.append(s.getMdian())
    return ret



queries = [
    ["ADD", "10"],
    ["ADD", "100"],
    ["DELETE", "100"],
    ["GET_MEDIAN"],
]
print(solution(queries))
