from typing import List

# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
#
# A good subarray is a subarray where:
#
# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
# Note that:
#
# A subarray is a contiguous part of the array.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # {mod: location}
        seenPrefixMods = {}
        curPrefixSum = 0
        for i, num in enumerate(nums):
            curPrefixSum += num
            modK = curPrefixSum % k
            if modK == 0 and i >= 1:
                return True
            if modK in seenPrefixMods:
                if i - seenPrefixMods[modK] > 1 and curPrefixSum >= modK:
                    return True
            else:
                seenPrefixMods[modK] = i
        return False



if __name__ == '__main__':
    print(Solution().checkSubarraySum([1, 0, 0], 2))