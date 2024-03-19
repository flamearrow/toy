# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself
#
# Example
# 1:
#
# Input: root = [1, 2, 3, null, null, 4, 5]
# Output: [1, 2, 3, null, null, 4, 5]
# Example
# 2:
#
# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from treeNode.treeNode import TreeNode
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret = []
        q = deque()
        q.append(root)
        while q:
            next = q.popleft()
            if next:
                ret.append(str(next.val))
                q.append(next.left)
                q.append(next.right)
            else:
                ret.append("null")

        return ", ".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        parents = deque()
        first = True
        isLeft = True
        ret = None
        tokens = data.split(", ")
        for token in tokens:
            if first:
                ret = TreeNode(int(token))
                first = False
                parents.append(ret)
            else:
                if isLeft:
                    nextParent = parents[0]  # not popping yet
                    if token != "null":
                        leftNode = nextParent.set_left(int(token))
                        parents.append(leftNode)
                    isLeft = False
                else:
                    nextParent = parents.popleft()
                    if token != "null":
                        rightNode = nextParent.set_right(int(token))
                        parents.append(rightNode)
                    isLeft = True
        return ret


if __name__ == '__main__':
    root = TreeNode(1)
    root.set_left(2)
    root.set_right(3).set_left(4)
    root.right.set_right(5)

    c = Codec()
    serialized = c.serialize(root)
    print(serialized)

    deserialized = c.deserialize(serialized)

    serialized2 = c.serialize(deserialized)
    print(serialized2)

