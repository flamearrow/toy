from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque


# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def nextEmptyPoint():  # next position "."
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        return (i, j)
            return None

        def possibleValuesAt(y, x):  # list of values
            candidates = set()
            for i in range(1, 10):
                candidates.add(str(i))
            for i in range(9):
                # don't need to check "." as discard ignore non existant key
                candidates.discard(board[i][x])
                candidates.discard(board[y][i])
            for boxY in range((y // 3) * 3, (y // 3) * 3 + 3):
                for boxX in range((x // 3) * 3, (x // 3) * 3 + 3):
                    candidates.discard(board[boxY][boxX])

            return candidates

        def solve():
            emptyPoint = nextEmptyPoint()
            if not emptyPoint:
                return True
            y, x = emptyPoint
            validValues = possibleValuesAt(y, x)
            for v in validValues:
                board[y][x] = v
                solveValue = solve()
                if solveValue:
                    return True
                else:
                    board[y][x] = "."
            return False

        solve()

    # add candidates upfront, use intersection to determin candaidates
    def solveSudoku2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # candidates for each row, colum and box
        rows = [set(str(i) for i in range(1, 10)) for _ in range(9)]
        cols = [set(str(i) for i in range(1, 10)) for _ in range(9)]
        boxes = [set(str(i) for i in range(1, 10)) for _ in range(9)]

        emptyCells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    emptyCells.append((i, j))
                else:
                    val = board[i][j]
                    row = i
                    col = j
                    box = (i // 3) * 3 + (j // 3)
                    rows[row].remove(val)
                    cols[col].remove(val)
                    boxes[box].remove(val)

        def solve():
            if not emptyCells:
                return True
            emptyCell = emptyCells.pop()
            y, x = emptyCell
            row = y
            col = x
            box = (y // 3) * 3 + (x // 3)

            # candidates at this point is the intersection of row/col/box
            candidates = rows[row] & cols[col] & boxes[box]

            for candidate in candidates:
                board[y][x] = candidate
                rows[row].remove(candidate)
                cols[col].remove(candidate)
                boxes[box].remove(candidate)
                if solve():
                    return True
                else:
                    # backtrack
                    board[y][x] = "."
                    rows[row].add(candidate)
                    cols[col].add(candidate)
                    boxes[box].add(candidate)
            emptyCells.append(emptyCell)
            return False

        solve()


if __name__ == '__main__':
    # board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #          [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #          [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    board = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "9", ".", ".", "1", ".", ".", "3", "."],
             [".", ".", "6", ".", "2", ".", "7", ".", "."],
             [".", ".", ".", "3", ".", "4", ".", ".", "."],
             ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", "2", "5", ".", "6", "4", ".", "."],
             [".", "8", ".", ".", ".", ".", ".", "1", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    Solution().solveSudoku(board)
    for row in board:
        print(row)
