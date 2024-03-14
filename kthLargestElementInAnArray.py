# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?
#
# Example 1:
#
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
#
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import random
from typing import List
class Solution:
    def __init__(self):
        pass

    # note: when recurse with python, directly pass the sublist is simpler, don't mess with left/right
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def doFind(nums, k):
            pivot = random.choice(nums)
            left, right, mid = [], [], []  # mid could have more than one elements
            for item in nums:
                if item == pivot:
                    mid.append(item)
                elif item > pivot:
                    left.append(item)
                elif item < pivot:
                    right.append(item)

            # if there's 8 number smaller than pivot and we want to find the 8th smallest, we need to go left
            if len(left) >= k:
                return doFind(left, k)

            # if there's 8 + 3 numbers in left and mid, and we want to find the 12th, we need to go right, and find the
            #  first number in right, note k starts from 1
            if len(left) + len(mid) < k:
                return doFind(right, k - len(left) - len(mid))
            return pivot

        return doFind(nums, k)





if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))