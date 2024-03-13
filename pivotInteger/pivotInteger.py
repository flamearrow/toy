# Given a positive integer n, find the pivot integer x such that:
#
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.



class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n+1):
            left = [j for j in range(1, i+1)]
            print("left", left)
            right = [j for j in range(i, n+1)]
            print("right", right)
            if sum(left) == sum(right):
                return i
        return -1



if __name__ == '__main__':
    s = Solution()
    print(s.pivotInteger(1))
