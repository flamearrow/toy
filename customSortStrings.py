# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
#
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
#
# Return any permutation of s that satisfies this property.


# Example 1:
#
# Input:  order = "cba", s = "abcd"
#
# Output:  "cbad"
#
# Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
#
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
#
# Example 2:
#
# Input:  order = "bcafg", s = "abcd"
#
# Output:  "bcad"
#
# Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.
#
# Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "bacd" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.
#


from typing import List

class Solution:
    def __init__(self):
        pass

    def customSortString2(self, order: str, s: str) -> str:
        return "".join(sorted(s, key=lambda x: order.find(x) if x in order else len(order)))


    def customSortString(self, order: str, s: str) -> str:
        currentHead = 0
        chars = [c for c in s]
        for c in order:
            nextIndex = self.findIndexFrom(chars, currentHead, c)
            while nextIndex >= 0:
                chars[nextIndex], chars[currentHead] = chars[currentHead], chars[nextIndex]
                currentHead += 1
                nextIndex = self.findIndexFrom(chars, currentHead, c)
        return "".join(chars)

    def findIndexFrom(self, chars, head, c):
        for i in range(head, len(chars)):
            if chars[i] == c:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.customSortString2("cba", "abcd"))