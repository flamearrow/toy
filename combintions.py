from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []

        def search(left, right, cur):
            if len(cur) == k:
                print(" adding", cur)
                ret.append(cur[:])
                return
            for i in range(left, right + 1):
                cur.append(i)
                print(" now cur", cur)
                search(i + 1, right, cur)
                cur.pop()
            return

        search(1, n, [])
        return ret


if __name__ == '__main__':
    print(Solution().combine(4, 2))