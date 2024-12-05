from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque


class Solution:

    # l/r moving window - make sure r is always valid by a for range
    #  move left while r can't move over using a while loop
    #  note it's checking >= target, not == target
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        curSum = 0
        ret = float('inf')
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:  # move left bound
                ret = min(ret, r - l + 1)
                curSum -= nums[l]
                l += 1  # can't go over because by then curSum reaches 0
        return 0 if ret == float('inf') else ret


if __name__ == '__main__':
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
