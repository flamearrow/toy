# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].
#
# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
#
# Example 1:
#
#
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
# Example 2:
#
# Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
# Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]


from typing import List

class Solution:
    def __init__(self):
        pass

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        height, width = len(mat), len(mat[0])
        def sortFrom(x, y):
            matDiag = []
            x0, y0 = x, y
            while x0 < width and y0 < height:
                matDiag.append(mat[y0][x0])
                y0 += 1
                x0 += 1
            matDiag.sort()
            x0, y0, i = x, y, 0
            while x0 < width and y0 < height:
                mat[y0][x0] = matDiag[i]
                y0 += 1
                x0 += 1
                i += 1
        # button to top
        for y in range(height - 1, 0, -1):
            sortFrom(0, y)

        sortFrom(0, 0)

        # left to right
        for x in range(1, width):
            sortFrom(x, 0)

        return mat


if __name__ == '__main__':
    s = Solution()