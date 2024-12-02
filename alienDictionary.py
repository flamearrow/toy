# There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.
#
# You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are
# sorted lexicographically
#  by the rules of this new language.
#
# If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".
#
# Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.
#
# Example 1:
#
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:
#
# Input: words = ["z","x"]
# Output: "zx"
# Example 3:
#
# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return ""

from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque
from itertools import permutations

class Solution:
    def __init__(self):
        pass

    def alienOrder(self, words: List[str]):
        # all possible order of distinct letters from words
        def generateAlphabets():
            letters = set()
            for w in words:
                for c in w:
                    letters.add(c)

            ret = []
            letters = list(letters)
            available = [True] * len(letters)

            def search(curList):
                if len(curList) == len(letters):
                    ret.append("".join(curList))
                else:
                    for i, isAvail in enumerate(available):
                        if isAvail:
                            available[i] = False
                            curList.append(letters[i])
                            search(curList)
                            curList.pop()
                            available[i] = True
            search([])
            return ret

        def generateAlphabetsNoBoolean():
            letters = set()
            for w in words:
                for c in w:
                    letters.add(c)

            ret = []
            letters = list(letters)

            def search(curList):
                if len(curList) == len(letters):
                    ret.append("".join(curList))
                else:
                    for ch in letters:
                        if ch not in curList:
                            curList.append(ch)
                            search(curList)
                            curList.pop()
            search([])
            return ret

        def generateAlphabetsWithpermutations():
            letters = set()
            for w in words:
                for c in w:
                    letters.add(c)

            ret = []
            letters = list(letters)
            # permutations generates a list of all permutation of the word letters
            for pList in permutations(letters):
                ret.append("".join(pList))
            return ret

        def isLarger(left, right, alphaDict):
            cur = 0
            while cur < len(left) and cur < len(right):
                if alphaDict[left[cur]] > alphaDict[right[cur]]:
                    return True
                elif alphaDict[left[cur]] < alphaDict[right[cur]]:
                    return False
                else:
                    cur += 1
            if cur == len(left) and cur == len(right):  # equal
                return False
            elif cur == len(left):  # same prefix, left is shorter than right
                return False
            else:  # same prefix, left is longer than right
                return True

        alphabets = generateAlphabetsNoBoolean()
        for alphabet in alphabets:
            # alphaDict is a dict of {char: int}
            alphaDict = {}
            for i, c in enumerate(alphabet):
                alphaDict[c] = i
            found = True
            for i in range(1, len(words)):
                prev = words[i - 1]
                cur = words[i]
                if isLarger(prev, cur, alphaDict):
                    found = False
                    break
            if found:
                return alphabet

        return ""


if __name__ == '__main__':
    result = Solution().alienOrder(words=["wrt","wrf","er","ett","rftt"])
    print(result)
