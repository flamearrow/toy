from treeNode.treeNode import TreeNode

from typing import List, Optional


# Given the root of a binary tree, return the vertical order traversal of its nodes' values.
# (i.e., from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right


from collections import deque
class Solution:
    def __init__(self):
        pass


    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvlNodeDict = {}  # lvl, nodes

        q = deque()
        q.append((root, 0))

        while q:
            nextNode, lvl = q.popleft()
            nodesAtLvl = lvlNodeDict.setdefault(lvl, [])
            nodesAtLvl.append(nextNode.val)
            if nextNode.left:
                q.append((nextNode.left, lvl-1))
            if nextNode.right:
                q.append((nextNode.right, lvl+1))

        return list(map(lambda x: x[1], sorted(lvlNodeDict.items(), key=lambda x: x[0])))


if __name__ == '__main__':
    root = TreeNode(3)
    root.set_left(9).set_left(1)
    root.left.set_right(0)
    root.set_right(8).set_left(1)
    print(Solution().verticalOrder(root))
