# walk along the trie, when current word == "", reaaches the end node, check how many words termintaed here

# Trie can do two things
#  check if a prefix exists
#  check if a string existt
class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.terminated = 0

    def insert(self, word: str) -> None:
        if word:
            childIndex = ord(word[0]) - ord('a')
            if not self.children[childIndex]:
                self.children[childIndex] = Trie()
            self.children[childIndex].insert(word[1:])
        else:
            self.terminated += 1

    def countWordsEqualTo(self, word: str) -> int:
        if word:
            childIndex = ord(word[0]) - ord('a')
            if self.children[childIndex]:
                return self.children[childIndex].countWordsEqualTo(word[1:])
            else:
                return 0
        else:
            return self.terminated

    def countWordsStartingWith(self, prefix: str) -> int:
        if prefix:
            childIndex = ord(prefix[0]) - ord('a')
            if self.children[childIndex]:
                return self.children[childIndex].countWordsStartingWith(prefix[1:])
            else:
                return 0
        else:
            return self.allTerminated()

    def allTerminated(self):
        ret = self.terminated
        for child in self.children:
            if child:
                ret += child.allTerminated()
        return ret

    def erase(self, word: str) -> None:
        if word:
            childIndex = ord(word[0]) - ord('a')
            if self.children[childIndex]:
                self.children[childIndex].erase(word[1:])
        else:
            self.terminated -= 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)