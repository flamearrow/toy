from typing import List
from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        isPos = True
        # need a stack to save if we need reverse or not, each time a ( is encoutred, based on current op push t/f
        # e.g 1-(1-(1-(1+1)))
        #  the stack is [t, f, t]
        shouldReverse = deque()
        curNum = 0
        ret = 0

        def shouldR():
            if shouldReverse:
                return shouldReverse[-1]
            else:
                return False

        for index, c in enumerate(s):
            if c.isdigit():
                curNum = curNum * 10 + ord(c) - ord('0')
            # the termination point to accumulate to result:
            #  1. when encoutnred +- : add the previous val to result, update op
            #  2. when encoutred ): add the previous val to result,
            #  op will be updated later because +- must appear after )
            if c in "+-)" or index == len(s) - 1:
                if shouldR():
                    if isPos:
                        ret -= curNum
                    else:
                        ret += curNum
                else:
                    if isPos:
                        ret += curNum
                    else:
                        ret -= curNum
                if c == "+":
                    isPos = True
                elif c == "-":
                    isPos = False
                elif c == ")":
                    shouldReverse.pop()
                curNum = 0
            elif c == "(":
                if isPos:
                    if not shouldReverse:
                        shouldReverse.append(False)
                    else:
                        shouldReverse.append(shouldReverse[-1])
                else:
                    if not shouldReverse:
                        shouldReverse.append(True)
                    else:
                        shouldReverse.append(not shouldReverse[-1])
                isPos = True  # inside the bracket, always starts from pos
        return ret


if __name__ == '__main__':
    print(Solution().calculate("(1-(3-4))+1"))
    # print(Solution().calculate("1-(1-1)"))
