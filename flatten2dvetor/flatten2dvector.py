# Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.
#
# Implement the Vector2D class:
#
# Vector2D(int[][] vec) initializes the object with the 2D vector vec.
# next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
# hasNext() returns true if there are still some elements in the vector, and false otherwise.
from typing import List


# Example 1:
#
# Input
# ["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
# [[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
# Output
# [null, 1, 2, 3, true, true, 4, false]
#
# Explanation
# Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
# vector2D.next();    // return 1
# vector2D.next();    // return 2
# vector2D.next();    // return 3
# vector2D.hasNext(); // return True
# vector2D.hasNext(); // return True
# vector2D.next();    // return 4
# vector2D.hasNext(); // return False

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.listAt = 0
        self.itemAt = -1
        self.bumpToNext()
        self.busted = False

    def bumpToNext(self):
        # if current list not exhausted, go to next item
        if not len(self.vec):
            self.busted = True
            return

        if self.itemAt < len(self.vec[self.listAt]) - 1:
            self.itemAt += 1
        # otherwise need to bump list
        else:
            # need to bump to the next non empty list or reach the end
            nextListIndex = self.listAt + 1
            while nextListIndex < len(self.vec) and (not self.vec[nextListIndex]):
                nextListIndex += 1
            # now if nextListIndex is out of bounds, then entire list is exhausted
            # otherwise it's pointing to the next non empty List
            # reset itemAt to 0 regardless
            self.listAt = nextListIndex
            self.itemAt = 0

    def next(self) -> int:
        ret = self.vec[self.listAt][self.itemAt]
        self.bumpToNext()
        return ret

    def hasNext(self) -> bool:
        return False if self.busted else self.listAt < len(self.vec)



if __name__ == '__main__':
    # v = Vector2D([[1,2],[3],[4]])
    l = [[], []]
    v = Vector2D(l)
    print(v.hasNext())
    # print(v.next())
    # print(v.next())
    # print(v.next())
    # print(v.hasNext())
    # print(v.hasNext())
    # print(v.next())
    # print(v.hasNext())