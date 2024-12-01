from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def matchFrom(sI, pI):
            if sI == len(s) and pI == len(p):
                return True
            elif sI == len(s):
                if all(k == "*" for k in p[pI:]):
                    return True
                else:
                    return False
            elif pI == len(p):
                return False
            if p[pI] == s[sI] or p[pI] == "?":
                return matchFrom(sI + 1, pI + 1)
            elif p[pI] != "*" and p[pI] != s[sI]:
                return False
            else:  # p[pI] = '*'
                # skip consecutive *
                nextNonStartIndex = pI + 1
                while nextNonStartIndex < len(p) and p[nextNonStartIndex] == "*":
                    nextNonStartIndex += 1
                for sIndex in range(sI, len(s) + 1):
                    if matchFrom(sIndex, nextNonStartIndex):
                        return True
                return False

        return matchFrom(0, 0)


if __name__ == '__main__':
    print(Solution().isMatch("12", "1*******2*"))