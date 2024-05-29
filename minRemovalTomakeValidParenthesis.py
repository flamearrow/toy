# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
# Example 1:
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.

from typing import List
from collections import deque

class Solution:
    def __init__(self):
        pass


    # use a stack to save (, pop when seeing a right
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        to_remove = set()
        for index, c in enumerate(s):
            if c == "(":
                stack.append(index)
            elif c == ")":
                if stack:
                    stack.pop() # a pair
                else: # extra ) - remove
                    to_remove.add(index)
        for i in stack:
            to_remove.add(i)

        result = ""
        for index, c in enumerate(s):
            if index not in to_remove:
                result += c
        return result

if __name__ == '__main__':
    print(Solution())