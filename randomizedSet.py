import random

# Implement the RandomizedSet class:
#
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity

class RandomizedSet:

    def __init__(self):
        self.iv = {}
        self.vi = {}
        self.nextIndex = 0

    def insert(self, val: int) -> bool:
        if val in self.vi:
            return False
        else:
            self.vi[val] = self.nextIndex
            self.iv[self.nextIndex] = val
            self.nextIndex += 1
            return True

    def remove(self, val: int) -> bool:
        # swap with latest
        if val in self.vi:
            oldIndex = self.vi[val]
            del self.vi[val]
            del self.iv[oldIndex]
            self.nextIndex -= 1
            if self.nextIndex > 0 and oldIndex != self.nextIndex:
                # swap with last Index
                lastIndex = self.nextIndex
                lastValue = self.iv[lastIndex]
                # need assign lastValue to oldIndex
                del self.iv[lastIndex]
                self.iv[oldIndex] = lastValue
                self.vi[lastValue] = oldIndex # was pointing to lastIndex
            return True
        else:
            return False


    def getRandom(self) -> int:
        return self.iv[random.randint(0, self.nextIndex-1)]