# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
#
# The test cases are generated so that the answer can fit in a 32-bit integer.
#
# Example 1:
#
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:
#
# Input: nums = [9], target = 3
# Output: 0

from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        nums = sorted(nums) # can avoid sort and loop from 0
        for num in nums: # can avoid this and only set dp[0] to 1
            if num <= target:
                dp[num] = 1

        for i in range(nums[0], target + 1):
            for num in nums:
                if i - num >= 0 and dp[i - num] > 0:
                    dp[i] += dp[i - num]

        return dp[target]


    def combinationSum4Another(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(0, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]

