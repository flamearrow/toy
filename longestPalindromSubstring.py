from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode


# Given a string s, return the longest palindromic substring in s
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        # checking from [0, 2], [1, 3] .... because [0, 1] and [1, 2] ... already populated
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i : j + 1]

    def longestPalindrome2(self, s: str) -> str:
        l = len(s)
        dp = [[False]*l for _ in range(l)]
        ret = ""
        for i in range(l): # self and consecutive two are palindromes
            dp[i][i] = True
            ret = s[i]
        for i in range(l-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ret = s[i:i+2]

        # calculate dp[0][l-1], need to calcualte dp[1][l-2]
        # start filling dp with reverse diagnals
        #  dp[0][2], dp[1][3]...
        #  dp[0][3], dp[2][4]...
        for diff in range(2, l):
            # make sure the last right bound x: (start + diff == l-1),  start=l-diff-1
            for start in range(l-diff):
                left, right = start, start+diff
                if dp[left+1][right-1] and s[left] == s[right]:
                    dp[left][right] = True
                    ret = s[left:right+1]

        return ret


if __name__ == '__main__':
    print(Solution().longestPalindrome2("cbbd"))