# You are given an array start where start = [startX, startY] represents your initial position (startX, startY) in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position (targetX, targetY).
#
# The cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.
#
# There are also some special roads. You are given a 2D array specialRoads where specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road can take you from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use each special road any number of times.
#
# Return the minimum cost required to go from (startX, startY) to (targetX, targetY)
#
# Example 1:
#
# Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
# Output: 5
# Explanation: The optimal path from (1,1) to (4,5) is the following:
# - (1,1) -> (1,2). This move has a cost of |1 - 1| + |2 - 1| = 1.
# - (1,2) -> (3,3). This move uses the first special edge, the cost is 2.
# - (3,3) -> (3,4). This move has a cost of |3 - 3| + |4 - 3| = 1.
# - (3,4) -> (4,5). This move uses the second special edge, the cost is 1.
# So the total cost is 1 + 2 + 1 + 1 = 5.
# It can be shown that we cannot achieve a smaller total cost than 5.
# Example 2:
#
# Input: start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
# Output: 7
# Explanation: It is optimal to not use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7


from typing import List

class Solution:
    def __init__(self):
        pass

    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        def directCostBtn(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        # specialRoads = list(filter(lambda road: road[4] < directCostBtn(road[0], road[1], road[2], road[3]), specialRoads))

        def costBtn(x1a, y1a, x2a, y2a):
            for (x1, y1, x2, y2, cost) in specialRoads:
                if x1a == x1 and y1a == y1 and x2a == x2 and y2a == y2:
                    return min(cost, directCostBtn(x1a, y1a, x2a, y2a))
            return directCostBtn(x1a, y1a, x2a, y2a)

        # cost from start to end through special road
        def costThrough(start, throughRoad, end):
            startx, starty = start
            endx, endy = end
            x1, y1, x2, y2, cost = throughRoad
            return costBtn(startx, starty, x1, y1) + cost + costBtn(x2, y2, endx, endy)

        if len(specialRoads) == 0:
            return costBtn(start[0], start[1], target[0], target[1])

        minsCostWithLastPoint = [0] * len(specialRoads)
        minsCostWithLastPoint[0] = min(
            costBtn(start[0], start[1], target[0], target[1]),
            costThrough(start, specialRoads[0], target)
        )

        for i in range(1, len(specialRoads)):
            minsCostWithLastPoint[i] = costThrough(start, specialRoads[i], target)
            for j in range(0, i):
                jcost = (minsCostWithLastPoint[j] - costBtn(target[0], target[1], specialRoads[j][2], specialRoads[j][3])  # minus distance from j to target
                         + costThrough((specialRoads[j][2], specialRoads[j][3]), specialRoads[i], (target[0], target[1])))  # plus distance from j end to target through i
                minsCostWithLastPoint[i] = min(minsCostWithLastPoint[i], jcost)

        return min(minsCostWithLastPoint)




if __name__ == '__main__':
    s = Solution()
    print(s.minimumCost([1,1], [5,10], [[3,4,5,2,5],[4,5,3,8,3],[3,2,5,3,1]]))
    # print(int('inf'))
