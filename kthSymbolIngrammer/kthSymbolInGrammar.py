# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
#
# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

# Example 1:
#
# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0
# Example 2:
#
# Input: n = 2, k = 1
# Output: 0

# Explanation:
# row 1: 0
# row 2: 01
# Example 3:
#
# Input: n = 2, k = 2
# Output: 1
# Explanation:
# row 1: 0
# row 2: 01
# Constraints:
#
# 1 <= n <= 30
# 1 <= k <= 2n - 1
import math
from math import pow
class Solution:

    def kthGrammar(self, n: int, k: int) -> int :
        # return int(self.row(n)[k-1])
        return int(self.dfs(n, k, 0))

    # thinks it as a binary tree, looking at level n, there's 2**(n-1) nodes, we need to know what value that node is
    # search from binary tree deep first, by passing the level n, index k and rootValue(0 or 1)
    # if n reaches 1, then we find the node at rootValue
    # otherwise try to go to next level by
    #   determin should go left or right by comparing # of nodes at lvl and k
    #    go left half or right half accodingly, when going right, remember to update k to (k-nodesAtLvl/2)
    def dfs(self, n, k, root):
        if n == 1:
            return root

        totalNodesAtLvlN = 2 ** (n-1)
        # note: totalNodesAtLvlN / 2 is a integer, k starts from 1, so use <=
        # e.g  if k=16 and totalNodesAtLvlN = 32, need to go left sub tree
        if k <= totalNodesAtLvlN / 2:  # go left
            nextRoot = 0 if root == 0 else 1
            return self.dfs(n-1, k, nextRoot)
        else:  # go right, skip left tree by (k-totalNodesAtLvlN/2)
            nextRoot = 1 if root == 0 else 0
            return self.dfs(n-1, k - totalNodesAtLvlN / 2, nextRoot)

    def row(self, n):
        if n == 1:
            return "0"
        else:
            ret = ""
            for i in self.row(n-1):
                ret += "01" if i == "0" else "10"
            return ret

if __name__ == '__main__':
    s = Solution()
    print(s.kthGrammar(2, 2))
