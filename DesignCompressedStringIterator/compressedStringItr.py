# implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

# Implement the StringIterator class:

# next() Returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
# hasNext() Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.


# Example 1:

# Input
# ["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
# [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
# Output
# [null, "L", "e", "e", "t", "C", "o", true, "d", true]

# Explanation
# StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
# stringIterator.next(); // return "L"
# stringIterator.next(); // return "e"
# stringIterator.next(); // return "e"
# stringIterator.next(); // return "t"
# stringIterator.next(); // return "C"
# stringIterator.next(); // return "o"
# stringIterator.hasNext(); // return True
# stringIterator.next(); // return "d"
# stringIterator.hasNext(); // return True

class StringIterator:

    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.currentLetterPointer = 0  # pointer in compressedString
        self.currentLetterCount = 0
        if compressedString:
            self.exhausted = False
            self.currentLetterTotal = self.calculateLetterTotal()
        else:
            self.exhausted = True

    def calculateLetterTotal(self):
        # calculate how many letters required at self.compressedString[self.currentLetterPointer]
        index = self.currentLetterPointer + 1
        while index < len(self.compressedString) and self.compressedString[index].isdigit():
            index += 1
        ret = int(self.compressedString[self.currentLetterPointer + 1:index])
        return ret

    def moveToNextLetterAndMaybeUpdateTotal(self):
        index = self.currentLetterPointer + 1
        while index < len(self.compressedString) and self.compressedString[index].isdigit():
            index += 1
        if index == len(self.compressedString):
            self.exhausted = True
        else:
            self.currentLetterPointer = index
            self.currentLetterTotal = self.calculateLetterTotal()
            self.currentLetterCount = 0

    def next(self) -> str:
        if self.hasNext():
            ret = self.compressedString[self.currentLetterPointer]
            self.currentLetterCount += 1
            if self.currentLetterCount >= self.currentLetterTotal:
                self.moveToNextLetterAndMaybeUpdateTotal()
            return ret
        else:
            return " "

    def hasNext(self) -> bool:
        return not self.exhausted