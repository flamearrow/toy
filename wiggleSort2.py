# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# You may assume the input array always has a valid answer.
#
# Example 1:
#
# Input: nums = [1,5,1,1,6,4]
# Output: [1,6,1,5,1,4]
# Explanation: [1,4,1,5,1,6] is also accepted.
# Example 2:
#
# Input: nums = [1,3,2,2,3,1]
# Output: [2,3,1,3,1,2]

from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # cut the array into two groups, larger and smaller
        # assign them zigzagly
        # note: need to assign from end to start
        #  e.g: 4, 5, 5, 6: larger[5, 6], smaller[4, 5]
        #   assign 5, 6, 5, 4
        #    x if assign from start: 4, 5, 5, 6

        sortedNums = sorted(nums)
        smallerGroupSize = (len(nums) + 1) >> 1
        smallerPointer = smallerGroupSize - 1
        largerPointer = len(nums) - 1

        for i in range(len(nums)):
            if i % 2 == 0:  # pick from smaller group
                nums[i] = sortedNums[smallerPointer]
                smallerPointer -= 1
            else:
                nums[i] = sortedNums[largerPointer]
                largerPointer -= 1






if __name__ == '__main__':
    s = Solution()
    nums = [1,4,3,4,1,2,1,3,1,3,2,3,3]
    s.wiggleSort(nums)
    print(nums)