# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may be changed

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from listNode import ListNode

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyHead = ListNode(0, next=head)

        # reverse nextK nodes and return the tail
        def reverseNextK(prehead, k):  # returns the last of group of k, or None if there's no k
            if not prehead:
                return None
            head = prehead.next  # haed is going to be the new tail
            if k == 1:
                return head
            else:
                subTail = reverseNextK(head, k - 1)  # don't have long enough K, return none
                if not subTail:
                    return None
                subhead = head.next
                prehead.next = subhead
                head.next = subTail.next
                subTail.next = head
                return head

        cur = dummyHead
        while cur:
            cur = reverseNextK(cur, k)

        return dummyHead.next

