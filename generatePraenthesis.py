from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        # at each step, decide what I can append to the end of the current path
        # it's either a ( or a )
        def search(cur, left, right):
            if len(cur) == 2 * n:
                print(" here", n)
                ret.append(cur)
                return
            if left > 0:
                search(cur + "(", left - 1, right)
            if right > left:
                search(cur + ")", left, right - 1)

        search("", n, n)

    # get sub problem, combine them with an additional ( or )
    def generateParenthesisSlower(self, n: int) -> List[str]:
        if n == 0:
            return ""
        elif n == 1:
            return ["()"]
        else:
            ret = []
            parens = self.generateParenthesis(n - 1)
            seen = set()
            for paren in parens:
                for i in range(len(paren) + 1):
                    addedLeft = paren[0:i] + "(" + paren[i:]
                    if addedLeft not in seen:
                        seen.add(addedLeft)
                        for j in range(i + 1, len(addedLeft) + 1):
                            addedBoth = addedLeft[0:j] + ")" + addedLeft[j:]
                            if addedBoth not in seen:
                                seen.add(addedBoth)

                                ret.append(addedBoth)
            return ret

if __name__ == '__main__':
    print(Solution())