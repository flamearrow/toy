from typing import List
def rotate(nums: List[int], k: int):
    """
    Do not return anything, modify nums in-place instead.
    """
    twoNums = nums + nums
    return twoNums[k + 1:k + 1 + len(nums)]


if __name__ == '__main__':
    print(rotate([1,2,3,4,5,6,7], 3))