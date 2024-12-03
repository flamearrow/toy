# Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /). For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.
#
# When writing such an expression, we adhere to the following conventions:
#
# The division operator (/) returns rational numbers.
# There are no parentheses placed anywhere.
# We use the usual order of operations: multiplication and division happen before addition and subtraction.
# It is not allowed to use the unary negation operator (-). For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.
# We would like to write an expression with the least number of operators such that the expression equals the given target. Return the least number of operators used.
#
# Example
# 1:
#
# Input: x = 3, target = 19
# Output: 5
# Explanation: 3 * 3 + 3 * 3 + 3 / 3.
# The
# expression
# contains
# 5
# operations.
# Example
# 2:
#
# Input: x = 5, target = 501
# Output: 8
# Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.
# The
# expression
# contains
# 8
# operations.
# Example
# 3:
#
# Input: x = 100, target = 100000000
# Output: 3
# Explanation: 100 * 100 * 100 * 100.
# The
# expression
# contains
# 3
# operations.
from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque

class Solution:
    def __init__(self):
        pass

    # stupidly bfs, cheat with eval()
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        q = deque()
        q.append(str(x))
        while q:
            nextExp = q.popleft()
            nextVal = eval(nextExp)
            if nextVal == target:
                return len(nextExp.split(f"{x}")) - 2
            else:
                q.append(f"{nextExp}+{x}")
                q.append(f"{nextExp}-{x}")
                q.append(f"{nextExp}*{x}")
                q.append(f"{nextExp}/{x}")

        # not reachable
        return -1

    # try to reach target greedly by using as many * as poosible
    #  then for the prod that's barely over target, look for subproblems solution
    #    (prod-target) and (target-prod//x)
    #  select the smaller.
    # Note only look (prod-target) when prod-target>target aka prod>2 *target, otherwise we'll look for a larget target
    # Note there's two cases when X > target, both involinving building 1s and add up to target
    def leastOpsExpressTargetDfs(self, x: int, target: int) -> int:
        buffer = {}
        def dfs(target):
            if target == x:
                return 0
            if x > target:
                # case1 : x/x + x/x +... add target times, need target "/" and (target-1) "+"
                # case2: x- x/x - x/x -... subtract (x-target) times, need (x-target) "-" and (x-target) "/"
                return min(2*target-1, 2*(x-target))
            if target in buffer:
                return buffer[target]

            cur = x
            count = 0
            while cur < target:
                cur = cur * x
                count += 1
            # now cur >= target

            # counts of one less * and one more +
            # target = cur // x + X, where X is sub problem
            # no need to plus one because remoed a "*" and added a "+"
            ret = dfs(target - cur // x) + count

            # counts of same * and one more -
            # target = cur - X where X is sub problem
            # need to plus one because added a "-"
            #  only continue search if cur - target < target, otherwise we're seraching a larger target
            #  and will cause infinite loop
            if cur < 2 * target:
                ret = min(ret, dfs(cur - target) + count + 1)
            buffer[target] = ret
            # NOTE: incorrect to greedily search the smaller abs btn (target, and cur),
            #  as the oprations is not necessarily smaller, need to compare both
            return ret

        return dfs(target)


if __name__ == '__main__':
    print(Solution())