# 1658. Minimum Operations to Reduce X to Zero
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
#
# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
# Example 1:
#
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:
#
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:
#
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        totalSum = sum(nums)
        # actually looking for the longest subarray whose sum is sum(nums)-X
        targetSum = totalSum - x
        if targetSum == 0:
            return len(nums)
        # {prefixSum: index}
        sumIndex = {0: -1}
        curSum = 0
        maxLength = -1
        targetLeft = -1
        targetRight = -1
        for index, num in enumerate(nums):
            curSum += num
            required = curSum - targetSum
            if required in sumIndex:
                if maxLength < index - sumIndex[required]:
                    maxLength = index - sumIndex[required]
                    targetLeft = sumIndex[required]
                    targetRight = index
            if curSum not in sumIndex:
                sumIndex[curSum] = index
        print(sumIndex)
        if maxLength == -1:
            return -1
        else:
            return len(nums) - targetRight + targetLeft
