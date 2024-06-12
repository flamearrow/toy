from listNode import ListNode


def reverse(head):
    # return (head, tail)
    def doReverse(head):
        if not head:
            return (None, None)
        if not head.next:
            return (head, head)
        subHead, subTail = doReverse(head.next)
        head.next = None
        subTail.next = head
        return subHead, head

    return doReverse(head)[0]

# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.
# from, to is locations inclusive(starting from 1)

# x x B s A A A e X x   <- to reverse between s and e,  -note we only ahve reference to B, don't have access to s and e
#    1. reverse AAA, returns the reversedEnd
#    2. since sublist is reversed and linked to orignal s and e, we know two infos
#       * reversedStart = l.next
#       * end = revseredEnd.next
#    3. need to swap s and e in this step to keep the reversed order, so that it look like this
# x x B e A' A' A' s X x <- where A' is already reversed
#       * after(X) = end.next
#       * B.next=end
#       * end.next=reversedStart
#       * reversedEnd.next=start
#       * start.next=after(X)
# only edge case is
#    x s e x
# in this case, just swap s and e and set reversedStarted=start and reversedEnd=end


# the recursive call passes in a node BEFORE the actual reversing starting point, reverses the sublist and make sure the outer bound is still connected

def reverseLeftRight(head, left, right):
    dummy = ListNode(val=0, next=head)
    before = dummy
    for i in range(1, left):
        before = before.next

    # now before.next is poiting to the leftth item

    # reverse node between before+1 to before+right-left+1
    # return the tail for the list
    def doReverse(before, left, right):
        if left - right == 0:
            return before.next

        start = before.next  # starting from this node

        if right - left > 1:
            reversedEnd = doReverse(start, left + 1, right - 1)
            reversedStart = start.next
            end = reversedEnd.next
        else: # consecutive
            end = start.next
            reversedStart = start
            reversedEnd = end

        after = end.next

        before.next = end
        end.next = reversedStart

        reversedEnd.next = start
        start.next = after
        return start

    doReverse(before, left, right)
    return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.setNext(2).setNext(3).setNext(4).setNext(5)

    # reversed = reverse(head)
    # reversed.printFromSelf()
    reversed = reverseLeftRight(head, 2, 4)
    reversed.printFromSelf()
