from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
#
# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
#
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
#
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
class Solution:

    # 1, the regular algorithm find the largest subarray
    # 2. use a reverse algorithm to find the smallest subarray, then use total sum minus it to get the largest prefix&suffix
    #       note if the samllest subarray == total sum, it means prefix+suffixSize == 0 -> this won't be a valid result
    # compare the resutl of 1 and 2 return the larger

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        curSum = nums[0]
        curMax = nums[0]
        curSumReverse = nums[0]
        curMin = nums[0]

        tSum = nums[0]

        for i in range(1, len(nums)):
            tSum += nums[i]
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            curMax = max(curMax, curSum)

            if curSumReverse > 0:
                curSumReverse = 0
            curSumReverse += nums[i]
            curMin = min(curMin, curSumReverse)
        if tSum == curMin:
            return curMax
        return max(curMax, tSum - curMin)


    # calculate maxPrefixSum[i] and maxSuffixSum[j] - for any i, see if mps[i]+mss[i+1] is larger than regular result within
    def maxSubarraySumCircularPrefixSufix(self, nums: List[int]) -> int:
        def regular(nums):
            if len(nums) == 0:
                return 0
            curSum = nums[0]
            ret = curSum
            for i in range(1, len(nums)):
                if curSum < 0:
                    curSum = 0
                curSum += nums[i]
                ret = max(ret, curSum)
            return ret

        # startting from 0 to i, the maxSum inclusive
        maxPrefixes = [0] * len(nums)

        # starting from i to tail, the maxSum inclusive
        maxSufixes = [0] * len(nums)

        curPreSum = nums[0]
        curPreMax = nums[0]
        maxPrefixes[0] = nums[0]
        for i in range(1, len(nums)):
            curPreSum += nums[i]
            maxPrefixes[i] = max(curPreSum, curPreMax)
            curPreMax = maxPrefixes[i]

        curSufSum = nums[-1]
        curSufMax = nums[-1]
        maxSufixes[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            curSufSum += nums[i]
            maxSufixes[i] = max(curSufSum, curSufMax)
            curSufMax = maxSufixes[i]

        ret = regular(nums)
        for i in range(0, len(nums) - 1):
            ret = max(ret, maxPrefixes[i] + maxSufixes[i + 1])

        return ret


if __name__ == '__main__':
    print(Solution().maxSubarraySumCircular([6, 9, -3]))