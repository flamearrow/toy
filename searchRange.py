from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftBound, rightBound = -1, -1

        l, r = 0, len(nums) - 1

        # search for left bound
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == 0:
                    leftBound = 0
                    break
                else:
                    if nums[mid - 1] < nums[mid]:
                        leftBound = mid
                        break
                    else:  # go left
                        r = mid - 1
            else:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

        # search for right bound
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1:
                    rightBound = len(nums) - 1
                    break
                else:
                    if nums[mid + 1] > nums[mid]:
                        rightBound = mid
                        break
                    else:  # go right
                        l = mid + 1
            else:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

        return [leftBound, rightBound]


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
