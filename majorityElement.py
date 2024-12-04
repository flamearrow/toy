# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
#
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from typing import List
class Solution:

    # Boyer-Moore Voting Algorithm
    #  use a count to keep track the majority
    #  when seeing a hit, increment count, otherwise decrement
    #  when count reaches 0, replace candidate
    # need to verify canddiateis indeed majority later
    def majorityElement(self, nums: List[int]) -> int:
        cur = -1
        curCount = 0
        for i in range(len(nums)):
            if curCount == 0:
                cur = nums[i]
            if nums[i] == cur:
                curCount += 1
            else:
                curCount -= 1

        # now cur might be a candidate
        realCurCount = sum([i == cur for i in nums])
        if realCurCount >= (len(nums) // 2):
            return cur
        else:
            return -1  # not possible
