# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
#
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.


from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque
class Solution:

    # use a stack, making sure numbers are always going up
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()
        for digit in num:
            if k == 0:
                stack.append(digit)
            else:
                if not stack:
                    stack.append(digit)
                else:
                    digitV = int(digit)
                    if int(stack[-1]) <= digitV:
                        stack.append(digit)
                    else:
                        # keep popping while there's still elements and while k is not 0
                        while k > 0 and stack and int(stack[-1]) > digitV:
                            stack.pop()
                            k -= 1
                        stack.append(digit)
        ret = "".join(stack)
        if k > 0: # now ret is non decreasing, cut the last k
            ret = ret[0:len(ret)-k]
        if not ret:
            return "0"
        while len(ret) > 1 and ret.startswith("0"):
            ret = ret[1:]
        return ret

    # use stack use stack use stack
    def removeKdigitsTake2(self, num: str, k: int) -> str:
        s = deque()

        for c in num:
            if k == 0:
                s.append(c)
            elif not s:
                s.append(c)
            else:
                while s and c < s[-1] and k > 0:
                    s.pop()
                    k -= 1
                s.append(c)

        # now s is non decreasing, remove tail if k>0
        rst = "".join(s)[0:len(s) - k]
        if not rst:
            return "0"
        else:
            cur = 0
            while cur < len(rst) and rst[cur] == "0":
                cur += 1
            if cur == len(rst):
                return "0"
            else:
                return rst[cur:]




    # find the peak when going up or down, remove it one by one
    def removeKdigitsPeak(self, num: str, k: int) -> str:
        def removeOne(num):
            if len(num) == 1:
                return "0"
            else:
                cur, n = 0, 1
                while n < len(num) and num[cur] == num[n]:
                    cur += 1
                    n += 1
                if n == len(num): # all equal, could be 000000
                    return num[1:]
                else:
                    if num[cur] < num[n]: # going up, find the peak
                        while n < len(num) and num[cur] <= num[n]:
                            cur += 1
                            n += 1
                        # now cur is peak
                        ret = num[0:cur] + num[cur+1:]
                    else: # going down, remove head, cur is head
                        ret = num[0:cur] + num[cur+1:]
                    zeroP = 0
                    while zeroP < len(ret) and ret[zeroP] == "0":
                        zeroP += 1
                    if zeroP == len(ret):
                        return "0"
                    else:
                        return ret[zeroP:]

        for i in range(k):
            num = removeOne(num)
        return num

if __name__ == '__main__':
    print(Solution())