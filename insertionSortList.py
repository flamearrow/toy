# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
#
# The steps of the insertion sort algorithm:
#
# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy header
        # don't do it in place, create one list from scratch
        dummy = ListNode()
        curr = head
        while curr:
            prev = dummy # always start from the -1 position
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next

            # now prev.next val > curr.val, insert in between
            # or now prev.next is null, then add curr as the last one
            next = curr.next

            curr.next = prev.next
            prev.next = curr

            curr = next

        return dummy.next






if __name__ == '__main__':
    s = Solution()