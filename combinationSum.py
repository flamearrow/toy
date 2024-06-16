from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []

        def search(cur, candidateIndex):
            print("cur", cur)
            if sum(cur) == target:
                ret.append(cur[:])
                return
            if sum(cur) > target:
                return

            for i in range(candidateIndex, len(candidates)):
                cur.append(candidates[i])
                search(cur, i)
                cur.pop()
            return

        search([], 0)
        return ret


if __name__ == '__main__':
    print(Solution().combinationSum([2,3,6,7], 7))