# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        ret = 0
        # don't start from duplicate points
        for num in numsSet: # try build the streak from any starting point that doesn't have one before
            # observation - this runs O(n) because it skips a lot of num once its previous has already seen
            #  which means num is considred in the previous nums while loop
            if num-1 not in numsSet: # num could be a new starting point
                curLen = 1
                nextNum = num+1
                while nextNum in numsSet:
                    nextNum += 1
                    curLen +=1
                ret = max(curLen, ret)
        return ret
