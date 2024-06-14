from typing import List
# You are given a string s and an array of strings words. All the strings of words are of the same length.
#
# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
#
# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any orde
#
# Example 1:
#
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
#
# Output: [0,9]
#
# Explanation:
#
# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
#
# Example 2:
#
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
#
# Output: []
#
# Explanation:
#
# There is no concatenated substring.
#
# Example 3:
#
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
#
# Output: [6,9,12]
#
# Explanation:
#
# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        wordLen = len(words[0])
        targetSize = len(words) * wordLen
        for starting in range(0, wordLen):
            wordsCount = {}
            for word in words:
                if word not in wordsCount:
                    wordsCount[word] = 1
                else:
                    wordsCount[word] = wordsCount[word] + 1
            print(wordsCount)
            left, right = starting, starting + wordLen # right exclusive
            while right <= len(s):
                newWord = s[right-wordLen:right]
                print(" newWord", newWord)
                if wordsCount.get(newWord, 0) > 0: # got a new word
                    print(" got newWord", newWord)
                    wordsCount[newWord] -= 1
                    print("  now size:", right - left)
                    if right - left == targetSize: # got a full substring
                        ret.append(left)
                        wordsCount[s[left:left+wordLen]] += 1 # remove one from left
                        left += wordLen
                        right += wordLen
                    elif right - left < targetSize: # try to get the next word
                        right += wordLen
                else: # right is not new word, move start by 1 unit
                    wordToRemove = s[left:left+wordLen]
                    if wordToRemove in wordsCount:
                        wordsCount[wordToRemove] += 1
                    left += wordLen
                    if left == right:
                        right += wordLen
        return ret


if __name__ == '__main__':
    print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))