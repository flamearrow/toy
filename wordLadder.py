from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque


class BFSNode:
    def __init__(self, word, visited=None):
        if visited:
            self.visited = visited
        else:
            self.visited = [word]

    def add(self, newWord):
        self.visited.append(newWord)

    def contains(self, word):
        return word in self.visited

    def last(self):
        return self.visited[-1]

    def __str__(self):
        return self.last()

    def copy(self):
        return BFSNode("", visited=self.visited[:])

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append(BFSNode(beginWord))

        def neighbours(word):  # all words in wordList that's one letter different from word
            ret = []
            for candidate in wordList:
                diffCount = 0
                for i in range(len(candidate)):
                    if candidate[i] != word[i]:
                        diffCount += 1
                        if diffCount > 1:
                            break
                if diffCount == 1:
                    ret.append(candidate)
            return ret

        foundNode = None
        while queue:
            nextNode = queue.popleft()
            for n in neighbours(nextNode.last()):
                if n == endWord:
                    nextNode.add(n)
                    foundNode = nextNode
                    break
                elif not nextNode.contains(n):
                    copyNode = nextNode.copy()
                    copyNode.add(n)
                    queue.append(copyNode)
            if foundNode:
                break
        if foundNode:
            print(foundNode.visited)
            return len(foundNode.visited)
        else:
            return 0

    # 1: prebuilt the word pattern to get neighbours
    # 2: don't use a dedicated node, instead
    #   just use (lastWord, lastLength) tuple as node
    #   to check viable next node, create a set of avaialble words, remove from that set as a word is enqueued
    #    since we're BFS, we won't miss out shorter path as one will be visited first
    def ladderLengthFaster(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # makes it faster to find neighbours
        #  e.g "*og": ["dog", "cog", "log"]
        neighbours = {}  # {pattern: [words]}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                if pattern not in neighbours:
                    neighbours[pattern] = [word]
                else:
                    neighbours[pattern].append(word)

        availableWords = set(wordList)

        queue = deque()
        queue.append((beginWord, 1))


        while queue:
            curWord, curLen = queue.popleft()
            for i in range(len(curWord)):
                pattern = curWord[:i] + "*" + curWord[i+1:]
                for n in neighbours.get(pattern, []):
                    if n == endWord:
                        return curLen + 1
                    elif n in availableWords:
                        availableWords.remove(n)
                        queue.append((n, curLen + 1))
        return 0


if __name__ == '__main__':
    print(Solution().ladderLengthFaster("hit", "cog", ["hot","dot","dog","lot","log","cog"]))