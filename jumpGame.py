# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index


from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # starting from right to left, result[i] means from i if one can jump to end
        result = [False] * (len(nums))
        # last one is True
        result[len(nums)-1] = True

        lastGoodIndex = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            # if this node can jump beyond lastGood, then this is also good
            if i + nums[i] >= lastGoodIndex:
                result[i] = True
                # now this index is a good index, update it
                lastGoodIndex = i

        return result[0]

    def canJumpRecursive(self, nums: List[int]) -> bool:
        # all indices that can't reach end
        buffer = set()

        def search(currentIndex):
            if currentIndex in buffer:
                return False
            if currentIndex == len(nums) - 1:
                return True
            else:
                jumpLength = nums[currentIndex]
                for nextIndex in range(currentIndex + 1, currentIndex + jumpLength + 1):
                    if search(nextIndex):
                        return True
                buffer.add(currentIndex)
                return False

        return search(0)

if __name__ == '__main__':
    print(Solution())