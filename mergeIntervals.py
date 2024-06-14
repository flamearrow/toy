from typing import List
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # connected components
        ret = []

        # find the first one that overlaps with nextInterval, need to modify interval
        def retrieveIntervalRange(intervals, nextInterval):
            toRemove = -1
            for index, interval in enumerate(intervals):
                if not interval[0] > nextInterval[1] and not interval[1] < nextInterval[0]:
                    toRemove = index
                    break
            if toRemove != -1:
                return intervals.pop(toRemove)
            else:
                return None

        while intervals:
            nextInterval = intervals.pop()
            nextOverlapRange = retrieveIntervalRange(intervals, nextInterval)
            while nextOverlapRange:
                nextInterval = [min(nextInterval[0], nextOverlapRange[0]), max(nextInterval[1], nextOverlapRange[1])]
                nextOverlapRange = retrieveIntervalRange(intervals, nextInterval)
            # now nextInterval is fully connected
            ret.append(nextInterval)

        return ret

if __name__ == '__main__':
    print(Solution())