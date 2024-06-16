from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
#
# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board
#
# Example
# 1:
#
# Input: board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
#
# Output: [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
#

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        height = len(board)
        width = len(board[0])
        parents = [-1] * (width * height)

        def findAncestor(x):
            if parents[x] == -1:
                return -1
            if x != parents[x]:
                return findAncestor(parents[x])
            else:
                return x

        def union(x, y):
            aX = findAncestor(x)
            aY = findAncestor(y)
            parents[aX] = aY

        for i in range(height):
            for j in range(width):
                if board[i][j] == 'O':
                    parents[i * width + j] = i * width + j

        for i in range(height):
            for j in range(width):
                if board[i][j] == 'O':
                    # up
                    if i - 1 >= 0 and board[i - 1][j] == 'O':
                        union(i * width + j, (i - 1) * width + j)
                    # down
                    if i + 1 < height and board[i + 1][j] == 'O':
                        union(i * width + j, (i + 1) * width + j)
                    # left
                    if j - 1 >= 0 and board[i][j - 1] == 'O':
                        union(i * width + j, i * width + j - 1)
                    # right
                    if j + 1 < width and board[i][j + 1] == 'O':
                        union(i * width + j, i * width + j + 1)

        badAncestors = []
        for i in range(height):
            if board[i][0] == 'O':
                badAncestors.append(findAncestor(i * width))
            if board[i][width - 1] == 'O':
                badAncestors.append(findAncestor(i * width + width - 1))
        for j in range(width):
            if board[0][j] == 'O':
                badAncestors.append(findAncestor(j))
            if board[height - 1][j] == 'O':
                badAncestors.append(findAncestor((height - 1) * width + j))

        for i in range(height):
            for j in range(width):
                curnAncestor = findAncestor(i * width + j)
                if curnAncestor != -1 and curnAncestor not in badAncestors:
                    board[i][j] = 'X'

if __name__ == '__main__':
    print(Solution())