# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [2,3,0,1,4]
# Output: 2
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # index: minDistance
        buffer = {}

        def jumpDis(curIndex):
            if curIndex in buffer:
                return buffer[curIndex]
            if curIndex >= len(nums) - 1:
                return 0
            else:
                ret = -1
                for nextIndex in range(curIndex + 1, curIndex + 1 + nums[curIndex]):
                    newDistance = 1 + jumpDis(nextIndex)
                    if newDistance == 0:  # nextIndex returns -1, can't go anywhere
                        continue
                    if ret < 0:
                        ret = newDistance
                    else:
                        ret = min(ret, newDistance)
            buffer[curIndex] = ret
            return ret

        return jumpDis(0)

    def jumpDPNSqr(self, nums: List[int]) -> int:
        # dp[i] - min steps to jump to i
        dp = [None] * len(nums)
        dp[0] = 0

        for i in range(1, len(nums)):
            for startIndex in range(0, i):
                if startIndex + nums[startIndex] >= i:  # can make a jump from startIndex to i
                    if not dp[i]:
                        dp[i] = dp[startIndex] + 1
                    else:
                        dp[i] = min(dp[i], dp[startIndex] + 1)

        return dp[len(nums) - 1]

if __name__ == '__main__':
    print(Solution())