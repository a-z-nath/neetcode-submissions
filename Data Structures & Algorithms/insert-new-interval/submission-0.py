class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        mergeStart, mergeEnd = newStart, newEnd
        for s, e in intervals:
            if newStart <= e and newEnd >= s:
                mergeStart = min(s, mergeStart)
                mergeEnd = max(e, mergeEnd)
        idx = 0
        print(mergeStart, mergeEnd)
        while True:
            if idx < len(intervals):
                if intervals[idx][0] >= mergeStart and intervals[idx][1] <= mergeEnd:
                    intervals.pop(idx)
                else:
                    idx += 1
            else:
                break
        intervals.append([mergeStart, mergeEnd])
        intervals.sort()
        print(intervals)
        return intervals