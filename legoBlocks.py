# You have an infinite number of 4 types of lego blocks of sizes given as (depth x height x width):
#
# d	h	w
# 1	1	1
# 1	1	2
# 1	1	3
# 1	1	4
# Using these blocks, you want to make a wall of height  and width . Features of the wall are:
#
# - The wall should not have any holes in it.
# - The wall you build should be one solid structure, so there should not be a straight vertical break across all rows of bricks.
# - The bricks must be laid horizontally.
#
# How many ways can the wall be built?
#
# Example
#
#
#
# The height is  and the width is . Here are some configurations:
#
# image
#
# These are not all of the valid permutations. There are  valid permutations in all.
#
# Function Description
#
# Complete the legoBlocks function in the editor below.
#
# legoBlocks has the following parameter(s):
#
# int n: the height of the wall
# int m: the width of the wall
# Returns
# - int: the number of valid wall formations modulo
#
# Input Format
#
# The first line contains the number of test cases .
#
# Each of the next  lines contains two space-separated integers  and .
#
# Constraints
#
#
#
# Sample Input
#
# STDIN   Function
# -----   --------
# 4       t = 4
# 2 2     n = 2, m = 2
# 3 2     n = 3, m = 2
# 2 3     n = 2, m = 3
# 4 4     n = 4, m = 4
# Sample Output
#
# 3
# 7
# 9
# 3375
# Explanation
#
# For the first case, we can have:
#
# image
#
#
# For the second case, each row of the wall can contain either two blocks of width 1, or one block of width 2. However, the wall where all rows contain two blocks of width 1 is not a solid one as it can be divided vertically. Thus, the number of ways is  and .

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
def legoBlocks(n, m):
    mod = pow(10, 9) + 7
    ways = [1, 2, 3, 4]
    for i in range(4, m):
        ways.append(ways[i - 1] + ways[i - 2] + ways[i - 3] + ways[i - 4])
    print(ways)
    totalways = pow(ways[m - 1], n)
    print("totalways", totalways)
    for separator in range(1, m):
        leftWidth = separator - 0
        rightWidth = m - separator
        print("left", leftWidth, "right", rightWidth)
        print("leftWays", pow(ways[leftWidth-1], n))
        print("rightWays", pow(ways[rightWidth-1], n))
        totalways -= pow(ways[leftWidth-1], n) * pow(ways[rightWidth-1], n)

    return totalways % mod


if __name__ == '__main__':
    print(legoBlocks(2, 3))
