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