# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        maxWithI = [0] * size
        maxWithI[0] = nums[0]
        maxWithI[1] = nums[1]
        for i in range(2, len(nums)):
            for ending in range(0, i-2+1):
                maxWithI[i] = max(maxWithI[i], maxWithI[ending] + nums[i])

        return max(maxWithI[size-1], maxWithI[size-2])

    def robOn(self, nums: List[int]) -> int:
        dpW, dpWO = [0] * len(nums), [0] * len(nums)
        dpW[0] = nums[0]
        dpWO[0] = 0
        for i in range(1, len(nums)):
            dpW[i] = nums[i] + dpWO[i-1]
            dpWO[i] = max(dpW[i - 1], dpWO[i - 1])
        return max(dpW[len(nums) - 1], dpWO[len(nums) - 1])

    def robOnO1(self, nums: List[int]) -> int:
        prevW, prevWO = nums[0], 0

        for i in range(1, len(nums)):
            curW = prevWO + nums[i]
            curWO = max(prevW, prevWO)
            prevW, prevWO = curW, curWO

        return max(prevW, prevWO)