# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # [(time, isStart)]
        times = [(r[0], True) for r in intervals] + [(r[1], False) for r in intervals]
        times = sorted(times, key = lambda x: (x[0], x[1])) # sorted by time
        ret = 0
        curRequired = 0
        for time, isStart in times:
            if isStart:
                curRequired += 1
                ret = max(ret, curRequired)
            else:
                curRequired -= 1
        return ret