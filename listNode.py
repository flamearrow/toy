class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def setNext(self, val):
        self.next = ListNode(val)
        return self.next

    def printFromSelf(self):
        print("{} ".format(self.val), end=" ")
        if self.next:
            self.next.printFromSelf()