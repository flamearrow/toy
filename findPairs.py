# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3


# def findDup(l):
#     n = len(l)
#     s = sum([i for i in range(1, n + 1)])
#     actualSum = sum(l)
#     return actualSum - s


# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
# Example 1:
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. 5 and 10 never collide.

# Example 2:
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.

# Example 3:
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

# 1, 2, -3, 4, -3
# 1, -3, 4, -3
# -3, 4, -3
# -3, 4


# 1, 2, -3, 4, -3
# 1, 2, -3, 4
# 1, -3, 4
# -3, 4

def findParis(arr):
    left, right = findLeftPRightN(arr)  # 2 -5
    while left != 0 and right != 0:
        if left > abs(right):
            arr.remove(right)
        elif left < abs(right):
            arr.remove(left)
        else:
            arr.remove(left)
            arr.remove(right)
        left, right = findLeftPRightN(arr)

    return arr


def findLeftPRightN(arr):
    for i in range(0, len(arr) - 1):
        left = arr[i]
        right = arr[i + 1]
        if left > 0 and right < 0:
            return left, right

    return 0, 0


if __name__ == '__main__':
    print(findParis([1, 2, -3, 4, -3]))