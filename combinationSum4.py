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
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # ret = 0
        # def search(curIndex, curValue):
        #     nonlocal ret
        #     if curValue > target:
        #         return
        #     elif curValue == target:
        #         ret += 1
        #         return
        #     else:
        #         for i in range(curIndex, len(nums)):
        #             search(curIndex, curValue + nums[i])
        # search(0, 0)

        # return ret
        dp = [0] * (target + 1)
        nums = sorted(nums)
        for num in nums:
            if num <= target:
                dp[num] = 1

        for i in range(nums[0], target + 1):
            for num in nums:
                if i - num >= 0 and dp[i - num] > 0:
                    dp[i] += dp[i - num]

        return dp[target]

