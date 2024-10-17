# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
# the smallest in lexicographical order
#  among all possible results

# Example 1:
#
# Input: s = "bcabc"
# Output: "abc"
# Example 2:
#
# Input: s = "cbacdcbc"
# Output: "acdb

from collections import Counter, deque
class Solution:

    # find pos, the position of the smallest c, whose suffix contains all other strings needed
    # then take c, recursively calculate required values for the substring after c, note c needs to be removed form subtring
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
        c = Counter(s)  # {char: count}

        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            c[s[i]] -= 1
            if c[s[i]] == 0:
                break

        suffixWithoutPos = s[pos + 1:].replace(s[pos], "")

        return s[pos] + self.removeDuplicateLetters(suffixWithoutPos)


    # using stack:
    # for each incoming char,
    # if previous top is greater than cur, and previous top will occur later, we can drop previous stop
    # otherwise remember what chars are added, if it's added, skip this char
    def removeDuplicateLettersStack(self, s: str) -> str:
        stack = deque()
        c = Counter(s)
        added = set()
        for ch in s:
            if ch in added:
                c[ch] -= 1
                continue
            while stack:
                topCh = stack[len(stack) - 1]
                # if the top char is greater then current char
                # and the top char will appear later, then remove top char
                if topCh > ch and c[topCh] > 0:
                    stack.pop()
                    added.remove(topCh)
                else:
                    break
            # if top is the same with upcoming char, don't do anything
            stack.append(ch)
            added.add(ch)
            c[ch] -= 1

        ret = ""
        for c in stack:
            ret += c
        return ret

if __name__ == '__main__':
    print(Solution().removeDuplicateLettersStack("abacb"))