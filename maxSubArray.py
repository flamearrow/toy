# Given an integer array nums, find the
# subarray with the largest sum, and return its sum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur > 0 and curMax > 0:
                curSum += cur
                curMax = max(curSum, curMax)
            elif cur > 0 and curMax <= 0:
                curSum = cur
                curMax = max(curSum, curMax)
            else: # cur <= 0
                if curSum + cur > 0:
                    curSum += cur
                else:
                    curSum = 0
                    curMax = max(curMax, cur)

        return curMax