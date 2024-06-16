from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode


# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = [len(board)]
        width = [len(board[0])]
        size = [height[0] * width[0]]

        visited = set()

        def search(word, cur):
            if not word:
                return True
            if cur == size[0]:
                return False
            if cur < 0 or cur > size[0]:
                return False
            visited.add(cur)

            y = cur // width[0]
            x = cur % width[0]
            if board[y][x] != word[0]:
                visited.remove(cur)
                return False
            else:
                if len(word) == 1:
                    return True
                toVisits = []
                # try right, just increment cur+1 might go to the first of nextrow
                if cur % width[0] + 1 < width[0] and cur + 1 not in visited:
                    toVisits.append(cur + 1)
                # try left, just decrement cur+1 might go to the first of prevRow
                if cur % width[0] - 1 >= 0 and cur - 1 not in visited:
                    toVisits.append(cur - 1)
                # try up
                if cur - width[0] >= 0 and cur - width[0] not in visited:
                    toVisits.append(cur - width[0])
                # try right
                if cur + width[0] < size[0] and cur + width[0] not in visited:
                    toVisits.append(cur + width[0])

                for toVisit in toVisits:
                    if search(word[1:], toVisit):
                        return True
                visited.remove(cur)
                return False

        for i in range(0, size[0]):
            if search(word, i):
                return True
        return False


if __name__ == '__main__':
    print(Solution().exist([["a", "e", "b"], ["d", "g", "c"]], "bcd"))
