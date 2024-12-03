# Given an array of distinct strings words, return the minimal possible abbreviations for every word.
#
# The following are the rules for a string abbreviation:
#
# The initial abbreviation for each word is: the first character, then the number of characters in between, followed by the last character.
# If more than one word shares the same abbreviation, then perform the following operation:
# Increase the prefix (characters in the first part) of each of their abbreviations by 1.
# For example, say you start with the words ["abcdef","abndef"] both initially abbreviated as "a4f". Then, a sequence of operations would be ["a4f","a4f"] -> ["ab3f","ab3f"] -> ["abc2f","abn2f"].
# This operation is repeated until every abbreviation is unique.
# At the end, if an abbreviation did not make a word shorter, then keep it as the original word.
#
# Example
# 1:
#
# Input: words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
# Output: ["l2e", "god", "internal", "me", "i6t", "interval", "inte4n", "f2e", "intr4n"]
# Example
# 2:
#
# Input: words = ["aa", "aaa"]
# Output: ["aa", "aaa"]

from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque


# min impl of trie - use a dictionary of {letter: TrieNode}
class TrieNode:
    def __init__(self):
        self.children = {}  # {letter: TrieNode}
        self.count = 0  # how many prefix reached this node

    def add(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()

        self.children[char].count += 1
        return self.children[char]


class Solution:
    def __init__(self):
        pass

    # first make every word to shortest abbrv
    # then for each word at I, check if there's a dup after it,
    #   if there is, keep reAbbr them until there's no dup
    # done when I reaches end
    # NOTE: to abbr, pass original word and preLen,
    # then save the preLen for each word so it's trivial to calculate abbr each time

    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        # pass in the preLen to reAbbr everytime
        #  don't pass in an already abbrieved word and auto detect
        def toAbbr(preLen, word):  # leave prevLen chars, abrrv the rest
            abbrLen = len(word) - preLen - 1
            if abbrLen <= 1:
                return word
            else:
                return word[:preLen] + str(abbrLen) + word[-1]

        l = len(words)

        # ret = [""] * l

        results = [["", 0]] * l

        for i, word in enumerate(words):
            # ret[i] = toAbbr(1, word)
            results[i] = [toAbbr(1, word), 1]

        # preLens = [1] * l

        for i in range(l):
            hasMoreDup = True
            while hasMoreDup:  # reAbbr all the duplicate words until only ret[i] is unique
                # cur = ret[i]
                cur = results[i][0]
                dupIds = set()
                for j in range(i + 1, l):
                    if results[j][0] == cur:
                        dupIds.add(j)
                if not dupIds:
                    hasMoreDup = False
                else:
                    dupIds.add(i)
                    for dupId in dupIds:
                        results[dupId][1] += 1
                        results[dupId][0] = toAbbr(results[dupId][1], words[dupId])
                        # preLens[dupId] += 1
                        # ret[dupId] = toAbbr(preLens[dupId], words[dupId])

        return [x[0] for x in results]


    # first group all words with same length and first/last letter
    # each group might have colliding abbrevs, so looking at each group
    #  with a trie for each group, search for the first node that has count 1 - it means this prefix is unique
    #   and we can create abbr immediate
    def wordsAbbreviationTrie(self, words):
        groups = {}  # {(worldLen, firstLetter, lastLetter): [words]}

        for i, word in enumerate(words):
            key = (len(word), word[0], word[-1])
            if key not in groups:
                groups[key] = []

            groups[key].append((i, word))

        ret = [""] * len(words)
        # looking at each group, key no longer matters
        for group in groups.values():
            # build a trie for all words - they are same length
            trieRoot = TrieNode()
            for _, word in group:
                cur = trieRoot
                for c in word:
                    cur = cur.add(c)

            # each this word in the group until the first prefix with count 1 is reached
            for index, word in group:
                wordLen = len(word)
                cur = trieRoot
                wordIndex = 0
                while cur.count != 1:
                    cur = cur.children[word[wordIndex]]
                    wordIndex += 1

                # now wordIndex points to the end letter of a unique prefix
                abbr = word[:wordIndex] + str(wordLen - wordIndex - 1) + word[-1]
                if len(abbr) >= len(word):
                    ret[index] = word
                else:
                    ret[index] = abbr

        return ret


if __name__ == '__main__':
    print(Solution().wordsAbbreviationTrie(["abcfgh", "abcdgh", "abedgh"]))
