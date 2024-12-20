from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isRowValid():
            height = len(board)
            width = len(board[0])
            for i in range(height):
                seen = set()
                for j in range(width):
                    if board[i][j] != "." and board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
            return True

        def isColumnValid():
            height = len(board)
            width = len(board[0])
            for i in range(width):
                seen = set()
                for j in range(height):
                    if board[j][i] != "." and board[j][i] in seen:
                        return False
                    else:
                        seen.add(board[j][i])
            return True

        def isBlockValid():
            for i in range(0, 3):
                for j in range(0, 3):
                    blockI = i * 3
                    blockJ = j * 3
                    seen = set()
                    for bi in range(blockI, blockI + 3):
                        for bj in range(blockJ, blockJ + 3):
                            if board[bi][bj] != "." and board[bi][bj] in seen:
                                print(" blockInvalid", blockI, blockJ)
                                print(" blockInvalid", seen)
                                return False
                            else:
                                seen.add(board[bi][bj])
            return True

        return isRowValid() and isColumnValid() and isBlockValid()

    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        boxes = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                box = boxes[(i // 3) * 3 + j // 3]
                row = rows[i]
                col = cols[j]

                curV = board[i][j]

                if curV in box or curV in row or curV in col:
                    return False

                if curV != ".":
                    box.add(curV)
                    row.add(curV)
                    col.add(curV)

        return True


if __name__ == '__main__':
    board = [['7', '2', '1', '8', '5', '3', '9', '4', '6'],
             ['4', '9', '5', '6', '1', '7', '8', '3', '2'],
             ['8', '3', '6', '4', '2', '9', '7', '5', '1'],
             ['9', '6', '7', '3', '8', '4', '1', '2', '5'],
             ['2', '1', '4', '7', '6', '5', '3', '9', '8'],
             ['3', '5', '8', '2', '9', '1', '6', '7', '4'],
             ['1', '7', '2', '5', '3', '6', '4', '8', '9'],
             ['6', '8', '3', '9', '4', '2', '5', '1', '7'],
             ['5', '4', '9', '1', '7', '8', '2', '6', '3']]
    print(Solution().isValidSudoku2(board))
