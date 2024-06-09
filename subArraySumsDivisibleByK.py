# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
#
# A subarray is a contiguous part of an array
#
# Example 1:
#
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:
#
# Input: nums = [5], k = 9
# Output: 0
from typing import List
class Solution:

    # if prefixSum[i]%k == prefixSum[j]%k, then prefixSum[j]-prefixSum[i] is also divided by k
    #  for each prefix sum, let its mod=X, see how many previous prefix sum has same mod, add taht to result
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # {mod: count}
        prefixWithModCount = {}
        curPrefixSum = 0
        ret = 0
        for num in nums:
            curPrefixSum += num
            modK = curPrefixSum % k
            if modK == 0: # the whole prefix can be an answer, add it
                ret += 1
            if modK in prefixWithModCount: # seen prefixeSums which %k = modK
                ret += prefixWithModCount[modK]
                prefixWithModCount[modK] += 1
            else:
                prefixWithModCount[modK] = 1
        return ret

if __name__ == '__main__':
    print(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5))

    # print(Solution().subarraysDivByK([5, 15, 25], 5))
