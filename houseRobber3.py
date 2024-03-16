# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
#
# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.
#
# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police

# Example 1:
#
#
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

# Example 2:
#
#
# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.a


from typing import List, Optional
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def set_left(self, left_value=None):
        self.left = TreeNode(val=left_value)
        return self.left

    def set_right(self, right_value=None):
        self.right = TreeNode(val=right_value)
        return self.right
class Solution:
    def __init__(self):
        pass
    def rob(self, root: Optional[TreeNode]) -> int:
        # return a tuple: (max with root, max without root)
        def calculateMax(node):
            if not node:
                return 0, 0
            (maxWithLeft, maxWithoutLeft) = calculateMax(node.left)
            (maxWithRight, maxWithoutRight) = calculateMax(node.right)
            # with root - have to use maxWithotuLeft and maxWithotuRight
            maxWithRoot = maxWithoutLeft + maxWithoutRight + node.val
            # without root - can choose whether to use with/without left or right, chose the larger one
            #  if maxWithotuLeft is larger, it means both root and left are skipped
            maxWithoutRoot = max(maxWithLeft, maxWithoutLeft) + max(maxWithRight, maxWithoutRight)
            return maxWithRoot, maxWithoutRoot

        (maxWithRoot, maxWithoutRoot) = calculateMax(root)
        print(maxWithRoot, maxWithoutRoot)
        return max(maxWithRoot, maxWithoutRoot)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(4)
    root.set_left(1).set_left(2).set_left(3)
    print(s.rob(root))
