# You
# are
# given
# an
# integer
# num.You
# can
# swap
# two
# digits
# at
# most
# once
# to
# get
# the
# maximum
# valued
# number.
#
# Return
# the
# maximum
# valued
# number
# you
# can
# get.
#
# Example
# 1:
#
# Input: num = 2736
# Output: 7236
# Explanation: Swap
# the
# number
# 2 and the
# number
# 7.
# Example
# 2:
#
# Input: num = 9973
# Output: 9973
# Explanation: No
# swap.


from typing import List


class Solution:
    def maximumSwap(self, num: int) -> int:
        numArr = [int(d) for d in str(num)]
        # 5510 will create map {0: 3, 1: 2, 5: 1}
        lastDigitIndex = {digit: index for index, digit in enumerate(numArr)}
        for currentIndex, d  in enumerate(numArr):
            # if I find there's a digit greater than d in the right, then I swap it with d and get a large number
            # search from 9
            for largerDigit in range(9, d, -1):
                if largerDigit in lastDigitIndex and lastDigitIndex[largerDigit] > currentIndex:
                    rightIndex = lastDigitIndex[largerDigit]
                    numArr[currentIndex], numArr[rightIndex] = numArr[rightIndex], numArr[currentIndex]
                    return int("".join(map(lambda x: str(x), numArr)))

        return num


if __name__ == '__main__':
    print(Solution().maximumSwap(98368))