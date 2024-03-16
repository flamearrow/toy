# # You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# #
# # Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
#
# Example 1:
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:
#
# Input: nums = [1,2,3]
# Output: 3

from typing import List

class Solution:
    def __init__(self):
        pass

    # either rob [0:n-1] or rob[1:n], get the larger of the two
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        return max(self.robSub(nums[1:]), self.robSub(nums[:-1]))


    def robSub(self, nums: List[int]) -> int:
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


if __name__ == '__main__':
    s = Solution()