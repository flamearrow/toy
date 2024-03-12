from typing import List


# Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

# Implement the ZigzagIterator class:

# ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
# boolean hasNext() returns true if the iterator still has elements, and false otherwise.
# int next() returns the current element of the iterator and moves the iterator to the next element.


# Example 1:

# Input: v1 = [1,2], v2 = [3,4,5,6]
# Output: [1,3,2,4,5,6]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
# Example 2:

# Input: v1 = [1], v2 = []
# Output: [1]
# Example 3:

# Input: v1 = [], v2 = [1]
# Output: [1]


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.vec = [v1, v2]
        if self.v1:
            self.x = 0
            self.y = 0
        else:
            self.x = 0
            self.y = 1

    def bumpNext(self):
        # at v1, want to go down
        if self.y == 0:
            # can go down
            if self.x < len(self.v2):
                self.y = self.y + 1
            # go right - might out of bounds
            else:
                self.x = self.x + 1
        # at v2, want to go upper right
        else:
            # go upper right
            if self.x + 1 < len(self.v1):
                self.x = self.x + 1
                self.y = 0
            # go right - might out of bounds
            else:
                self.x = self.x + 1

    def next(self) -> int:
        ret = self.vec[self.y][self.x]
        self.bumpNext()
        return ret

    def hasNext(self) -> bool:
        # check x is out of bounds of current list
        return self.x < len(self.vec[self.y])

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())