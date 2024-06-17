from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
# Given an integer n, return the number of trailing zeroes in n!.
#
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 1. easy way: for each N inclusive, find hwo many 5s it can be divided, each 5(along with 2 appears before it) would contribute to a 0
        # fiveCount = 0
        # for i in range(5, n+1, 5):
        #     while i % 5 == 0:
        #         i = i / 5
        #         fiveCount += 1
        # return fiveCount


        # 2. smart way: count multiples of five from n directly
        fiveCount = 0
        curPow = 5
        while n >= curPow:
            fiveCount += n//curPow
            curPow *= 5
        return fiveCount

if __name__ == '__main__':
    print(Solution())