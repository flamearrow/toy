# Given the root of a complete binary tree, return the number of the nodes in the tree.
#
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Design an algorithm that runs in less than O(n) time complexity
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:
#
# Input: root = []
# Output: 0
# Example 3:
#
# Input: root = [1]
# Output: 1

from typing import List, Optional
from treeNode.treeNode import TreeNode

class Solution:
    def __init__(self):
        pass

    def countNodes(self, root: TreeNode) -> int:
        def depth(node):
            d = 0
            while node:
                node = node.left
                d += 1
            return d

        if not root:
            return 0
        leftD = depth(root.left)
        rightD = depth(root.right)
        if leftD == rightD:  # left is a full tree
            return (1 << leftD) + self.countNodes(root.right)  # shift has lower priority than plus, need bracket
        else: # right is a full tree, shorter than left
            return (1 << rightD) + self.countNodes(root.left)


if __name__ == '__main__':
    root = TreeNode(1)
    root.set_left(2).set_left(4)
    root.set_right(3).set_left(6)
    root.left.set_right(5)



    s = Solution()
    print(s.countNodes(root))