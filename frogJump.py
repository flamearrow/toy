# A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
#
# Given a list of stones positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
#
# If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.
#
# Example 1:
#
# Input: stones = [0,1,3,5,6,8,12,17]
# Output: true
# Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
# Example 2:
#
# Input: stones = [0,1,2,3,4,8,9,11]
# Output: false
# Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large

from typing import List, Optional
from listNode import ListNode
from treeNode.treeNode import TreeNode
from collections import deque


class Solution:
    def __init__(self):
        pass

    # have a map # [(index: [steps reaching this index])]
    # search from start, for each step i, calculate the distance from all its previous steps
    #  if at previous index, there are steps reaching this index, and one of those steps is +=1 from distance,
    #   it means i can be reached, add that to i

    # space in efficent as we're saving a list at each point
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        l = len(stones)
        c = [[] for _ in range(l)]  # [(index: [steps reaching this index])]
        c[1] = [1]

        for i in range(2, l):
            for prev in range(1, i):
                distance = stones[i] - stones[prev]
                for step in c[prev]:
                    if (step == distance) or ((step + 1) == distance) or ((step - 1) == distance):
                        c[i].append(distance)

        return len(c[l - 1]) > 0

    # similar idea, but build a stoneDict for {value:index} for faster search
    def canCrossDFS(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        stoneDict = {value: index for index, value in enumerate(stones)}  # stoneValue, index
        l = len(stones)
        buffer = {}  # {(curIndex, lastJump): value}

        def canReach(curIndex, lastJump):
            if (curIndex, lastJump) in buffer:
                return buffer[(curIndex, lastJump)]
            if curIndex == l - 1:
                return True
            else:
                for nextJump in [lastJump - 1, lastJump, lastJump + 1]:
                    if nextJump > 0:
                        nextStoneValue = stones[curIndex] + nextJump
                        if nextStoneValue in stoneDict:  # jump to this stone index
                            if canReach(stoneDict[nextStoneValue], nextJump):
                                buffer[(curIndex, lastJump)] = True
                                return True
                buffer[(curIndex, lastJump)] = False
                return False

        return canReach(1, 1)


if __name__ == '__main__':
    print(Solution().canCrossBack([0, 1, 2, 3, 4, 8, 9, 11]))
