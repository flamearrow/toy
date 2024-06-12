# You are given the head of a linked list with n nodes.
#
# For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.
#
# Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.


from listNode import ListNode

from typing import List, Optional
from collections import  deque

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # use a stack to svave vaue and index in decreatsing order
        s = deque()  # stackOfDecreasingValues
        cur = head
        size = 0
        while cur:
            size += 1
            cur = cur.next
        ret = [None] * size
        cur = head
        index = 0
        while cur:
            if not s:
                s.append((cur.val, index))
            else:
                while s and s[-1][0] < cur.val:  # cur.val is the next larger value of the previous node
                    prevVal, prevIndex = s.pop()
                    ret[prevIndex] = cur.val
                s.append((cur.val, index))
            index += 1
            cur = cur.next
        # now all the indices in the stack doesn't have a value larger than it
        while s:
            nextVal, nextIndex = s.pop()
            ret[nextIndex] = 0

        return ret
