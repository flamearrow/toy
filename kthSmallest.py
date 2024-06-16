from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
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


if __name__ == '__main__':
    print(Solution())