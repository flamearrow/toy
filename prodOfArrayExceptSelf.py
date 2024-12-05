from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefixProduct = [1] * l
        suffixProduct = [1] * l

        prefixProduct[0] = nums[0]
        for i in range(1, l):
            prefixProduct[i] = nums[i] * prefixProduct[i - 1]

        suffixProduct[l - 1] = nums[l - 1]
        for i in range(l - 2, -1, -1):
            suffixProduct[i] = nums[i] * suffixProduct[i + 1]

        ret = []
        for i in range(l):
            if i == 0:
                ret.append(suffixProduct[i + 1])
            elif i == l - 1:
                ret.append(prefixProduct[i - 1])
            else:
                ret.append(prefixProduct[i - 1] * suffixProduct[i + 1])

        return ret


if __name__ == '__main__':
    print(Solution())