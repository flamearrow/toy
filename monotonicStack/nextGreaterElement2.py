from typing import List
from collections import deque
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
#
# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
#
# Example 1:
#
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number.
# The second 1's next greater number needs to search circularly, which is also 2.
# Example 2:
#
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]


# Use a stack to save decreasing elelemnts and indices, if found num where stackTop < cur , [stackTop, cur] is a result
# note need to save the index of the value instead of the value iteself in stack, in case there are mutliple same values
# when there's a loop, do it twice, the next time don't append more value to the stack
def nextGreaterElements(nums: List[int]) -> List[int]:
    ret = [-1] * len(nums)
    numStack = deque()
    for index, num in enumerate(nums):
        while numStack and nums[numStack[-1]] < num:  # find a pair
            ret[numStack.pop()] = num
        numStack.append(index)

    for index, num in enumerate(nums):
        while numStack and nums[numStack[-1]] < num:  # find a pair
            ret[numStack.pop()] = num

    for index in numStack:
        ret[index] = -1
    return ret


if __name__ == '__main__':
    input = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
    # input = [1, 2, 1]
    print(nextGreaterElements(input))
