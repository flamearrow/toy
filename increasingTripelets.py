from typing import List
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# note: s doesn't necessarily need to be to the left of m
# s and m only indicates the smallest possible fist and second element up to that point
def increasingTriplet(nums: List[int]) -> bool:
    s, m = float('inf'), float('inf')
    for num in nums:
        if num <= s:
            s = num
        elif num <= m:
            m = num
        else:  # s < m < num
            return True
    return False


if __name__ == '__main__':
    print(increasingTriplet([1, 2, -4, -3, -3]))
    # print(increasingTriplet([5, 1, 5, 0, 4, 6]))