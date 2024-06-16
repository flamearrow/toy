from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
class Solution:
    def totalNQueens(self, n: int) -> int:
        ret = [0]
        board = [[0] * n for _ in range(n)]

        # native way - check if there's conflict each row/ ecach column, each diagnal/ each anti diagnal
        # a better way to check if [i, j] is valid:
        #  use 4 sets: cols, rows, diags, antidiags to save the currently occupied lines
        #    diags: each diag can be reprecented by (row-col) - as all ndoes under the same diag have same (row-col) value
        #    antidiags: similar to diag
        def validBoard():
            print("current boards")
            for row in board:
                print(row)
            # rows
            for i in range(0, n):
                seenOne = False
                for j in range(0, n):
                    if board[i][j] == 1:
                        if seenOne:
                            return False
                        else:
                            seenOne = True

            # cols
            for i in range(0, n):
                seenOne = False
                for j in range(0, n):
                    if board[j][i] == 1:
                        if seenOne:
                            return False
                        else:
                            seenOne = True

            # diagnal
            for i in range(0, n):
                curY = 0
                curX = i
                seenOne = False
                while curY < n and curX < n:
                    if board[curY][curX] == 1:
                        if seenOne:
                            return False
                        else:
                            seenOne = True
                    curY += 1
                    curX += 1

            for i in range(0, n):
                curY = 0
                curX = i
                seenOne = False
                while curY < n and curX >= 0:
                    if board[curY][curX] == 1:
                        if seenOne:
                            return False
                        else:
                            seenOne = True
                    curY += 1
                    curX -= 1

            for i in range(0, n):
                curY = i
                curX = 0
                seenOne = False
                while curY < n and curX < n:
                    if board[curY][curX] == 1:
                        if seenOne:
                            return False
                        else:
                            seenOne = True
                    curY += 1
                    curX += 1

            for i in range(0, n):
                curY = i
                curX = n - 1
                seenOne = False
                while curY < n and curX >= 0:
                    if board[curY][curX] == 1:
                        if seenOne:
                            return False
                        else:
                            seenOne = True
                    curY += 1
                    curX -= 1

            return True

        def search(placed, cur):
            if placed == n:
                ret[0] += 1
                return
            if cur == n * n:
                return

            for next in range(cur, n * n):
                y = next // n
                x = next % n
                board[y][x] = 1
                if validBoard():
                    search(placed + 1, next + 1)
                board[y][x] = 0

        search(0, 0)
        return ret[0]


if __name__ == '__main__':
    print(Solution().totalNQueens(4))