# 146. LRU Cache
# Solved
# Medium
# Topics
# Companies
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4


# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.


import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dict:
            ret = self.dict[key]
            self.dict.move_to_end(key)
            return ret
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key].value = value
            self.dict.move_to_end(key)
        else:
            self.dict[key] = value
            # evict
            if len(self.dict) > self.capacity:
                self.dict.popitem(False)



###########################
class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def setNext(self, node):
        self.next = node

    def setPrevious(self, node):
        self.previous = node

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous


class LRUCacheWithDoublylinkedList:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity
        # key : Node for O(1) access
        self.values = {}

    def get(self, key: int) -> int:
        if key in self.values:
            node = self.values[key]
            self.promote(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            node = self.values[key]
            node.value = value
            self.promote(node)
        else:
            node = Node(key=key, value=value)
            self.values[key] = node
            if self.head:
                self.head.setNext(node)
                node.setPrevious(self.head)
                self.head = node
            else:  # empty list
                self.head = node
                self.tail = node

            if len(self.values) > self.capacity:
                oldTailNode = self.tail
                self.values.pop(oldTailNode.key)
                self.tail = self.tail.getNext()
                if self.tail:  # if new tail is not empty, evit previous
                    self.tail.setPrevious(None)

    def promote(self, node):
        if len(self.values) <= 1:
            return
        if node == self.head:
            return

        prevNode = node.getPrevious()
        nextNode = node.getNext()
        if prevNode:
            prevNode.setNext(nextNode)
        else:  # node doesn't have prev, it's the tail, need to update tail
            self.tail = nextNode
        if nextNode:
            nextNode.setPrevious(prevNode)

        node.setNext(None)
        node.setPrevious(None)
        if self.head:  # update head
            self.head.setNext(node)
            node.setPrevious(self.head)
            self.head = node
        else:  # not possible
            raise Exception("promote a node in a list without head")




########
# LRU with dummy head and tail and doubly linkedlist


class Node2:
    def __init__(self, key=None, value=None):
        self.k = key
        self.v = value
        self.next = None
        self.prev = None


class LRUCache2:

    def __init__(self, capacity: int):
        self.kvMap = {}
        self.capacity = capacity
        self.head = Node2()
        self.tail = Node2()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, key):  # key must exist, return the removed Node with prev/next cleared
        node = self.kvMap[key]
        # self.kvMap.pop(key, None) # don't throw if key don't exist, no necessary
        self.kvMap.pop(key)
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        return node

    def debug(self):
        print("----")
        cur = self.head.next
        while cur != self.tail:
            print(cur.k, cur.v)
            cur = cur.next

    def get(self, key: int) -> int:
        if key in self.kvMap:
            retNode = self._remove(key)
            self.put(key, retNode.v)
            return retNode.v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kvMap:
            node = self._remove(key)
            node.v = value
        else:  # add new key
            if len(self.kvMap) == self.capacity:
                keyToRemove = self.tail.prev.k
                self._remove(keyToRemove)
            node = Node(key, value)
        self.kvMap[key] = node
        # put node after head
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node