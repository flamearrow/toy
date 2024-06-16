# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#



from typing import List, Optional
from listNode import ListNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = [None]

        # returns from and below node, how many nodes are in p and q
        def search(node):
            if not node:
                return 0
            leftCount = search(node.left)
            rightCount = search(node.right)
            ret = 0
            if node == p or node == q:
                ret += 1
                if leftCount > 0 or rightCount > 0:  # node is LCA, and node is one of p or q
                    result[0] = node
            else:  # node is lca and node isnt' p or q
                if leftCount > 0 and rightCount > 0:
                    result[0] = node

            return ret + leftCount + rightCount

        search(root)

        return result[0]