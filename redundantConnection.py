from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode

# In this problem, a tree is an undirected graph that is connected and has no cycles.
#
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
#
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}  # node : setOfNeighbours

        def canReach(f, t, visited):
            if f not in visited:
                visited.add(f)
                if f == t:
                    return True
                else:
                    return any([canReach(n, t, visited) for n in graph.get(f, set())])

        for f, t in edges:
            # add all disconnected nodes to the graph
            # if there's another pair of (f, t) that can reach in the existing graph,
            # the pair builds an edge to the graph
            if canReach(f, t, set()):
                return [f, t]
            else:
                if f not in graph:
                    graph[f] = set()
                graph[f].add(t)
                if t not in graph:
                    graph[t] = set()
                graph[t].add(f)

    # union find triks
    #  find(x) - return the ancestor of x, which group it belongs to
    #  union(x, y) - add an edge between x and y, find ancestor of anceX and anceY
    #     they must be different - otherwise it means x and y are already connected in the same group
    #     to link them, update parent[anceX] = anceY, so later x and y will return the same ancestor
    #     rank is not cenessary
    def findRedundantConnectionUnionFind(self, edges: List[List[int]]) -> List[int]:
        parents = {}
        ranks = {}

        def findParent(x):
            if x not in parents:
                parents[x] = x
                ranks[x] = 0
                return x
            if parents[x] != x:
                return findParent(parents[x])
            else:
                return x

        # when union two nodes, udpate their ancestors' parent
        def union(u, v):
            pu = findParent(u)
            pv = findParent(v)
            if pu == pv:  # there is already an union of u and v, now found another pair
                return False
            else:
                ranku = ranks[pu]
                rankv = ranks[pv]
                if ranku == rankv:
                    parents[pv] = pu
                    ranks[pu] += 1
                elif ranku > rankv:
                    parents[pv] = pu
                else:
                    parents[pu] = pv
                return True

        for u, v in edges:
            print(" checking ", u, v)
            if not union(u, v):
                return [u, v]


    def findRedundantConnectionUnionFindNoRanks(self, edges: List[List[int]]) -> List[int]:
        parents = {}
        def finAncestor(x):
            if x not in parents:
                parents[x] = x
            if x == parents[x]:
                return x
            return finAncestor(parents[x])

        def union(u, v):
            uAnces = finAncestor(u)
            vAnces = finAncestor(v)
            if uAnces == vAnces:
                return False
            else:
                parents[uAnces] = vAnces # no need to have rank, just set any ancesor's parent to the other ancesotr
                return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []


if __name__ == '__main__':
    print(Solution().findRedundantConnectionUnionFindNoRanks([[3,4],[1,2],[2,4],[3,5],[2,5]]))