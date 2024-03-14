# Given a sorted integer array nums and three integers a, b and c,
# apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and return the array in a sorted order.

# Example 1:
# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]
# Example 2:
#
# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]


from typing import List

class Solution:
    def __init__(self):
        pass

    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        newNums = list(map(lambda x: a*(x**2) + b*x + c, nums))
        newNums.sort()
        return newNums

if __name__ == '__main__':
    s = Solution()