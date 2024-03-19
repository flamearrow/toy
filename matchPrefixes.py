# There is a given list of strings where each string contains only lowercase letters from , inclusive. The set of strings is said to be a GOOD SET if no string is a prefix of another string. In this case, print GOOD SET. Otherwise, print BAD SET on the first line followed by the string being checked.
#
# Note If two strings are identical, they are prefixes of each other.
#
# Example
#
# Here 'abcd' is a prefix of 'abcde' and 'bcd' is a prefix of 'bcde'. Since 'abcde' is tested first, print
#
# BAD SET
# abcde
# .
#
# No string is a prefix of another so print
#
# GOOD SET
# Function Description
# Complete the noPrefix function in the editor below.
#
# noPrefix has the following parameter(s):
# - string words[n]: an array of strings
#
# Prints
# - string(s): either GOOD SET or BAD SET on one line followed by the word on the next line. No return value is expected.
#
# Input Format
# First line contains , the size of .
# Then next  lines each contain a string, .

class TrieNode:
    def __init__(self, terminated):
        self.children = [None] * 26
        self.terminated = terminated

    # return (children, hasThisChildBefore)
    def set_child(self, value, terminated):
        i = ord(value) - ord('a')
        hasChildBefore = True
        if not self.children[i]:
            hasChildBefore = False
            self.children[i] = TrieNode(terminated)
        return self.children[i], hasChildBefore

    # return if this word is a refix, or there is a prefix of this word
    def try_add_word(self, word):
        node = self
        for index, c in enumerate(word):
            if index == len(word) - 1:
                # end of word, if this is a prefix of this word, hasChildBefore=true
                node, hasChildBefore = node.set_child(c, True)
                return hasChildBefore
            else:
                # mid of word, if the node returned is a termination node,
                # it means this word is longer than a prefix
                node, hasChildBefore = node.set_child(c, False)
                if node.terminated:
                    return True
        return False


def noPrefix(words):
    trieRoot = TrieNode(False)
    for word in words:
        if trieRoot.try_add_word(word):
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")
