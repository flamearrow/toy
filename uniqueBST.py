# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque


class Solution:
    def numTrees(self, n: int) -> int:
        buffer = {}

        # return # of trees built within [left, right]
        def numOfTrees(left, right):
            if (left, right) in buffer:
                return buffer[(left, right)]
            if left == right:
                return 1
            elif left > right:
                return 1
            ret = 0
            for root in range(left, right + 1):
                ret += numOfTrees(left, root - 1) * numOfTrees(root + 1, right)
            buffer[(left, right)] = ret
            return ret

        return numOfTrees(1, n)


if __name__ == '__main__':
    print(Solution())