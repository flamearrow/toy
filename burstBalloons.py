# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
#
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
#
# Return the maximum coins you can collect by bursting the balloons wisely.
#
# Example 1:
#
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# Example 2:
#
# Input: nums = [1,5]
# Output: 10

from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque


class Solution:
    # two tricks
    # 1. append/prepent the value with [1]
    # 2: within that range, try all possible values that bursted last
    #   sub problem becomes lastBusted*v[left-1]*v[right+1] + subProblem(left, i-1), subProblem(i+1, right)
    # add some buffers
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        cache = {}

        # calculate the best value from left to right
        def search(left, right):  # both inclusive
            if (left, right) in cache:
                return cache[(left, right)]
            if left > right:
                return 0
            ret = 0
            for i in range(left, right + 1):
                # calculate the contributor if nums[i] is bursted LAST within range [left, right]
                pivotValue = nums[left - 1] * nums[i] * nums[right + 1]
                leftSum = search(left, i - 1)
                rightSum = search(i + 1, right)
                ret = max(ret, pivotValue + leftSum + rightSum)
            cache[(left, right)] = ret
            return ret

        return search(1, len(nums) - 2)


if __name__ == '__main__':
    print(Solution().maxCoins([3, 1, 5, 8]))
