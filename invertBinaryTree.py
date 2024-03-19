# Given the root of a binary tree, invert the tree, and return its root.
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:
#
# Input: root = []
# Output: []

from typing import List, Optional
from treeNode.treeNode import TreeNode
class Solution:
    def __init__(self):
        pass

    class Solution:
        def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return
            else:
                invertedLeft = self.invertTree(root.left)
                invertedRight = self.invertTree(root.right)
                root.left = invertedRight
                root.right = invertedLeft
                return root

if __name__ == '__main__':
    s = Solution()