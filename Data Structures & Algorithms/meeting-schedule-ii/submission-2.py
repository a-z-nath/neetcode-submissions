"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        res = []
        intervals.sort(key=lambda interval: interval.start)
        for interval in intervals:
            s, e = interval.start, interval.end
            add = False
            for i in range(len(res)):
                if s >= res[i][-1]:
                    res[i].append(e)
                    add = True
                    break
            if not add:
                res.append([e])
        return len(res)