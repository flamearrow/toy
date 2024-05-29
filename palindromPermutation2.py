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


if __name__ == '__main__':
    # s = Solution()
    # print(s.generatePalindromes("aaabbccc"))
    i = int('inf')
    if 23 < i:
        print("a")
