from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [1]

        def search(root):
            if root:
                ret = search(root.left)
                if ret:
                    return ret
                if count[0] == k:
                    print(" returning", root.val)
                    return root.val
                count[0] += 1
                return search(root.right)
            return None

        return search(root)

    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            k -= 1
            print(cur.val)
            if not k:
                return cur.val
            cur = cur.right
        return -1

    def inOrderTraversal(self, root):
        stack = deque()
        cur = root
        while cur or stack: # termination: cur or stack null
            # each time push all the left most nodes into stack
            while cur:
                stack.append(cur)
                cur = cur.left
            # then get the last left
            cur = stack.pop()
            print(cur.val)
            # then start to searching from last left's right - could be empty
            cur = cur.right


if __name__ == '__main__':
    root = TreeNode(1)
    root.set_left(2).set_right(4).set_left(5)
    root.set_right(3)
    # Solution().kthSmallest2(root, 3)

    Solution().inOrderTraversal(root)