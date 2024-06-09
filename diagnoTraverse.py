from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        upRight = True # is going top right
        x = 0
        y = 0
        height = len(mat)
        width = len(mat[0])
        ret = []

        while True:
            ret.append(mat[y][x])
            print(" y ", y, " x ", x)
            if x == width - 1 and y == height - 1:
                break
            if upRight:
                # try go up right
                if (x+1) < width and (y-1) >= 0:
                    x = x+1
                    y = y-1
                else: # need to go bottom left
                    if x+1 < width:
                        x = x+1
                    else:
                        y = y+1
                    upRight = False
            else:
                 # try go bottom left
                if (x-1) >= 0 and (y+1) < height:
                    x = x-1
                    y = y+1
                else: # need to go bottom left
                    if y+1 < height:
                        y = y+1
                    else:
                        x = x+1
                    upRight = True
        return ret



if __name__ == '__main__':
    print(Solution().findDiagonalOrder([[1, 2, 3], [4,5,6]]))