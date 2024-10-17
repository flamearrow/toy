from typing import Optional
from listNode import ListNode


# check if a linkedlist is a palindrom using recursion
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # currentHead will move within recursion
        currentHead = head

        # Check from curHead to its mirrored point, if it's a palindrome
        def doSolve(cur):
            nonlocal currentHead  # accessing cur outside the function, need to declare cur is nonLocal
            if cur is None:
                return True
            else:
                # the recursive call will keep moving cur to end
                # then compare cur with currentHead
                # then currentHead is moved forward, recursive stack pop, comparing currentHead with the pevious value
                res = doSolve(cur.next) and currentHead.val == cur.val
                currentHead = currentHead.next
                return res

        return doSolve(head)
