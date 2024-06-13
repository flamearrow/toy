from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        left, right = 0, 0
        while left < len(words):
            curCount = len(words[left])
            while right + 1 < len(words) and curCount + 1 + len(words[right + 1]) <= maxWidth:
                curCount += 1 + len(words[right + 1])
                right = right + 1
            # nwo right is inclusieve
            newLine = ""
            if left == right:
                newLine = words[left] + " " * (maxWidth-len(words[left]))
            else:
                if right == len(words) - 1: # last line
                    for i in range(left, right+1):
                        if i == left:
                            newLine = words[i]
                        else:
                            newLine += " " + words[i]
                    newLine += " "*(maxWidth-len(newLine))
                else:
                    spaceCount = right - left
                    nonSpaceSize = sum(len(words[i]) for i in range(left, right+1))
                    spaceCountArr = [0] * spaceCount
                    leftOverSpace = (maxWidth - nonSpaceSize)
                    curSpaceCountPtr = 0
                    while leftOverSpace > 0:
                        spaceCountArr[curSpaceCountPtr] += 1
                        curSpaceCountPtr = (curSpaceCountPtr+1) % spaceCount
                        leftOverSpace -= 1

                    curSpaceCountPtr = 0
                    for i in range(left, right+1):
                        if i == left:
                            newLine = words[i]
                        else:
                            newLine += " " * spaceCountArr[curSpaceCountPtr] + words[i]
                            curSpaceCountPtr += 1
            ret.append(newLine)
            right += 1
            left = right
        return ret


if __name__ == '__main__':
    print(Solution().fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16))