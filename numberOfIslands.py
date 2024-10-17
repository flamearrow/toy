# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
# all four edges of the grid are all surrounded by water

# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

from typing import List


# start by counting each 1 as an island
# use union find to attach adjacent 1s together, once a new one is added, minus one from total island

# union: group two nodes togehter by check their ancestor, if their acestors aren't equal,
# set one ancestor's parent to the other ancesotr to connect them
#    ancA = find(A)
#    ancB = find(B)
#    if ancA != ancB:
#       parent[ancB] = ancA # this makes sure B->ancB->ancA, which makes B's anc acnA, meaning it has same group with A
# find: keep looking for a nodes parent until there's no more parents - returns the 'ancestor'
#    can initialize a dict {node: parent} with nothing or with {node: node}
#    then update the dict on the go


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        parents = {}  # node: parent

        height = len(grid)
        width = len(grid[0])

        # 一开始每个一是一座孤岛
        totalCounts = sum(grid[i][j] == "1" for i in range(height) for j in range(width))
        print(totalCounts)

        def find(x):  # keep finding parents until reaches the topmost
            if x not in parents:
                return x
            else:
                return find(parents[x])

        def union(x, y):
            nonlocal totalCounts
            ancX = find(x)
            print(f"{x} anc is {ancX}")
            ancY = find(y)
            print(f"{y} anc is {ancY}")
            if ancX != ancY:
                parents[ancY] = ancX
                print(f"  now {y} anc is {ancX}")
                # connected two islands, remove a totoal island
                totalCounts -= 1
                print(f"  now totalCounts is {totalCounts}")

        def calIndex(i, j):
            return i * width + j

        for i in range(height):
            for j in range(width):
                # check if it's connected with right or below
                if grid[i][j] == "1":
                    if j + 1 < width and grid[i][j + 1] == "1":
                        union(calIndex(i, j), calIndex(i, j + 1))
                    if i + 1 < height and grid[i + 1][j] == "1":
                        union(calIndex(i, j), calIndex(i + 1, j))
        return totalCounts

    def numIslands2(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ancestors = [i for i in range(m * n)]  # [0, 1, 2, 3, 4, 5...]

        def find(i):
            if ancestors[i] != i:
                return find(ancestors[i])
            return i

        def union(y1, x1, y2, x2):
            anc1 = find(y1 * n + x1)
            anc2 = find(y2 * n + x2)
            if anc1 != anc2:
                ancestors[anc1] = anc2

        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1":
                    if y - 1 >= 0 and grid[y - 1][x] == "1":
                        union(y, x, y - 1, x)
                        # ancestor[y*n + x] = find(y-1, x)
                    if x - 1 >= 0 and grid[y][x - 1] == "1":
                        union(y, x, y, x - 1)

        # now count distinct ancestors
        distinctAnc = set()
        for i in range(m * n):
            y = i // n
            x = i % n
            if grid[y][x] == "1": # only count when the node is 1
                distinctAnc.add(find(i))

        return len(distinctAnc)


if __name__ == '__main__':
    input = [["1", "1", "1", "1", "1", "0", "1", "1", "1", "1"],
             ["1", "0", "1", "0", "1", "1", "1", "1", "1", "1"],
             ["0", "1", "1", "1", "0", "1", "1", "1", "1", "1"],
             ["1", "1", "0", "1", "1", "0", "0", "0", "0", "1"],
             ["1", "0", "1", "0", "1", "0", "0", "1", "0", "1"],
             ["1", "0", "0", "1", "1", "1", "0", "1", "0", "0"],
             ["0", "0", "1", "0", "0", "1", "1", "1", "1", "0"],
             ["1", "0", "1", "1", "1", "0", "0", "1", "1", "1"],
             ["1", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
             ["1", "0", "1", "1", "1", "1", "1", "1", "1", "0"]]

    # input = [
    #     ["1", "1", "0", "0", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "1", "0", "0"],
    #     ["0", "0", "0", "1", "1"]
    # ]
    print(Solution().numIslands(input))
