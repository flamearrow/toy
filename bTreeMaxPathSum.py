import sys
from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxPathSumBuffer = {}
        self.maxPathFromBuffer = {}

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root in self.maxPathSumBuffer:
            return self.maxPathSumBuffer[root]

        def maxPathFrom(node):
            if not node:
                return 0
            if node in self.maxPathFromBuffer:
                return self.maxPathFromBuffer[node]

            maxFromLeft = maxPathFrom(node.left)
            maxFromRight = maxPathFrom(node.right)
            ret = max(node.val, node.val + maxFromLeft, node.val + maxFromRight, 0)
            self.maxPathFromBuffer[node] = ret
            return ret

        maxPassingRoot = maxPathFrom(root.left) + root.val + maxPathFrom(root.right)

        ret = maxPassingRoot
        if root.left:
            ret = max(self.maxPathSum(root.left), maxPassingRoot)
        if root.right:
            ret = max(self.maxPathSum(root.right), ret)
        self.maxPathSumBuffer[root] = ret
        return ret

    def maxPathSum2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ret = [-sys.maxsize-1]

        # returns the max path sum starting from node(just one leg)
        # update the global result in between
        def search(node):
            if not node:
                return 0
            leftSum = search(node.left)
            rightSum = search(node.right)
            # leftSum/rightSum might be minus, just compare and get the largest
            ret[0] = max(ret[0], node.val, node.val+leftSum, node.val+rightSum, node.val+leftSum+rightSum)
            return max(node.val, leftSum+node.val, rightSum+node.val)

        search(root)

        return ret[0]


if __name__ == '__main__':
    root = TreeNode(1)
    root.set_right(-3).set_left(-2)
    left = TreeNode(-2)
    left.set_left(1).set_left(-1)
    left.set_right(3)
    root.left = left

    print(Solution().maxPathSum2(root))