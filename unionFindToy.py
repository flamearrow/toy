from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode


# idea of union find:
#  * 1d array parents[]: save the parents of each node
#  *     in the end, all connected nodes will have the same parent, distinct parent count is distinct island cont
#  * fun union(node1, node2) - connect node1 and node2, set their parents to be the same
#     * only need to update the ancestor in the parents[] once
#  * fun find(node) - find the root(island number) of node - keep looking until parent[node] == node
#    insert one if not seen before


# Build the parents graph:
#  * initialize parent[i] == i if i is "1", or -1 - now each "1" is a separete island
#  * for each i, see if it can be union with its neighbour j, if can
#    * union(i, j) - check the root - rootI, rootJ -
#      * if rootI==rootJ, they alrady have same parent,
#      * otherwise, check rankI and rankJ, higher rank acts as parent. parent[lower] = higher,
#      * otherwise rankI == rankJ = these two haven't connected yet, use anyOne as parent, and increase its rank,
#           so that later the higher rank node will also be used as parent


class UnionFind:
    def __init__(self, grid):
        self.count = 0
        m, n = len(grid), len(grid[0])
        self.parent = []
        self.rank = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i * n + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    # "root of X: keep looking for parent until parent[i] = i
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        uf = UnionFind(grid)

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    if r - 1 >= 0 and grid[r - 1][c] == "1":  # up
                        uf.union(r * nc + c, (r - 1) * nc + c)
                    if r + 1 < nr and grid[r + 1][c] == "1":  # down
                        uf.union(r * nc + c, (r + 1) * nc + c)
                    if c - 1 >= 0 and grid[r][c - 1] == "1":  # left
                        uf.union(r * nc + c, r * nc + c - 1)
                    if c + 1 < nc and grid[r][c + 1] == "1":  # right
                        uf.union(r * nc + c, r * nc + c + 1)
        print("ranks", uf.rank)
        return uf.getCount()


if __name__ == '__main__':
    print(Solution().numIslands([['1', '0', '1', '1'], ['1', '0', '0', '0'], ['1', '1', '1', '1']]))
