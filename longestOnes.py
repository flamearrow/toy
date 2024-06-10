# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0'
#
# Example 1:
#
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:
#
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


# sliding window
from typing import List
def longestOnes(self, nums: List[int], k: int) -> int:
    kLeft = k
    start = 0
    end = 0
    ret = 0
    for index, num in enumerate(nums):
        # if index == 10:
        #     print("  kLeft", kLeft)
        if num == 1:
            ret = max(index - start + 1, ret)
        else:
            if kLeft > 0:
                ret = max(index - start + 1, ret)
                kLeft -= 1
            else:  # need to move start until it pass the first 0
                while nums[start] == 1:
                    start += 1
                # now nums[start] == 0, move 1 further
                start += 1
                end += 1
                ret = max(index - start + 1, ret)
    return ret