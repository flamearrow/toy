from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode

class Solution:
    # traditional edit distance DP
    def isOneEditDistance(self, s: str, t: str) -> bool:
        width = len(s)+1
        height = len(t)+1
        dp = [[0] * width for _ in range(height)]

        for y in range(height):
            dp[y][0] = y
        for x in range(width):
            dp[0][x] = x

        for y in range(1, height):  # t
            for x in range(1, width):  # s
                candidates = []
                candidates.append(dp[y][x-1]+1)
                candidates.append(dp[y-1][x]+1)
                if t[y-1] == s[x-1]:
                    candidates.append(dp[y-1][x-1])
                else:
                    candidates.append(dp[y-1][x-1] + 1)
                dp[y][x] = min(candidates)
        return dp[-1][-1] == 1

    # one pass
    def isOneEditDistanceOnePass(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        def doCheck(longer, shorter):
            pLonger, pShorter = 0, 0
            while pShorter < len(shorter):
                if longer[pLonger] == shorter[pShorter]:
                    pLonger += 1
                    pShorter += 1
                else:
                    # remove one from longer
                    if longer[pLonger+1:] == shorter[pShorter:]:
                        return True
                    # skip one in both longer and shorter aka replace
                    elif longer[pLonger+1:] == shorter[pShorter+1:]:
                        return True
                    else:
                        return False
            return pLonger < len(longer) # if Ture, longer is one char longer, otherwise, equal
        if len(s) >= len(t):
            return doCheck(s, t)
        else:
            return doCheck(t, s)


if __name__ == '__main__':
    print(Solution().isOneEditDistanceOnePass("teacherly", "teacher"))
