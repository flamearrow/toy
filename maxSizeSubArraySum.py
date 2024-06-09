# Given an integer array nums and an integer k, return the maximum length of a
# subarray
#  that sums to k. If there is not one, return 0 instead
#
# Example 1:
#
# Input: nums = [1,-1,5,-2,3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Example 2:
#
# Input: nums = [-2,-1,2,1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest

from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # {prefixSum: Index}
        sumIndex = {0: -1}
        curSum = 0
        ret = 0
        for index, num in enumerate(nums):
            curSum += num
            required = curSum - k
            if required in sumIndex:
                ret = max(ret, index-sumIndex[required])
            if curSum not in sumIndex: # only record the first/left most
                sumIndex[curSum] = index
        return ret
