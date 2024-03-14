# Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
#
# You may assume the input array always has a valid answer.
#
# Example 1:
#
# Input: nums = [3,5,2,1,6,4]
# Output: [3,5,1,6,2,4]
# Explanation: [1,6,2,5,3,4] is also accepted.
# Example 2:
#
# Input: nums = [6,6,5,6,3,8]
# Output: [6,6,5,6,3,8]

from typing import List

class Solution:

    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            if i % 2 == 1:  # nums[i] needs to be larger than nums[i-1]
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            else:  # nums[i] needs to be smaller than nums[i-1]
                if nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]


    def wiggleSortSlow(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for combination in self.combinations(len(nums)):
            newNums = [nums[i] for i in combination]
            if self.isWiggle(newNums):
                for i in range(len(newNums)):
                    nums[i] = newNums[i]
                break

    def isWiggle(self, newNums):
        for (index, value) in enumerate(newNums):
            if index == len(newNums) - 1:
                return True
            if index % 2 == 0:
                if value > newNums[index+1]:
                    return False
            else:
                if value < newNums[index+1]:
                    return False
        return True


    def combinations(self, size):
        if size == 1:
            return [[0]]
        else:
            ret = []
            for subRes in self.combinations(size-1):
                newElement = size-1
                firstRest = subRes[:]
                firstRest.append(newElement)
                ret.append(firstRest)
                for i in range(len(subRes)-1, -1, -1):
                    newRes = subRes[0:i]
                    newRes.append(newElement)
                    newRes.extend(subRes[i:])
                    ret.append(newRes)

            return ret


if __name__ == '__main__':
    s = Solution()
    nums = [3,5,2,1,6,4]
    s.wiggleSort(nums)
    print(nums)