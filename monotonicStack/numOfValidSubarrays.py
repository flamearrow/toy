from typing import List
from collections import deque

# Given an integer array nums, return the number of non-empty subarrays with the leftmost element of the subarray not larger than other elements in the subarray.
#
# A subarray is a contiguous part of an array
#
# Example 1:
#
# Input: nums = [1,4,2,5,3]
# Output: 11
# Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
# Example 2:
#
# Input: nums = [3,2,1]
# Output: 3
# Explanation: The 3 valid subarrays are: [3],[2],[1].
# Example 3:
#
# Input: nums = [2,2,2]
# Output: 6
# Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        # stack to save (index, value), the value are sorted from small to large
        s = deque()
        ret = 0
        for index, value in enumerate(nums):
            # keep the stack sorted on values, each time a previous node is popped, add the distance to result.
            # e.g previous node is (3, 10) and current node is (5, 8)
            #  it means we find a sub array from [3, 5) where all values are greator than 10
            #   the add 2 to result with [3] and [3, 4]
            while s and s[-1][1] > value:
                prevIndex, prevValue = s.pop()
                ret += index - prevIndex
            s.append((index, value))

        while s:
            prevIndex, prevValue = s.pop()
            ret += len(nums) - prevIndex

        return ret

if __name__ == '__main__':
    print(Solution())