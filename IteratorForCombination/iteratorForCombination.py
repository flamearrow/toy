# Design the CombinationIterator class:

# CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# next() Returns the next combination of length combinationLength in lexicographical order.
# hasNext() Returns true if and only if there exists a next combination.


# Example 1:

# Input
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# Output
# [null, "ab", true, "ac", true, "bc", false]

# Explanation
# CombinationIterator itr = new CombinationIterator("abc", 2);
# itr.next();    // return "ab"
# itr.hasNext(); // return True
# itr.next();    // return "ac"
# itr.hasNext(); // return True
# itr.next();    // return "bc"
# itr.hasNext(); // return False

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.len = len(characters)
        self.combLen = combinationLength
        self.buff = []
        for _ in range(combinationLength):
            self.buff.append(True)
        for _ in range(self.len - combinationLength):
            self.buff.append(False)
        self.exhausted = False
        print("init:", self.buff)

    def next(self) -> str:
        ret = ""
        for i in range(0, self.len):
            if self.buff[i]:
                ret += self.chars[i]
        self.bump()
        print("bump:", self.buff)
        return ret

    def bump(self):
        # if last is not 1, then can move one right
        if not self.buff[self.len - 1]:
            rightMostOneIndex = self.len - 1
            while self.buff[rightMostOneIndex] != True:
                rightMostOneIndex -= 1
            # move one right
            self.buff[rightMostOneIndex] = False
            self.buff[rightMostOneIndex + 1] = True
            return
        else:  # something like 111000001111, or 11111, or 01111
            rightMost0Index = self.len - 1
            while rightMost0Index > 0 and self.buff[rightMost0Index]:
                rightMost0Index -= 1
            if (rightMost0Index == 0):  # 11111
                self.exhausted = True
                return
            rightMostOnes = self.len - 1 - rightMost0Index
            while rightMost0Index >= 0 and not self.buff[rightMost0Index]:
                rightMost0Index -= 1
            if rightMost0Index < 0:  # 0111 already last one
                self.exhausted = True
                return
            # swap 1 and 0
            self.buff[rightMost0Index] = False  # if it's 10111, then become 01111
            self.buff[rightMost0Index + 1] = True

            currentIndexToChange = rightMost0Index + 2
            for _ in range(rightMostOnes):
                self.buff[currentIndexToChange] = True
                currentIndexToChange += 1
            while currentIndexToChange < self.len:
                self.buff[currentIndexToChange] = False
                currentIndexToChange += 1

    def hasNext(self) -> bool:
        return not self.exhausted


# build all combinations upfront using backtrack
class CombinationIterator2:

    def __init__(self, characters: str, combinationLength: int):
        # list of strings to return
        self.buffer = []
        def search(curPath, curIndex):
            if len(curPath) == combinationLength:
                self.buffer.append("".join(curPath))
                return
            else:
                for i in range(curIndex, len(characters)):
                    curPath.append(characters[i])
                    search(curPath, i+1)
                    curPath.pop()
        search([], 0)
        self.buffer.reverse()
        for buffer in self.buffer:
            print(buffer)

    def next(self) -> str:
        return self.buffer.pop()

    def hasNext(self) -> bool:
        return self.buffer


class CombinationIterator3:

    # use bitmap
    # trick: bin(someNumber) -> return sstring represnetation of bitnary in 0b01010110
    # str.count('1') counts number of 1s in the string
    def __init__(self, characters: str, combinationLength: int):
        self.bitMap = ((1 << combinationLength) - 1) << (len(characters) - combinationLength)
        self.k = combinationLength
        self.characters = characters
        self.len = len(characters)
        print(" initial bitmap", bin(self.bitMap))


    def next(self) -> str:
        print(" bitmap", bin(self.bitMap))

        # retArr = [self.characters[i] for i in range(0, self.k+1) if ((1 << (self.k-i)) & self.bitMap) > 0]
        retArr = []

        for index, c in enumerate(self.characters):
            bitMapShift = self.len - index - 1
            if (1 << bitMapShift) & self.bitMap:
                retArr.append(c)

        self.bitMap -= 1
        while bin(self.bitMap).count('1') != self.k:
            self.bitMap -= 1

        print(" updated bitmap", bin(self.bitMap))

        return "".join(retArr)

    def hasNext(self) -> bool:
        return self.bitMap > 0


if __name__ == '__main__':
    cb = CombinationIterator("bvwz", 2)
    while(cb.hasNext()):
        print(cb.next())
    # print(cb.hasNext())
    # print(cb.hasNext())
    # print(cb.next())
    # print(cb.next())
    # print(cb.hasNext())
    # print(cb.hasNext())
    # print(cb.next())
    # print(cb.hasNext())
    # print(cb.hasNext())
    # print(cb.hasNext())
