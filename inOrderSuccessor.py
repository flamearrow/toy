# find in order successor of a bst
from treeNode.treeNode import TreeNode
from typing import Optional
class Solution:
    # use BST propertty to find the target number, whenever find something that's greater than target,
    # set it as successor candidate
    def inorderSuccessor(self, root: TreeNode, p: TreeNode):
        successor = None
        cur = root
        while cur:
            if p.val >= cur.val:  # go right, no successor found
                cur = cur.right
            else:  # found a successor candidate, go left
                successor = cur
                cur = cur.left

        return successor

    def inorderSuccessor2(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        ret = None

        cur = root

        while cur:
            if cur.val < p.val:
                cur = cur.right
            else:
                ret = cur
                cur = cur.left

        return cur


if __name__ == '__main__':
    # root = TreeNode(2)
    # root.set_left(1)
    # root.set_right(3)
    # Solution().inorderSuccessor2(root, TreeNode(1))
    l = [1,2,3]

