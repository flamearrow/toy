# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List, Optional
from listNode import ListNode
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        preHead = ListNode(val=0, next=head)
        pre = preHead
        cur = head
        while cur:
            seenDup = False
            while cur.next and cur.next.val == cur.val:
                seenDup = True
                cur = cur.next
            if not seenDup:
                pre.next = cur
                pre = cur
                cur = cur.next
            else:
                cur = cur.next
        pre.next = cur
        return preHead.next


if __name__ == '__main__':
    print(Solution())