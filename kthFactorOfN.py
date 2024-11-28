# You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
#
# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.


# Example 1:
#
# Input: n = 12, k = 3
# Output: 3
# Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
# Example 2:
#
# Input: n = 7, k = 2
# Output: 7
# Explanation: Factors list is [1, 7], the 2nd factor is 7.
# Example 3:
#
# Input: n = 4, k = 4
# Output: -1
# Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.

import math
class Solution:
    # instead of checking from 1-n, only need to check from 1-sqrt(n)
    # so time is O(sqrt(n))

    # 12's factors: 1, 2, 3, 4, 6, 12
    #  factors come in pairs(1, 12), (2, 6), (3, 4)
    #  so for i = [1, sqrt(12)) - i could be factor - n%i == 0
    #  then for i = [sqrt(12), 1] - n//i could be factor - n%(n//i) == 0
    def kthFactor(self, n: int, k: int) -> int:
        root = int(math.sqrt(n))
        if root * root == n:
            upper = root
        else:
            upper = root + 1
        for i in range(1, upper):
            print(f"checking {i}")
            if n % i == 0:
                k -= 1
            if k == 0:
                return i
        for i in range(int(root), 0, -1):
            candidate = n // i
            if n % candidate == 0:
                k -= 1
                if k == 0:
                    return n // i

        return -1