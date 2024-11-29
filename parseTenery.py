# Given a string expression representing arbitrarily nested ternary expressions, evaluate the expression, and return the result of it.
#
# You can always assume that the given expression is valid and only contains digits, '?', ':', 'T', and 'F' where 'T' is true and 'F' is false. All the numbers in the expression are one-digit numbers (i.e., in the range [0, 9]).
#
# The conditional expressions group right-to-left (as usual in most languages), and the result of the expression will always evaluate to either a digit, 'T' or 'F'.
#


# Example 1:
#
# Input: expression = "T?2:3"
# Output: "2"
# Explanation: If true, then result is 2; otherwise result is 3.
# Example 2:
#
# Input: expression = "F?1:T?4:5"
# Output: "4"
# Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
# "(F ? 1 : (T ? 4 : 5))" --> "(F ? 1 : 4)" --> "4"
# or "(F ? 1 : (T ? 4 : 5))" --> "(T ? 4 : 5)" --> "4"
# Example 3:
#
# Input: expression = "T?T?F:5:3"
# Output: "F"
# Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
# "(T ? (T ? F : 5) : 3)" --> "(T ? F : 3)" --> "F"
# "(T ? (T ? F : 5) : 3)" --> "(T ? F : 5)" --> "F"


from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque

class Solution:
    # key observation is to look from right to left, then this becomes a postFix notation problem with stack
    #  falseValue, True, T/F
    # Reverse polish notation AKA postfix notation - use stack
    # infix: 3-2
    # prefix: -32
    # postfix: 32-
    def parseTernary(self, expression: str) -> str:
        def calExp(exp):  # A?B:C
            if exp[0] == "T":
                return exp[2]
            else:
                return exp[4]

        while len(expression) >= 5:
            # find the adjacent ? and :
            lastQIndex = -1
            cur = 0
            while cur < len(expression):
                if expression[cur] == ":":
                    # the condition of a atomic exp:
                    # 1: no expression should appear after :, only a direct value
                    # 2: no expression should appear before :, only a direct value, meaning lastQIndex and cur is only 2 apart

                    # or a slightly faster way:
                    # start from right to left, find the first ?: pair, that one will be the valid one
                    if (cur == len(expression) - 2 or expression[cur + 2] != "?") and lastQIndex == cur - 2:
                        break
                elif expression[cur] == "?":
                    lastQIndex = cur
                cur += 1

            # lastQIndex points to ?
            # cur poitns to :
            subExpressionLeft = lastQIndex - 1
            subExpressionRight = cur + 2
            val = calExp(expression[subExpressionLeft:subExpressionRight])
            expression = expression[:subExpressionLeft] + val + expression[subExpressionRight:]

        return expression

    # similar as evaluation a reverse polish notation
    def parseTernaryWithAStack(self, expression: str) -> str:
        # from right to left, using a stack, can ignore :
        stack = deque()
        cur = len(expression) - 1
        while cur > 0:
            curC = expression[cur]
            if curC == "?":
                tValue = stack.pop()
                fValue = stack.pop()
                operator = expression[cur - 1]
                if operator == "T":
                    stack.append(tValue)
                else:
                    stack.append(fValue)
                cur -= 2
            elif curC != ":":  # digits or TF
                stack.append(curC)
                cur -= 1
            else:  # skip :
                cur -= 1
        return stack[0]

if __name__ == '__main__':
    print(Solution())