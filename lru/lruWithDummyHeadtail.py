from typing import List, Optional
from listNode import ListNode

class BiNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def setNext(self, nextNode):
        self.next = nextNode

    def setPrev(self, prevNode):
        self.prev = prevNode

class LRUCache:

    def __init__(self, capacity: int):
        self.head = BiNode(0, 0)
        self.tail = BiNode(0, 0)
        self.head.setNext(self.tail)
        self.tail.setPrev(self.head)
        # {val: node}
        self.nodes = {}
        self.capacity = capacity

    def remove(self, n):
        prevNode = n.prev
        nextNode = n.next
        prevNode.next = nextNode
        nextNode.prev = prevNode


    def addTohead(self, n):
        prevHead = self.head.next
        self.head.setNext(n)
        n.setPrev(self.head)
        prevHead.setPrev(n)
        n.setNext(prevHead)

    def get(self, key: int) -> int:
        if key in self.nodes:
            retNode  = self.nodes[key]
            self.remove(retNode)
            self.addTohead(retNode) # add to top
            return retNode.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            oldNode = self.nodes[key]
            self.remove(oldNode)
            newNode = BiNode(key, value)
            self.nodes[key] = newNode
            self.addTohead(newNode)
        else:
            newNode = BiNode(key, value)
            self.nodes[key] = newNode
            self.addTohead(newNode)
            if len(self.nodes) > self.capacity:
                nodeToEvict = self.tail.prev
                del self.nodes[nodeToEvict.key]
                print("  evicting", nodeToEvict.val)
                self.remove(nodeToEvict)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)