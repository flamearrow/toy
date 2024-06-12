# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.
#
# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
#
# Example
# 1:
#
# Input: n = 12
# Output: 21
# Example
# 2:
#
# Input: n = 21
# Output: -1

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        intArray = [int(x) for x in str(n)]

        digitToBorrow = len(intArray) - 2

        while digitToBorrow >= 0 and intArray[digitToBorrow] >= intArray[digitToBorrow + 1]:
            digitToBorrow -= 1

        if digitToBorrow < 0:
            return -1

        digit = intArray[digitToBorrow]

        digitToSwap = len(intArray) - 1
        while intArray[digitToSwap] <= digit:
            digitToSwap -= 1

        intArray[digitToBorrow], intArray[digitToSwap] = intArray[digitToSwap], intArray[digitToBorrow]

        left = digitToBorrow + 1
        right = len(intArray) - 1
        while left < right:
            intArray[left], intArray[right] = intArray[right], intArray[left]
            left += 1
            right -= 1

        ret = int("".join([str(i) for i in intArray]))

        if ret.bit_length() >= 32:
            return -1
        else:
            return ret