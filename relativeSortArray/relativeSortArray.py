# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
#
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.


# Example 1:
#
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

# Example 2:
# Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# Output: [22,28,8,6,17,44]

from typing import List
class Solution:
    def __init__(self):
        pass

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        currentArr1Head = 0
        for target in arr2:
            nextTargetInext = self.getIndexFrom(arr1, currentArr1Head, target)
            while nextTargetInext >= 0:
                # swap()
                arr1[nextTargetInext] = arr1[currentArr1Head]
                arr1[currentArr1Head] = target
                currentArr1Head += 1
                nextTargetInext = self.getIndexFrom(arr1, currentArr1Head, target)

        # sort from currentArr1Head to end
        subArr = arr1[currentArr1Head:]
        subArr.sort()
        ret = arr1[0:currentArr1Head]
        ret.extend(subArr)
        return ret

    def getIndexFrom(self, arr, currentHead, target):
        for i in range(currentHead, len(arr)):
            if arr[i] == target:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))