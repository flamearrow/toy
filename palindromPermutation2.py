# Given a string s, return all the palindromic permutations (without duplicates) of it.
#
# You may return the answer in any order. If s has no palindromic permutation, return an empty list
# Example 1:
#
# Input: s = "aabb"
# Output: ["abba","baab"]
# Example 2:
#
# Input: s = "abc"
# Output: []
from typing import List


class Solution:
    def __init__(self):
        pass

    def generatePalindromes(self, s: str) -> List[str]:
        cCount = {}
        for c in s:
            if c in cCount:
                cCount[c] = cCount[c] + 1
            else:
                cCount[c] = 1

        odd = list(filter(lambda x: x[1] % 2 == 1, cCount.items()))
        if len(odd) > 1:
            return []
        else:
            if len(odd) == 1:
                inital = odd[0][0]
                if cCount[odd[0][0]] == 1:
                    cCount.pop(odd[0][0])
                else:
                    cCount[odd[0][0]] = odd[0][1] - 1
            else:
                inital = ""
            # now cCount has all even numbers
            result = set()

            def doCreatePalindrom(cur, leftOver):
                if not leftOver:
                    result.add(cur)
                else:
                    for (index, c) in enumerate(leftOver):
                        doCreatePalindrom(c + cur + c, leftOver[:index] + leftOver[index + 1:])

            leftOver = ""
            for c, count in cCount.items():
                leftOver += c * (count//2)

            doCreatePalindrom(inital, leftOver)

            return list(result)

    def generatePalindromes2(self, s: str) -> List[str]:
        cCount = {}
        for c in s:
            if c in cCount:
                cCount[c] += 1
            else:
                cCount[c] = 1

        center = ""
        seenOdd = False
        for c in cCount:
            if cCount[c] % 2 == 1:
                if seenOdd:
                    return []
                else:
                    seenOdd = True
                    center = c
                    cCount[c] -= 1

        ret = []

        def buildPalindrome(cur):
            if len(cur) == len(s):
                ret.append(cur)
            else:
                for c in cCount:
                    if cCount[c] > 0:
                        cCount[c] -= 2
                        buildPalindrome(c+cur+c)
                        cCount[c] += 2

        buildPalindrome(center)

        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.generatePalindromes2("aaab"))