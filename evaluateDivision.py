from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # from : [(to, valule)]
        graph = {}
        for i in range(len(equations)):
            left, right = equations[i]
            result = values[i]
            if left not in graph:
                graph[left] = []
            graph[left].append([right, result])

            if right not in graph:
                graph[right] = []
            graph[right].append([left, 1 / result])

        ret = []

        print(" graph", graph)
        visited = set()

        def dfs(start, end, cur):
            print(" start", start, " visited", visited)
            if start == end:
                return cur
            else:
                if start not in graph:
                    return None
                visited.add(start)
                for neighbour, result in graph[start]:
                    if neighbour not in visited:
                        print(" checking ", start, "and", neighbour)
                        # start/neighbour == result
                        dfsResult = dfs(neighbour, end, cur * result)
                        if dfsResult is not None:
                            return dfsResult
                return None

        for qLeft, qRight in queries:
            visited = set()
            result = dfs(qLeft, qRight, 1)
            if result is not None:
                ret.append(result)
            else:
                ret.append(-1.0)
        return ret


if __name__ == '__main__':
    print(Solution().calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["x","x"]]))